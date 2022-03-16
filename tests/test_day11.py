from day11 import parse, neighbors


def test_parse():
    input_str = "123\n456\n"
    expected = {
        (0, 0): 1, (0, 1): 2, (0, 2): 3,
        (1, 0): 4, (1, 1): 5, (1, 2): 6,
    }
    grid = parse(input_str)
    assert dict(grid) == expected
    

def test_neighbors():
    expected = {
        (0, 1), (0, -1),
        (1, 0), (1, 1), (1, -1),
        (-1, 0), (-1, 1), (-1, -1)
    }
    assert set(neighbors(0, 0)) == expected
