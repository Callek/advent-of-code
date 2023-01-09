"""2015 - Day 4"""
import pytest

from py_aoc.y2015 import day4


@pytest.mark.parametrize(
    "directions,expect",
    (("abcdef", 609043), ("pqrstuv", 1048970)),
)
def test_part1(directions: str, expect: int) -> None:
    """Test Part 1"""
    assert expect == day4.part1(directions)


@pytest.mark.parametrize(
    "directions,expect",
    (("abcdef", 6742839), ("pqrstuv", 5714438)),
)
def test_part2(directions: str, expect: int) -> None:
    """Test Part 2"""
    assert expect == day4.part2(directions)
