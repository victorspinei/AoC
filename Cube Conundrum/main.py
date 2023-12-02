import re

cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

TESTING = True
SECOND_PART = True

game_id_regex = re.compile(r'Game \d+:')
sections_regex = re.compile(r'(( (\d+) (blue|red|green),*)+;*)+')
colors_regex = re.compile(r' (\d+) (blue|red|green)')

def main():
    sum = 0
    file = input("Type the name of the file: ")
    with open(file + '.txt', 'r') as f:
        if not SECOND_PART:
            sum += part1(f)
        else:
            sum += part2(f)

    if TESTING and not SECOND_PART and file == 'i1':
        if sum == 8:
            print('Test passed')
        else:
            print('Test failed')

    if TESTING and SECOND_PART and file == 'i1':
        if sum == 2286:
            print('Test passed')
        else:
            print('Test failed')

    print(sum)

def part1(f):
    sum = 0
    for line in f.readlines():
        game_id = re.compile(r'\d+').search(game_id_regex.search(line).group()).group()
        sections = sections_regex.search(line).group().split(';')

        valid = True

        for section in sections:
            sections_sum = {
                'red': 0,
                'green': 0,
                'blue': 0
            }

            colors = colors_regex.findall(section)
            for color in colors:
                sections_sum[color[1]] += int(color[0])


            if sections_sum['red'] > cubes['red'] or sections_sum['blue'] > cubes['blue'] or sections_sum['green'] > cubes['green']:
                valid = False
                break

        if valid:
            sum += int(game_id)

    
    return sum

def part2(f):
    sum = 0
    for line in f.readlines():
        line_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        sections = sections_regex.search(line).group().split(';')
        for section in sections:
            sections_sum = {
                'red': 0,
                'green': 0,
                'blue': 0
            }

            colors = colors_regex.findall(section)
            for color in colors:
                sections_sum[color[1]] = max(int(color[0]), sections_sum[color[1]])

            line_cubes['red'] = max(sections_sum['red'], line_cubes['red'])
            line_cubes['green'] = max(sections_sum['green'], line_cubes['green'])
            line_cubes['blue'] = max(sections_sum['blue'], line_cubes['blue'])


        sum += line_cubes['red'] * line_cubes['blue'] * line_cubes['green']

    return sum

if __name__ == "__main__":
    main()