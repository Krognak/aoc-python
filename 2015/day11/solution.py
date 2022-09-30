import string
from pathlib import Path

straights = [string.ascii_lowercase[i : i + 3] for i in range(24)]
forbidden = ["i", "o", "l"]
doubles = [i + i for i in string.ascii_lowercase]


class Password:
    def __init__(self, input_):
        self.value = [i for i in map(ord, input_)]
        self.len = len(input_)
        self.chars = "".join((map(chr, self.value)))

    def increment(self, index: int = -1):
        if self.value[index] + 1 > 122:
            self.value[index] = 97
            self.chars = "".join((map(chr, self.value)))
            self.increment(index - 1)
        else:
            self.value[index] += 1
            self.chars = "".join((map(chr, self.value)))

    def check_straights(self):
        return any([i in self.chars for i in straights])

    def check_not_forbidden(self):
        return any([i not in self.chars for i in forbidden])

    def check_doubles(self):
        double_count = {i: self.chars.count(i) for i in doubles}
        no_repeats = all([j <= 1 for j in double_count.values()])
        return all([sum(double_count.values()) >= 2, no_repeats])

    def valid_pass(self):
        return all(
            [self.check_doubles(), self.check_not_forbidden(), self.check_straights()]
        )


def update_password(password: Password):
    while True:
        password.increment()
        if password.valid_pass():
            break


password1 = Password(Path("2015/day11/input.txt").read_text())

update_password(password1)

print(password1.chars)

password2 = Password(password1.chars)

update_password(password2)

print(password2.chars)
