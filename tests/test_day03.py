from day03 import parse, accumulate, gamma_i, part_two, filter_until_single


def test_parse():
    data = "001\n010\n100\n"
    assert parse(data) == [[0, 0, 1], [0, 1, 0], [1, 0 , 0]]


def test_accumulate():
    numbers = [[0, 0, 1], [0, 1, 0], [1, 0 , 0]]
    assert accumulate(numbers) == [1, 1, 1]


def test_gamma():
    numbers = [[0, 0, 1], [1, 1, 0], [1, 0 , 0]]
    assert gamma_i(numbers, 0) == 1
    assert gamma_i(numbers, 1) == 0

def test_filter_until_single():
    data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    numbers = parse(data)
    assert filter_until_single(numbers, gamma_i) == 23

def test_part_two():
    data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    numbers = parse(data)
    assert part_two(numbers) == 230

