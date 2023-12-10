"""2015 - Day 3"""
import pytest

from py_aoc.y2015 import day3


@pytest.mark.parametrize(
    "directions,expect",
    ((">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)),
)
def test_part1(directions: str, expect: int) -> None:
    """Test Part 1"""
    assert expect == day3.part1(directions)


@pytest.mark.parametrize(
    "directions,expect",
    (("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)),
)
def test_part2(directions: str, expect: int) -> None:
    """Test Part 2"""
    assert expect == day3.part2(directions)
