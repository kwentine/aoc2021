from day04 import parse_grid, mark

def test_parse_grid():
    grid_s = "1 2\n3 4\n"
    expected = {
        1: (0, 0),
        2: (0, 1),
        3: (1, 0),
        4: (1, 1),
        'height': 2,
        'width': 2,
        'row_marked_count': [0, 0],
        'col_marked_count': [0, 0],
        'unmarked_sum': 10
    }
    assert parse_grid(grid_s) == expected

def test_mark():
    grid = {
        1: (0, 0),
        2: (0, 1),
        3: (1, 0),
        4: (1, 1),
        'height': 2,
        'width': 2,
        'row_marked_count': [0, 0],
        'col_marked_count': [0, 0],
        'unmarked_sum': 10
    }
    mark(4, grid)
    assert grid['unmarked_sum'] == 6
    assert grid['row_marked_count'] == [0, 1]
    assert grid['col_marked_count'] == [0, 1]
