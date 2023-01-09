"""2015 - Day 15"""
from py_aoc.y2015 import day16


TEST_DATA = """Sue 210: perfumes: 4, cars: 8, samoyeds: 3
Sue 211: perfumes: 2, cars: 8, trees: 9
Sue 212: trees: 7, perfumes: 2, akitas: 5
Sue 213: children: 3, goldfish: 5, vizslas: 0
Sue 214: akitas: 6, goldfish: 0, children: 0
Sue 215: trees: 8, akitas: 3, goldfish: 1
"""


def test_part1() -> None:
    """Test Part 1"""

    aunts = day16.parse_aunt(TEST_DATA)
    assert "213" == day16.part1(aunts)
