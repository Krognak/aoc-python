import math
from itertools import combinations

with open("2015/day02/input.txt") as f:
    data = f.read().splitlines()


def get_wrapping_total(data):
    """Return total area of wrapping paper required"""
    wrapping_total = 0
    for line in data:
        areas = [int(i) * int(j) for i, j in combinations(line.split("x"), 2)]
        wrapping_total += 2 * sum(areas) + min(areas)
    return wrapping_total


def get_ribbon_total(data):
    """Return total length of ribbon required"""
    ribbon_total = 0
    for datum in data:
        a, b, c = datum.split("x")
        dims = [int(a), int(b), int(c)]
        ribbon_total += math.prod(dims)
        dims.remove(max(dims))
        ribbon_total += 2 * sum(dims)
    return ribbon_total


if __name__ == "__main__":
    print(get_wrapping_total(data))
    print(get_ribbon_total(data))
