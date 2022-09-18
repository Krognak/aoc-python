import re

import numpy as np

pattern = re.compile(
    r"(?P<kw>^\w+\s*\w*)\s(?P<x1>\d+),(?P<y1>\d+)\sthrough\s(?P<x2>\d+),(?P<y2>\d+)"
)

with open("2015/day06/input.txt") as f:
    data = f.readlines()

lights = np.zeros((1000, 1000), dtype=int)
for instruction in data:
    m = pattern.match(instruction)
    x1 = int(m.group("x1"))
    x2 = int(m.group("x2"))
    y1 = int(m.group("y1"))
    y2 = int(m.group("y2"))
    kw = m.group("kw")
    if kw == "toggle":
        lights[x1 : x2 + 1, y1 : y2 + 1] ^= 1
    elif kw == "turn off":
        lights[x1 : x2 + 1, y1 : y2 + 1] = 0
    else:
        lights[x1 : x2 + 1, y1 : y2 + 1] = 1

print(np.sum(lights))

lights = np.zeros((1000, 1000), dtype=int)
for instruction in data:
    m = pattern.match(instruction)
    x1 = int(m.group("x1"))
    x2 = int(m.group("x2"))
    y1 = int(m.group("y1"))
    y2 = int(m.group("y2"))
    kw = m.group("kw")
    if kw == "toggle":
        lights[x1 : x2 + 1, y1 : y2 + 1] += 2
    elif kw == "turn off":
        lights[x1 : x2 + 1, y1 : y2 + 1] -= 1
        lights = np.where(lights < 0, 0, lights)
    else:
        lights[x1 : x2 + 1, y1 : y2 + 1] += 1

print(np.sum(lights))
