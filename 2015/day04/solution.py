import hashlib

with open("2015/day04/input.txt") as f:
    data = f.read().encode()


def five_zeroes(data):
    trial = 1
    while True:
        h = hashlib.md5(data + str(trial).encode())
        if h.hexdigest()[0:5] == "00000":
            break
        trial += 1
    return trial


def six_zeroes(data):
    trial = 1
    while True:
        h = hashlib.md5(data + str(trial).encode())
        if h.hexdigest()[0:6] == "000000":
            break
        trial += 1
    return trial


if __name__ == "__main__":
    print(five_zeroes(data))
    print(six_zeroes(data))
