from utils import read_input


DAY = 4


def parse(input_s):
    numbers, *grids = input_s.split('\n\n')
    numbers = [int(n) for n in numbers.split(',')]
    grids = [parse_grid(grid) for grid in grids]
    return numbers, grids


def parse_grid(grid_s: str) -> dict:
    lines = [[int(n) for n in line.split()] for line in grid_s.splitlines()]
    height = len(lines)
    width = len(lines[0])
    grid = {
        'height': height,
        'width': width,
        'row_marked_count': [0] * height,
        'col_marked_count': [0] * width,
        'unmarked_sum': sum(sum(line) for line in lines)
    }
    for i, line in enumerate(lines):
        for j, n in enumerate(line):
            grid[n] = (i, j)
    return grid


def mark(n, grid):
    if n not in grid:
        return
    i, j = grid[n]
    grid['row_marked_count'][i] += 1
    grid['col_marked_count'][j] += 1
    grid['unmarked_sum'] -= n


def bingo(grid):
    return (grid['height'] in grid['row_marked_count'] or
            grid['width'] in grid['col_marked_count'])


def part_one(numbers, grids):
    for n in numbers:
        for grid in grids:
            mark(n, grid)
            if bingo(grid):
                return grid['unmarked_sum'] * n
    raise RuntimeError("No winning grid")


def part_two(numbers, grids):
    for n in numbers:
        next_grids = []
        for grid in grids:
            mark(n, grid)
            if not bingo(grid):
                next_grids.append(grid)
        if not next_grids:
            return grid['unmarked_sum'] * n
        grids = next_grids


if __name__ == "__main__":
    numbers, grids = parse(read_input(4))
    print(part_two(numbers, grids))
