import math
import itertools
from utils import read_input


DAY = 18


def parse(data):
    return [eval(line) for line in data.splitlines()]


def serialize(number):
    if isinstance(number, Number):
        return number.value
    l, r = number
    return [serialize(l), serialize(r)]


def _add(number, value, rightmost=True):
    if value == 0:
        return number
    if isinstance(number, int):
        return number + value
    l, r = number
    if rightmost:
        return [l, _add(r, value, rightmost)]
    return [_add(l, value, rightmost), r]


def add_rightmost(number, value):
    return _add(number, value, rightmost=True)


def add_leftmost(number, value):
    return _add(number, value, rightmost=False)


def rec_explode(number, depth=0):
    if isinstance(number, int):
        return False, 0, 0, number
    if depth == 4:
        l, r = number
        return True, l, r, 0
    a, b = number
    did_explode, l, r, a = rec_explode(a, depth + 1)
    if did_explode:
        return did_explode, l, 0, [a, add_leftmost(b, r)]
    did_explode, l, r, b = rec_explode(b, depth + 1)
    if did_explode:
        return did_explode, 0, r, [add_rightmost(a, l), b]
    return False, 0, 0, number


def rec_split(number):
    if isinstance(number, int):
        if number < 10:
            return False, number
        half = number / 2
        return True, [math.floor(half), math.ceil(half)]
    r, l = number
    has_split, r = rec_split(r)
    if not has_split:
        has_split, l = rec_split(l)
    return has_split, [r, l]


def reduce_number(number):
    while True:
        expl, _, _, number = rec_explode(number)
        if expl:
            continue
        s, number = rec_split(number)
        if s:
            continue
        return number


def snail_add(n1, n2):
    return reduce_number([n1, n2])


def magnitude(number):
    if isinstance(number, int):
        return number
    l, r = number
    return 3 * magnitude(l) + 2 * magnitude(r)


def part_one(data):
    res = data[0]
    for number in data[1:]:
        res = snail_add(res, number)
    return magnitude(res)


def part_two(data: str) -> int:
    return max(magnitude(snail_add(a, b)) for (a, b) in itertools.permutations(data, 2))


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_one(data))
    # Slow!
    # print(part_two(data))
