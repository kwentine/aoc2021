import pytest
from day18 import (reduce_number, snail_add, rec_explode, rec_split)


@pytest.mark.parametrize('number,exploded', [
    ([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4]),
    ([7, [6, [5, [4, [3, 2]]]]], [7, [6, [5, [7, 0]]]]),
    ([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3]),
    ([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]],
     [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]),
    ([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
     [[3, [2, [8, 0]]], [9, [5, [7, 0]]]])
])
def test_rec_explode(number, exploded):
    assert rec_explode(number)[-1] == exploded


@pytest.mark.parametrize('number,expected', [
    ([[[[0, 7], 4], [15, [0, 13]]], [1, 1]], [
     [[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]])
])
def test_rec_split(number, expected):
    s, l = rec_split(number)
    assert s
    assert l == expected


@pytest.mark.parametrize('number,expected', [
    ([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]],
     [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]),

])
def test_reduce_number(number, expected):
    assert reduce_number(number) == expected


@pytest.mark.parametrize("n1,n2,expected", [
    (
        [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
        [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
        [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]
    )
])
def test_snail_add(n1, n2, expected):
    assert snail_add(n1, n2) == expected
