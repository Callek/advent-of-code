"""2022 - Day 3"""
import pytest
from py_aoc.y2022 import day3

EXAMPLE_DATA = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_parser() -> None:
    """Test parsing"""
    expected = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    assert expected == day3.parse_rucksacks(EXAMPLE_DATA)


@pytest.mark.parametrize(
    "item,expect", (("A", 27), ("D", 30), ("Y", 51), ("a", 1), ("j", 10))
)
def test_item_prio(item: str, expect: int) -> None:
    """Test priority values"""
    assert expect == day3.get_item_prio(item)


def test_part1() -> None:
    """Test part1"""
    sacks = day3.parse_rucksacks(EXAMPLE_DATA)
    assert 157 == day3.part1(sacks)


def test_part2() -> None:
    """Test part1"""
    sacks = day3.parse_rucksacks(EXAMPLE_DATA)
    assert 70 == day3.part2(sacks)
