from day02 import part_one, part_two

def test_part_one():
    steps = [
        ('forward', 5),
        ('down', 5),
        ('forward', 8),
        ('up', 3),
        ('down', 8),
        ('forward', 2)
    ]
    assert part_one(steps) == 150

def test_part_two():
    steps = [
        ('forward', 5),
        ('down', 5),
        ('forward', 8),
        ('up', 3),
        ('down', 8),
        ('forward', 2)
    ]
    assert part_two(steps) == 900
