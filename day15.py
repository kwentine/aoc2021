from utils import read_input
from math import inf
from collections import defaultdict
import heapq

DAY = 15


def parse(data):
    grid = defaultdict(lambda: inf)
    for i, line in enumerate(data.splitlines()):
        for j, risk in enumerate(line):
            grid[(i, j)] = int(risk)
    return grid, i, j


def extend(grid, imax, jmax):
    new_grid = defaultdict(lambda: inf)
    for i in range(imax + 1):
        for j in range(jmax + 1):
            for k in range(5):
                for l in range(5):
                    ik, jl = i + k * (imax + 1), j + l * (jmax + 1)
                    new_risk = grid[i, j] + k + l
                    if new_risk > 9:
                        new_risk -= 9
                    new_grid[ik, jl] = new_risk
    return new_grid, imax + 4 * (imax + 1), jmax + 4 * (jmax + 1)


def neighbors(i, j):
    yield i + 1, j
    yield i, j + 1
    yield i - 1, j
    yield i, j - 1


def part_one(grid, imax, jmax):
    visited = set()
    todo = [(0, 0, 0)]
    distances = defaultdict(lambda: inf)
    while todo:
        d, i, j = heapq.heappop(todo)
        if (i, j) in visited:
            continue
        if (i, j) == (imax, jmax):
            return d
        for (a, b) in neighbors(i, j):
            l = d + grid[(a, b)]
            if l < distances[a, b]:
                distances[a, b] = l
                heapq.heappush(todo, (l, a, b))
        visited.add((i, j))


def part_two(grid, imax, jmax):
    grid, imax, jmax = extend(grid, imax, jmax)
    return part_one(grid, imax, jmax)


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_two(*data))
