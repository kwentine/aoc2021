from utils import read_input
from collections import defaultdict, Counter


DAY = 14


def parse(input_str):
    polymer, insertions = input_str.split("\n\n")
    insertions = {
        (s[0], s[1]): s[-1] for s in insertions.splitlines()
    }
    return polymer, insertions


def step(pair_counts, insertions):
    new_counts = defaultdict(int)
    for (a, b), count in pair_counts.items():
        insert = insertions.get((a, b))
        if not insert:
            new_counts[(a, b)] += count
        else:
            new_counts[(a, insert)] += count
            new_counts[(insert, b)] += count
    return new_counts


def count_chars(pair_counts):
    char_counts = defaultdict(int)
    for (a, b), count in pair_counts.items():
        char_counts[a] += count
    return sorted((count, char) for char, count in char_counts.items())


def evolve(polymer, insertions, steps):
    polymer += "\x00"
    pair_counts = defaultdict(int)
    for i in range(len(polymer) - 1):
        pair_counts[polymer[i], polymer[i+1]] += 1
    for _ in range(steps):
        pair_counts = step(pair_counts, insertions)
    return pair_counts


def part_one(polymer, insertions):
    pair_counts = evolve(polymer, insertions, steps=10)
    char_counts = count_chars(pair_counts)
    return char_counts[-1][0] - char_counts[0][0]


def part_two(polymer, insertions):
    pair_counts = evolve(polymer, insertions, steps=40)
    char_counts = count_chars(pair_counts)
    return char_counts[-1][0] - char_counts[0][0]


if __name__ == "__main__":
    polymer, insertions = parse(read_input(day=DAY))
    print(part_one(polymer, insertions))
