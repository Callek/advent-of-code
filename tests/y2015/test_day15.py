"""2015 - Day 15"""
from py_aoc.y2015 import day15


TEST_DATA = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""


def test_part1() -> None:
    """Test Part 1"""

    ingredients = day15.parse_ingredients(TEST_DATA)
    assert 62842880 == day15.part1(ingredients)


def test_part2() -> None:
    """Test Part 2"""

    ingredients = day15.parse_ingredients(TEST_DATA)
    assert 57600000 == day15.part2(ingredients)
