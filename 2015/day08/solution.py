with open("2015/day08/input.txt") as f:
    input_ = f.read().splitlines()

print(sum([len(line) - len(eval(line)) for line in input_]))

print(sum([2 + line.count("\\") + line.count('"') for line in input_]))
