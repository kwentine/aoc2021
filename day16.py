from utils import read_input
from functools import reduce
import operator as op

DAY = 16

TYPE_LITERAL = 4

FIXED_LENGTH = 0
SUBPACKET_COUNT = 1
FIXED_LENGTH_WIDTH = 15
SUB_COUNT_WIDTH = 11


OPERATORS = {
    0: lambda l: reduce(op.add, l, 0),
    1: lambda l: reduce(op.mul, l, 1),
    2: min,
    3: max,
    5: lambda l: int(l[0] > l[1]),
    6: lambda l: int(l[0] < l[1]),
    7: lambda l: int(l[0] == l[1])
}


def parse(data):
    w = len(data.strip()) * 4
    return bin(int(data, base=16))[2:].zfill(w)


def parse_bits(message, offset):
    (version, type_id), offset = parse_header(message, offset)
    if type_id == TYPE_LITERAL:
        number, offset = parse_number(message, offset)
        return (version, type_id, number), offset
    packets, offset = parse_list(message, offset)
    return (version, type_id, packets), offset


def parse_header(message, offset):
    version = int(message[offset:offset+3], base=2)
    type_id = int(message[offset + 3:offset + 6], base=2)
    return (version, type_id), offset + 6


def parse_number(message, offset):
    feed = 1
    parts = []
    while feed:
        feed = int(message[offset])
        chunk = message[offset + 1:offset+5]
        parts.append(chunk)
        offset += 5
    value = int("".join(parts), base=2)
    return value, offset


def _parse_int(message, offset, width):
    return int(message[offset:offset + width], base=2), offset + width


def parse_list(message, offset):
    length_type = int(message[offset])
    if length_type == FIXED_LENGTH:
        fixed_length, offset = _parse_int(
            message, offset + 1, FIXED_LENGTH_WIDTH)
        packets, offset = parse_fixed_length(message, offset, fixed_length)
    else:
        sub_count, offset = _parse_int(message, offset + 1, SUB_COUNT_WIDTH)
        packets, offset = parse_subpackets(message, offset, sub_count)
    return packets, offset


def parse_fixed_length(message, offset, length):
    stop = offset + length
    packets = []
    while offset < stop:
        packet, offset = parse_bits(message, offset)
        packets.append(packet)
    return packets, offset


def parse_subpackets(message, offset, sub_count):
    subpackets = []
    for i in range(sub_count):
        packet, offset = parse_bits(message, offset)
        subpackets.append(packet)
    return subpackets, offset


def sum_versions(tree):
    a, b, c = tree
    if b == TYPE_LITERAL:
        return a
    else:
        return a + sum(sum_versions(t) for t in c)


def evaluate(tree):
    version, type_id, payload = tree
    if type_id == TYPE_LITERAL:
        return payload
    return OPERATORS[type_id]([evaluate(p) for p in payload])


def part_one(data: str) -> int:
    tree, _ = parse_bits(data, 0)
    return sum_versions(tree)


def part_two(data: str) -> int:
    tree, _ = parse_bits(data, 0)
    return evaluate(tree)


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_two(data))
