from collections import defaultdict
from itertools import permutations

with open("2015/day09/input.txt") as f:
    data = f.read()

distances = defaultdict(dict)
for i in data.splitlines():
    node, edge = i.split(" to ")
    dest, dist = edge.split(" = ")
    # not a directed graph so if A -> B then B -> A
    distances[node].update({dest: int(dist)})
    distances[dest].update({node: int(dist)})

nodes = distances.keys()


def get_distance(x):
    return distances[x[0]][x[1]]


# brute-forcing all possible routes, assuming complete graph
max = float("inf")
for i in permutations(nodes):
    total = 0
    for j in range(len(i) - 1):
        total += get_distance(i[j:j+2])
    if total < max:
        max = total
print(max)

min = float("-inf")
for i in permutations(nodes):
    total = 0
    for j in range(len(i) - 1):
        total += get_distance(i[j:j+2])
    if total > min:
        min = total
print(min)
