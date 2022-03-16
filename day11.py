import math
from collections import defaultdict
from itertools import product
from time import sleep
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


def display(grid, h, w):
    print("\033[2J\033[1;1H")
    img = [[' '] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[(i, j)] == 0:
                img[i][j] = "\033[33;1m\u25A0\033[0m"
            else:
                img[i][j] = "\033[34;1m\u25A0\033[0m"
    print('\n'.join([''.join(l) for l in img]))


def part_one(grid):
    return sum(step(grid) for _ in range(100))


def part_two(grid):
    h = max(i for (i, _) in grid) + 1
    w = max(j for (_, j) in grid) + 1
    octopus_count = len(grid)
    step_count = 0
    while True:
        flash_count = step(grid)
        step_count += 1
        display(grid, h, w)
        print(f"Step: {step_count}")
        if flash_count == octopus_count:
            return step_count
        sleep(0.1)


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    part_two(data)
