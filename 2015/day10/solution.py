from itertools import groupby

with open("2015/day10/input.txt") as f:
    data = f.read()


def turn(arg):
    output = []
    for k, g in groupby(arg):
        output.append(str(len(list(g))))
        output.append(k)
    return "".join(output)


for i in range(40):
    data = turn(data)
print(len(data))

for i in range(10):
    data = turn(data)
print(len(data))
