"""2022 - Day 4"""
from py_aoc.y2022 import day4

EXAMPLE_DATA = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_part1() -> None:
    """Test part1"""
    assignments = day4.parse_assignments(EXAMPLE_DATA)
    assert 2 == day4.part1(assignments)
