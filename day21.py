from utils import read_input
from itertools import cycle, chain, islice

DAY = 21
START_1 = 7
START_2 = 2


def parse(data):
    pass


def player(start):
    return cycle(chain(range(start + 1, 11), range(1, start + 1)))


def det_die(n):
    return cycle(range(1, n + 1))


def take(n, iterable):
    return list(islice(iterable, n))


def run_game(pos_1=START_1, pos_2=START_2):
    turn_count = 1
    players = cycle([[player(pos_1), 0], [player(pos_2), 0]])
    die = det_die(100)
    while True:
        current_player = next(players)
        steps = sum(take(3, die))
        current_player[1] += take(steps, current_player[0])
        if current_player[1] >= 1000:
            return turn_count, players
        turn_count += 1


def part_one():
    turn_count, p = run_game()
    _, min_points = next(p)
    return turn_count * 3 * min_points


def part_two(data: str) -> int:
    pass


if __name__ == "__main__":
    print(part_one())
