"""2020 - Day 9"""
from py_aoc.y2020 import day9

TEST_DATA = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


def test_day9() -> None:
    """Test Part 1"""
    acc = day9.part1(TEST_DATA, preamble=5)
    assert int(acc) == 127


def test_day9_part2() -> None:
    """Test Part 2"""
    target = day9.part1(TEST_DATA, preamble=5)
    acc = day9.part2(TEST_DATA, target)
    assert acc == 62
