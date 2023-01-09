"""2015 - Day 1"""
import pytest

from py_aoc.y2015 import day1


@pytest.mark.parametrize(
    "instructions,expect",
    (
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ),
)
def test_part1(instructions: str, expect: int) -> None:
    """Test Part 1"""
    assert expect == day1.part1(instructions)


@pytest.mark.parametrize(
    "instructions,expect",
    (
        (")", 1),
        ("()())", 5),
    ),
)
def test_part2(instructions: str, expect: int) -> None:
    """Test Part 2"""
    assert expect == day1.part2(instructions)
