with open("2015/day08/input.txt") as f:
    input_ = f.read().splitlines()

# eval to reduce escaped characters to single characters
print(sum([len(line) - len(eval(line)) for line in input_]))

# add two "", escape backslashes, and escape quotation marks per line
print(sum([2 + line.count("\\") + line.count('"') for line in input_]))
