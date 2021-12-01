from typing import List

def parse(data: str) -> List[int]:
    return [int(l) for l in data.splitlines()]

def count_incr(meas: List[int]) -> int:
    if len(meas) < 2:
        return 0
    return sum(a < b for a, b in zip(meas, meas[1:]))

def count_window_incr(meas: List[int]) -> int:
    if len(meas) < 4:
        return 0
    return sum(n1 < n4 for n1, n4 in zip(meas, meas[3:]))

def part_one(data: str) -> int:
    meas = parse(data)
    return count_incr(meas)

def part_two(data: str) -> int:
    meas = parse(data)
    return count_window_incr(meas)

if __name__ == "__main__":
    with open("data/day01.txt") as f:
        data = f.read()
    print(part_one(data))
    print(part_two(data))
