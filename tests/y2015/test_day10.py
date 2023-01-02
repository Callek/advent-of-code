"""2015 - Day 9"""
from py_aoc.y2015 import day10

TEST_DATA = "1"


def test_part1() -> None:
    """Test Part 1"""

    assert "312211" == day10.do_look_and_say(TEST_DATA, iterations=5)
    assert 82350 == day10.part1(TEST_DATA)
