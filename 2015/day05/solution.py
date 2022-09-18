import re

with open("2015/day05/input.txt") as f:
    data = f.readlines()


def check_if_good(data):
    good = 0
    for string in data:
        vowels_match = re.findall(r"[aeiou]", string)
        repeated_char_match = re.search(r"(.)\1+", string)
        forbidden_chars = not re.search(r"ab|cd|pq|xy", string)
        if all([len(vowels_match) >= 3, repeated_char_match, forbidden_chars]):
            good += 1
    return good


def check_if_better(data):
    better = 0
    for string in data:
        cond1 = re.findall(r"(..)[^\1]*\1", string)
        cond2 = re.search(r"(.)[^\1]\1", string)
        if all([cond1, cond2]):

            better += 1
    return better


if __name__ == "__main__":
    print(check_if_good(data))
    print(check_if_better(data))
