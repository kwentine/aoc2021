from utils import read_input
from collections import defaultdict

DAY = 9


def parse(input_s):
    grid = {}
    for i, line in enumerate(input_s.splitlines()):
        for j, digit in enumerate(line):
            grid[(i, j)] = int(digit)
    return grid


def neighbors(i, j):
    return (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)


def argmin(i, j, grid):
    cur_pos, cur_min = (i, j), grid[i, j]
    for (a, b) in neighbors(i, j):
        d = grid.get((a, b), 9)
        if d < cur_min:
            cur_pos, cur_min = (a, b), d
    return cur_pos


def find_basin(i, j, upslope_neighbors):
    """Find the attraction basin by moving upslope in all directions"""
    basin = set()
    border = [(i, j)]
    while border:
        current = border.pop()
        g = upslope_neighbors[current]
        border.extend(g)
        basin.add(current)
    return basin


def part_two(grid):
    upsolpe_neighbors = defaultdict(list)
    low_points = []
    for (i, j), d in grid.items():
        x, y = argmin(i, j, grid)
        if d == 9:
            continue
        if (x, y) == (i, j):
            low_points.append((i, j))
        else:
            upsolpe_neighbors[(x, y)].append((i, j))
    basin_sizes = list(sorted([len(find_basin(i, j, upsolpe_neighbors))
                               for (i, j) in low_points]))
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


def part_one(grid):
    low_sum = 0
    for (i, j), d in grid.items():
        if (i, j) == argmin(i, j, grid) and d != 9:
            low_sum += d + 1
    return low_sum


if __name__ == "__main__":
    grid = parse(read_input(9))
    print(part_one(grid))
    print(part_two(grid))
