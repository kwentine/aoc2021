from utils import read_input
from typing import List
from functools import reduce

DAY = 3

def parse(data: str) -> List[List[int]]:
    return [[int(i) for i in line]
            for line in data.splitlines()]


def vector_sum(left, right):
    return [x + y for (x, y) in zip(right, left)]


def vector_to_int(vect):
    return int(''.join(str(i) for i in vect), base=2)


def gamma_vect(data):
    majority = len(data) / 2
    return [int(x >= majority) for x in reduce(vector_sum, numbers)]


def gamma_i(numbers, i):
    majority = len(numbers) / 2
    return int(sum(n[i] for n in numbers) >= majority)


def epsilon_i(numbers, i):
    majority = len(numbers) / 2
    return int(sum(n[i] for n in numbers) < majority)


def part_one(data):
    gamma = vector_to_int(gamma_vect(numbers))
    return gamma * (~gamma & 0xfff)


def filter_pass(criterium, i, numbers):
    return [n for n in numbers if n[i] == criterium]


def filter_until_single(numbers, criterium_func):
    for i in range(12):
        if len(numbers) == 1:
            break
        criterium = criterium_func(numbers, i)
        numbers = filter_pass(criterium, i, numbers)
    assert len(numbers) == 1
    return vector_to_int(numbers.pop())

def part_two(numbers):
    return filter_until_single(numbers, gamma_i) * filter_until_single(numbers, epsilon_i)

if __name__ == "__main__":
    numbers = parse(read_input(DAY))
    print(part_one(numbers))
    print(part_two(numbers))
