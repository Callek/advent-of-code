"""2015 - Day 8"""
from py_aoc.y2015 import day8

TEST_DATA = r"""""
"abc"
"aaa\"aaa"
"\x27"
"""


def test_part1() -> None:
    """Test Part 1"""

    data = day8.parse_list_of_string(TEST_DATA)
    assert 12 == day8.part1(data)


def test_part2() -> None:
    """Test Part 2"""

    data = day8.parse_list_of_string(TEST_DATA)
    assert 19 == day8.part2(data)
