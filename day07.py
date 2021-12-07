from utils import read_input
from collections import Counter

DAY = 7


def parse(input_s):
    return [int(i) for i in input_s.strip().split(',')]


def part_one(data):
    return min(sum(abs(x - y) for y in data) for x in data)


def part_two(data):
    return min(sum(abs(x - y) * (abs(x - y) + 1) / 2 for y in data) for x in data)

if __name__ == "__main__":
    data = parse(read_input(DAY))
    print(part_two(data))
