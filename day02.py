from typing import List, Tuple
from utils import read_input
import functools as ft


DAY = 2


def parse(data: str) -> List[int]:
    return [(label, int(amount)) for label, amount in
            [line.split() for line in data.readlines()]]


def reducer(actions):
    def step(state, action):
        label, amount = action
        try:
            return actions[label](amount, *state)
        except KeyError:
            raise RuntimeError(f"Unknown action: {label}")
    return step


def move(initial, actions, steps):
    f = reducer(actions)
    return ft.reduce(f, steps, initial)


def part_one(steps: List[Tuple[str, int]]) -> Tuple[int, int]:
    actions = {
        'forward': lambda dx, y, x: (y, x + dx),
        'up': lambda dy, y, x: (y - dy, x),
        'down': lambda dy, y, x: (y + dy, x)
    }
    initial = (0, 0)
    depth, distance = move(initial, actions, steps)
    return depth * distance


def part_two(steps: List[Tuple[str, int]]) -> Tuple[int, int]:
    actions = {
        'forward': lambda dx, a, y, x: (a, y + a * dx, x + dx),
        'up': lambda da, a, y, x: (a - da, y, x),
        'down': lambda da, a, y, x: (a + da, y, x)
    }
    initial = (0, 0, 0)
    _, depth, distance = move(initial, actions, steps)
    return depth * distance


if __name__ == "__main__":
    parsed = parse(read_input(DAY))
    print(part_two(parsed))
