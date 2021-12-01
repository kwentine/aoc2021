from day01 import count_incr, count_window_incr

def test_count_incr():
    mes = [0, 1, 2]
    assert count_incr(mes) == 2

def test_window_incr():
    mes = [0, 1, 2, 3]
    assert count_window_incr(mes) == 1
    
