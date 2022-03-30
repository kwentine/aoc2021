from utils import read_input
import collections
import itertools as it


DAY = 19


def parse(data):
    probes = []
    for group in data.split("\n\n"):
        beacons = []
        for beacon in group.splitlines()[1:]:
            x, y, z = beacon.split(',')
            beacons.append((int(x), int(y), int(z)))
        probes.append(beacons)
    return probes


def wedge(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return (
        y1 * z2 - z1 * y2,
        -(x1 * z2 - z1 * x2),
        x1 * y2 - y1 * x2
    )


def rotations():
    base = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1)
    ]
    for (a, b) in it.permutations(base, 2):
        c = wedge(a, b)
        if c != (0, 0, 0):
            yield tuple(zip(a, b, wedge(a, b)))


def rotate(r, v):
    """Apply rotation r to vector v"""
    return tuple(sum(a * b for (a, b) in zip(v, row)) for row in r)


def move(scan, dx, dy, dz):
    return [(x + dx, y + dy, z + dz) for (x, y, z) in scan]


def join(base, scan, transforms):

    for r in transforms:
        rotated = [rotate(r, v) for v in scan]
        [(diff, count)] = collections.Counter((x2 - x1, y2 - y1, z2 - z1)
                                              for (x1, y1, z1) in rotated
                                              for (x2, y2, z2) in base).most_common(1)
        if count >= 12:
            return diff, move(rotated, *diff)

    return None, None


def aggregate(scans):
    scanners = [(0, 0, 0)]
    transforms = list(rotations())
    base = set(scans[0])
    todo = collections.deque(scans[1:])
    while todo:
        scan = todo.popleft()
        diff, moved = join(base, scan, transforms)
        if not diff:
            todo.append(scan)
            continue
        base |= set(moved)
        scanners.append(diff)
    return scanners, base


def part_one(data: str) -> int:
    scanners, base = aggregate(data)
    return len(base)


def part_two(data: str) -> int:
    scanners, base = aggregate(data)
    print(scanners)
    return max(abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) for (x1, y1, z1) in scanners
               for (x2, y2, z2) in scanners)


if __name__ == "__main__":
    scans = parse(read_input(day=DAY))
    print(part_two(scans))
