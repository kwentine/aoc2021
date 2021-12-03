from utils import read_input
from typing import List, Callable
from functools import reduce

DAY = 3


def parse(data: str) -> List[List[int]]:
    return [[int(i) for i in line]
            for line in data.splitlines()]


def vector_sum(left: List[int], right: List[int]) -> List[int]:
    return [x + y for (x, y) in zip(right, left)]


def vector_to_int(vect: List[int]) -> int:
    return int(''.join(str(i) for i in vect), base=2)


def gamma_vect(vectors: List[List[int]]) -> List[int]:
    majority = len(vectors) / 2
    return [int(x >= majority) for x in reduce(vector_sum, vectors)]


def gamma_i(vectors: List[List[int]], i: int) -> int:
    majority = len(vectors) / 2
    return int(sum(n[i] for n in vectors) >= majority)


def epsilon_i(vectors: List[List[int]], i: int) -> int:
    majority = len(vectors) / 2
    return int(sum(n[i] for n in vectors) < majority)


def part_one(vectors: List[List[int]]) -> int:
    gamma = vector_to_int(gamma_vect(vectors))
    return gamma * (~gamma & 0xfff)


def filter_pass(criterium: bool, i: int, vectors: List[List[int]]):
    return [n for n in vectors if n[i] == criterium]


def filter_until_single(vectors: List[List[int]], criterium_func: Callable):
    for i in range(12):
        if len(vectors) == 1:
            break
        criterium = criterium_func(vectors, i)
        vectors = filter_pass(criterium, i, vectors)
    assert len(vectors) == 1
    return vector_to_int(vectors.pop())


def part_two(vectors: List[List[int]]):
    return (filter_until_single(vectors, gamma_i)
            * filter_until_single(vectors, epsilon_i))


if __name__ == "__main__":
    vectors = parse(read_input(DAY))
    print(part_one(vectors))
    print(part_two(vectors))
