import sys

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def parse_line(line):
    draws = []
    prefix, draw_strings = line.strip().split(": ")
    for draw_str in draw_strings.split("; "):
        draws.append(parse_draw(draw_str))
    return draws


def parse_draw(draw):
    cts = {'red' : 0, 'green': 0, 'blue': 0}
    for color_str in draw.split(", "):
        ct, color = color_str.split(" ")
        ct = int(ct)
        cts[color] = ct
    return cts


if __name__=="__main__":

    with open(sys.argv[1],'r') as infile:
        lines = infile.readlines()

    part_one_total = 0
    part_two_power = 0
    for i in range(1,len(lines)+1):
        line = lines[i-1]
        rgb_max = [0,0,0]
        for draw in parse_line(line):
            rgb_max[0] = max(rgb_max[0],draw['red'])
            rgb_max[1] = max(rgb_max[1],draw['green'])
            rgb_max[2] = max(rgb_max[2],draw['blue'])
        if (rgb_max[0] <= RED_MAX) and (rgb_max[1] <= GREEN_MAX) and (rgb_max[2] <= BLUE_MAX):
            part_one_total += i
        part_two_power += rgb_max[0] * rgb_max[1] * rgb_max[2]
    print(part_one_total)
    print(part_two_power)


    