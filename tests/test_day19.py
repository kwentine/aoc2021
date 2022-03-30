import pytest
import day19 as s


def test_wedge():
    a = (1, 0, 0)
    b = (0, 1, 0)
    assert s.wedge(a, b) == (0, 0, 1)


def test_rotations():
    assert len(list(s.rotations())) == 24


def test_rotate():
    r = (
        (0, -1, 0),
        (1, 0, 0),
        (0, 0, 1)
    )
    assert s.rotate(r, (1, 0, 0)) == (0, 1, 0)
