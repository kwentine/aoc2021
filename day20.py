from utils import read_input
from collections import defaultdict, deque
from tqdm import tqdm

DAY = 20


def parse(data):
    algo, img = data.split("\n\n")
    return parse_algo(algo), parse_img(img)


def parse_algo(algo):
    return [c == "#" for c in algo.strip()]


def parse_img(img):
    grid = defaultdict(bool)
    for (y, row) in enumerate(img.split("\n")):
        for (x, c) in enumerate(row.strip()):
            grid[x, y] = c == "#"
    return grid


def neighbors(x, y, size=1):
    for dy in range(-size, size + 1):
        for dx in range(-size, size + 1):
            yield x + dx, y + dy


def combine_pixels(center, grid):
    res = 0
    for n in neighbors(*center):
        res <<= 1
        if grid[n]:
            res += 1
    return res


def enhance(grid, algo, padding=False):
    todo = deque(grid)
    initial = set(grid)
    new_padding = algo[-1] if padding else algo[0]
    result = defaultdict(lambda: new_padding)
    while todo:
        pixel = todo.popleft()
        if grid[pixel] != padding:
            todo.extend(n for n in neighbors(
                *pixel, size=2) if n not in initial)
        result[pixel] = algo[combine_pixels(pixel, grid)]
    return result, new_padding


def display(grid):
    x_range = [x for (x, _) in grid]
    y_range = [y for (_, y) in grid]
    x_min, x_max = min(x_range), max(x_range)
    y_min, y_max = min(y_range), max(y_range)
    img = []
    for y in range(y_min - 5, y_max + 6):
        row = []
        for x in range(x_min - 5, x_max + 6):
            row.append("#" if grid[x, y] else '.')
        img.append(row)
    return "\n".join(''.join(row) for row in img)


def part_one(algo, img, iterations=2):
    padding = False
    for _ in range(iterations):
        img, padding = enhance(img, algo, padding=padding)
    print(display(img))
    return sum(img.values())


def part_two(data: str) -> int:
    pass


if __name__ == "__main__":
    input_s = """\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""
    data = parse(read_input(day=DAY))
    # data = parse(input_s)
    print(part_one(*data, iterations=50))
