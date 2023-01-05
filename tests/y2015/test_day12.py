"""2015 - Day 12"""
import pytest
from py_aoc.y2015 import day12


@pytest.mark.parametrize(
    ("json_str", "count"),
    (
        ("[1,2,3]", 6),
        ('{"a":2,"b":4}', 6),
        ("[[[3]]]", 3),
        ('{"a":{"b":4},"c":-1}', 3),
        ('{"a":[-1,1]}', 0),
        ('[-1,{"a":1}]', 0),
        ("[]", 0),
        ("{}", 0),
    ),
)
def test_part1(json_str: str, count: int) -> None:
    """Test Part 1"""

    assert count == day12.part1(json_str)


@pytest.mark.parametrize(
    ("json_str", "count"),
    (
        ("[1,2,3]", 6),
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5]', 6),
    ),
)
def test_part2(json_str: str, count: int) -> None:
    """Test Part 2"""

    assert count == day12.part2(json_str)
