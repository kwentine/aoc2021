from utils import read_input
from collections import Counter

DAY = 6


def parse(input_s):
    return [int(i) for i in input_s.strip().split(',')]


def next_day(counts):
    n_zero = counts[0]
    for i in range(8):
        counts[i] = counts[i + 1]
    counts[8] = n_zero
    counts[6] += n_zero


def live_for(fish, days=80):
    counts = Counter(fish)
    for i in range(days):
        next_day(counts)
    return sum(counts.values())
    
    
def part_one(fish):
    return live_for(fish, days=80)


def part_two(fish):
    return live_for(fish, days=256)

if __name__ == "__main__":
    fish = parse(read_input(DAY))
    print(part_two(fish))
