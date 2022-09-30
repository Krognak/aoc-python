import re
from collections import defaultdict

instruction_pattern = r"(^\w+\s*\w*)\s(\d+,\d+)\sthrough\s(\d+,\d+)"

with open("2015/day06/input.txt") as f:
    data = f.readlines()


def part1(data):
    lights = defaultdict(lambda: 0)
    for datum in data:
        m = re.match(instruction_pattern, datum)
        instruction = m.group(1)
        x1 = m.group(2).split(",")
        x2 = m.group(3).split(",")
        coords = [
            (x, y)
            for x in range(int(x1[0]), int(x2[0]) + 1)
            for y in range(int(x1[1]), int(x2[1]) + 1)
        ]
        if instruction == "turn off":
            for coord in coords:
                lights[coord] = 0
        elif instruction == "toggle":
            for coord in coords:
                lights[coord] ^= 1
        else:
            for coord in coords:
                lights[coord] = 1

    return sum(lights.values())


def part2(data):
    lights = defaultdict(lambda: 0)
    for datum in data:
        m = re.match(instruction_pattern, datum)
        instruction = m.group(1)
        x1 = m.group(2).split(",")
        x2 = m.group(3).split(",")
        coords = [
            (x, y)
            for x in range(int(x1[0]), int(x2[0]) + 1)
            for y in range(int(x1[1]), int(x2[1]) + 1)
        ]
        if instruction == "turn off":
            for coord in coords:
                lights[coord] -= 1
                if lights[coord] < 0:
                    lights[coord] = 0
        elif instruction == "toggle":
            for coord in coords:
                lights[coord] += 2
        else:
            for coord in coords:
                lights[coord] += 1

    return sum(lights.values())


if __name__ == "__main__":
    print(part1(data))
    print(part2(data))
