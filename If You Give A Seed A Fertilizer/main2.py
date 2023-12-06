import sys
import re

from itertools import groupby

## PARSE INPUT
def parse_ints(s):
    return list(map(int, re.findall("\d+", s)))

def split_list(lst):
    return (list(group) for _, group in groupby(lst, lambda x: x != ''))

almanac = [l.strip() for l in open(sys.argv[1]).readlines()]
seeds = parse_ints(almanac[0])
maps = [[parse_ints(x) for x in m[1:]] for m in split_list(almanac[2:])]

## PART 1
def part1(seed):
    for m in maps:
        for to, start, count in m:
            if (start <= seed <= start + count):
                seed += to - start
                break


    return seed    

print("1:", min(map(part1, seeds)))

## PART 2
def find_overlap(r1, r2):
    r1_start, r1_end = r1
    r2_start, r2_end = r2
    o_start = max(r1_start, r2_start)
    o_end = min(r1_end, r2_end)
    return (o_start, o_end) if o_start <= o_end else None

def shift_range(r, delta):
    r_start, r_end = r
    return (r_start + delta, r_end + delta)

def split_range(r, overlap):
    result = set()

    o_start, o_end = overlap
    r_start, r_end = r

    if r_start < o_start:
        result.add((r_start, o_start-1))

    if r_end > o_end:
        result.add((o_end+1, r_end))

    return result

def as_range(start_count):
    start, count = start_count
    return (start, start + count - 1)

def part2():
    ranges = set(map(as_range, zip(seeds[0::2], seeds[1::2])))
    
    for m in maps:
        shifted_ranges = set()

        for to, start, count in m:
            for r in ranges.copy():
                if overlap := find_overlap(r, as_range((start, count))):
                    ranges.remove(r)
                    ranges |= split_range(r, overlap)
                    shifted_ranges.add(shift_range(overlap, to - start))

        ranges |= shifted_ranges    

    return ranges

print("2:", min(min(part2())))