"""2022 - Day 2"""
from py_aoc.y2022 import day2

EXAMPLE_DATA = """A Y
B X
C Z
"""


def test_parser() -> None:
    """Test parsing"""
    expected = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z"),
    ]
    assert expected == day2.parse_hand_plays(EXAMPLE_DATA)


def test_part1() -> None:
    """Test Part 1"""
    hands = day2.parse_hand_plays(EXAMPLE_DATA)
    assert 15 == day2.part1(hands)


def test_part2() -> None:
    """Test Part 2"""
    hands = day2.parse_hand_plays(EXAMPLE_DATA)
    assert 12 == day2.part2(hands)
