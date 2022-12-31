"""2015 - Day 9"""
from py_aoc.y2015 import day9

TEST_DATA = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""


def test_part1() -> None:
    """Test Part 1"""

    data = day9.parse_list_of_string(TEST_DATA)
    cities = day9.get_cities(data)
    assert 605 == day9.part1(cities)
