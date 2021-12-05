from utils import read_input
from tqdm import tqdm
import re

DAY = 5


def parse(input_s):
    pattern = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
    segments = []
    for line in input_s.splitlines():
        m = pattern.match(line)
        if m is not None:
            segments.append(tuple(int(i) for i in m.group(1, 2, 3, 4)))
    return segments


def v_or_h(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2


def on_segment(x, y, x1, y1, x2, y2):
    """Is (x, y) on the segment delimited by (x1, y1) and (x2, y2) ?"""
    return ((min(x1, x2) <= x <= max(x1, x2)) and
            (min(y1, y2) <= y <= max(y1, y2)) and not
            (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1))


def count_intersects(segments):
    x_max = max(max(x1, x2) for (x1, y1, x2, y2) in segments)
    y_max = max(max(y1, y2) for (x1, y1, x2, y2) in segments)
    count = 0
    for x in tqdm(range(x_max + 1)):
        for y in range(y_max + 1):
            candidate = False
            for (x1, y1, x2, y2) in segments:
                if on_segment(x, y, x1, y1, x2, y2):
                    if candidate:
                        count += 1
                        break
                    else:
                        candidate = True
    return count


def part_one(segments):
    return count_intersects([s for s in segments if v_or_h(*s)])


def part_two(segments):
    return count_intersects(segments)


if __name__ == "__main__":
    segments = parse(read_input(DAY))
    print(part_two(segments))
