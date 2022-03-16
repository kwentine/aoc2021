from utils import read_input
from collections import defaultdict

DAY = 12
START = 'start'
END = 'end'


def parse(data):
    graph = defaultdict(set)
    for line in data.splitlines():
        src, dest = line.split('-')
        graph[src].add(dest)
        graph[dest].add(src)
    return graph


def extend(path, graph):
    if not path:
        yield [START]
    else:
        for neighbor in graph[path[-1]]:
            if neighbor.isupper() or neighbor not in path:
                yield path + [neighbor]


def extend_relaxed(path, allow_twice, graph):
    if not path:
        yield [START], True
    else:
        for neighbor in graph[path[-1]]:
            if neighbor == START:
                continue
            if neighbor.isupper() or neighbor not in path:
                yield path + [neighbor], allow_twice
            elif allow_twice:
                yield path + [neighbor], False


def part_one(graph):
    todo = [[]]
    paths = []
    while todo:
        path = todo.pop()
        for next_path in extend(path, graph):
            if next_path[-1] == END:
                paths.append(next_path)
            else:
                todo.append(next_path)
    return len(paths)


def part_two(graph):
    todo = [([], True)]
    paths = []
    while todo:
        path, allow_twice = todo.pop()
        for (next_path, next_allow_twice) in extend_relaxed(path, allow_twice, graph):
            if next_path[-1] == END:
                paths.append(next_path)
            else:
                todo.append((next_path, next_allow_twice))
    return len(paths)


if __name__ == "__main__":
    data = parse(read_input(day=DAY))
    print(part_two(data))
