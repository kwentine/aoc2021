import math
from collections import defaultdict
from itertools import product

from utils import read_input

DAY = 11


def parse(input_str):
    grid = defaultdict(lambda: -math.inf)
    for (i, line) in enumerate(input_str.splitlines()):
        for (j, n) in enumerate(line):
            grid[i, j] = int(n)
    return grid


def neighbors(i, j):
    steps = [-1, 0, 1]
    for dx, dy in product(steps, steps):
        if dy == dx == 0:
            continue
        yield i + dx, j + dy


def step(grid):
    flash_count = 0
    todo = []
    for (i, j) in grid:
        grid[i, j] += 1
        if grid[i, j] > 9:
            todo.append((i, j))
    while todo:
        i, j = todo.pop()
        for a, b in neighbors(i, j):
            if (a, b) in todo or grid[a, b] == 0:
                continue
            grid[a, b] += 1
            if grid[a, b] > 9:
                todo.append((a, b))
        grid[i, j] = 0
        flash_count += 1
    return flash_count


def part_one(grid):
    return sum(step(grid) for _ in range(100))


def part_two(grid):
    octopus_count = len(grid)
    step_count = 0
    while True:
        flash_count = step(grid)
        step_count += 1
        if flash_count == octopus_count:
            return step_count


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_two(data))
