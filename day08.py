from utils import read_input
from collections import Counter

DAY = 8


def parse(input_s):
    data = []
    for line in input_s.splitlines():
        patterns, digits = line.split('|')
        patterns = tuple(set(s) for s in patterns.split())
        digits = tuple(set(s) for s in digits.split())
        data.append((patterns, digits))
    return data


PATTERNS = [
    set("abcefg"),
    set("cf"),
    set("acdeg"),
    set("acdfg"),
    set("bcdf"),
    set("abdfg"),
    set("abdfge"),
    set("acf"),
    set("abcdefg"),
    set("abcdfg")
]


BASIS = {i: PATTERNS[i] for i in (1, 4, 7, 8)}


def signature(pattern, basis):
    return tuple(len(pattern & basis[i]) for i in (1, 4, 7, 8))

# Idea: a digit is uniquely identified by its "imprint" on the base
# digits, ie the size of its intersection with each base digit.
SIGNATURES_MAP = {
    signature(PATTERNS[i], BASIS): i for i in (0, 2, 3, 5, 6, 9)
}


def key(pattern):
    return "".join(sorted(pattern))


def decode_patterns(patterns):
    basis = {}
    ambiguous = []
    for s in patterns:
        if len(s) == 2:
            basis[1] = s
        elif len(s) == 3:
            basis[7] = s
        elif len(s) == 4:
            basis[4] = s
        elif len(s) == 7:
            basis[8] = s
        else:
            ambiguous.append(s)
    for s in ambiguous:
        d = SIGNATURES_MAP[signature(s, basis)]
        basis[d] = s
    return {
        key(s): d for d, s in basis.items()
    }


def part_one(data):
    counter = 0
    for _, digits in data:
        for s in digits:
            if len(s) in (2, 3, 4, 7):
                counter += 1
    return counter


def part_two(data):
    s = 0
    for patterns, digits in data:
        m = decode_patterns(patterns)
        digits = [m[key(d)] for d in digits]
        value = sum(10 ** (3 - k) * digits[k] for k in range(4))
        s += value
    return s
             

if __name__ == "__main__":
    data = parse(read_input(DAY))
    print(part_two(data))
