from utils import read_input
from collections import deque

DAY = 10


def parse(input_s):
    return input_s.strip().splitlines()


PENALTIES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


OPEN_TO_CLOSE = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}


def check(line):
    stack = []
    for symbol in line.strip():
        if symbol in OPEN_TO_CLOSE:
            stack.append(symbol)
            continue
        if not stack:
            return PENALTIES[symbol]
        last_opened = stack.pop()
        closing = OPEN_TO_CLOSE[last_opened]
        if symbol != closing:
            return PENALTIES[symbol]
    return 0


def complete(line):
    stack = []
    for line in line:
        if line in SCORES:
            stack.pop()
        else:
            stack.append(line)
    return "".join(OPEN_TO_CLOSE[c] for c in reversed(stack))


def score(completion):
    score = 0
    for c in completion:
        score = 5 * score + SCORES[c]
    return score


def part_one(lines):
    return sum(check(line) for line in lines)


def part_two(lines):
    completions = [complete(line) for line in lines if not check(line)]
    scores = sorted(score(c) for c in completions)
    return scores[len(scores) // 2]


if __name__ == "__main__":
    data = parse(read_input(10))
    test_data = parse("""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""")
    print(part_one(data))
    print(part_two(data))
