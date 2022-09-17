with open("2015/day01/input.txt") as f:
    data = f.read()

# final floor = sum of 'up' instructions less sum of 'down' instructions
print(data.count("(") - data.count(")"))

# iterate over increasingly larger slices of input, stopping when floor = -1
for i, _ in enumerate(data):
    if data[: i + 1].count("(") - data[: i + 1].count(")") == -1:
        print(i + 1)
        break
