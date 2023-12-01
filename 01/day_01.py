import sys
import re

def get_calibration_value(line):
    digits = [c for c in line if c.isdigit()]
    return int(digits[0] + digits[-1])

if __name__=="__main__":

    with open(sys.argv[1],'r') as infile:
        input_lines = infile.readlines()

    # Part one
    calibration_total = 0
    for line in input_lines:
        calibration_total += get_calibration_value(line)

    print(f"Part One Calibration Total: {calibration_total}")

    # Part two
    recalibration_total = 0
    pattern = re.compile("[1-9]|one|two|three|four|five|six|seven|eight|nine")
    nrettap = re.compile("enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|[1-9]")
    map = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5,
           "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9,
           "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5,
           "6" : 6, "7" : 7, "8" : 8, "9" : 9}
    
    for line in input_lines:
        first = pattern.search(line).group(0)
        last = nrettap.search(line[::-1]).group(0)[::-1]
        recalibration_total += 10 * map[first] + map[last]

    print(f"Part Two (Re-)Calibration Total: {recalibration_total}")