from utils import read_input

DAY = 13

def parse(data):
    dots, instructions = data.split('\n\n')
    grid = parse_dots(dots)
    folds = parse_folds(instructions)
    return grid, folds


def parse_dots(dots_str):
    grid = set()
    for line in dots_str.splitlines():
        x, y = line.split(',')
        grid.add((int(x), int(y)))
    return grid

def fold(point, along):
    x, y = point
    a, b = along
    dx = x - a if x > a > 0 else 0
    dy = y - b if y > b > 0 else 0
    return (x - 2 * dx, y - 2 * dy)

def parse_folds(folds_str):
    folds = []
    for line in folds_str.splitlines():
        inst, coord = line.split("=")
        coord = int(coord)
        folds.append((coord, 0) if inst[-1] == "x" else (0, coord))
    return folds


def part_one(grid, folds):
    along = folds[0]
    return len(set(fold(point, along) for point in grid))
     
    
def part_two(grid, folds):
    for along in folds:
        grid = set(fold(point, along) for point in grid)
    w = max(p[0] for p in grid) + 1
    h = max(p[1] for p in grid) + 1
    img = [[' '] * w for _ in range(h)]
    for (x, y) in grid:
        img[y][x] = '#'
    return "\n".join(''.join(l) for l in img)

if __name__ == "__main__":
    grid, folds = parse(read_input(day=DAY))
    print(part_two(grid, folds))

