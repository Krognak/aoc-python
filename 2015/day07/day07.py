import re

with open("2015/day07/input.txt") as f:
    input_ = f.read()


def assign(wires, **kwargs):
    try:
        wires[kwargs["wire"]] = wires[kwargs["rarg"]]
    except KeyError:
        wires[kwargs["wire"]] = int(kwargs["rarg"])


def bit_not(wires, **kwargs):
    wires[kwargs["wire"]] = ~wires[kwargs["rarg"]] & (2**16 - 1)


def bit_and(wires, **kwargs):
    try:
        wires[kwargs["wire"]] = wires[kwargs["larg"]] & wires[kwargs["rarg"]]
    except KeyError:
        wires[kwargs["wire"]] = int(kwargs["larg"]) & wires[kwargs["rarg"]]


def bit_or(wires, **kwargs):
    wires[kwargs["wire"]] = wires[kwargs["larg"]] | wires[kwargs["rarg"]]


def bit_lshift(wires, **kwargs):
    wires[kwargs["wire"]] = wires[kwargs["larg"]] << int(kwargs["rarg"])


def bit_rshift(wires, **kwargs):
    wires[kwargs["wire"]] = wires[kwargs["larg"]] >> int(kwargs["rarg"])


OPERATORS = {
    "NOT": bit_not,
    "": assign,
    "AND": bit_and,
    "OR": bit_or,
    "LSHIFT": bit_lshift,
    "RSHIFT": bit_rshift,
}

PATTERN = re.compile(
    r"(?P<larg>\w*?)\s*(?P<op>AND|OR|LSHIFT|RSHIFT|NOT|)?\s*(?P<rarg>\w+)\s->\s(?P<wire>\w+)"  # noqa: E501
)


def find_a(data, wires=None):
    if not wires:
        wires = {}
    while len(wires) < len(data.splitlines()):
        for i in data.splitlines():
            m = PATTERN.match(i)
            if m.group("wire") not in wires:
                try:
                    OPERATORS[m.group("op")](wires, **m.groupdict())
                except (KeyError, ValueError):
                    pass
    return wires["a"]


a = find_a(input_)
print(a)
print(find_a(input_, wires={"b": a}))
