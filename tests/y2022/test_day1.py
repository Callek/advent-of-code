"""2022 - Day 1"""
from py_aoc.y2022 import day1

EXAMPLE_DATA = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_parser() -> None:
    """Test parsing"""
    expected = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]
    assert expected == day1.parse_to_list_of_list_of_ints(EXAMPLE_DATA)


def test_part1() -> None:
    """Testing Day 1 - Part 1 Example"""
    data = day1.parse_to_list_of_list_of_ints(EXAMPLE_DATA)
    assert 24000 == day1.part1(data)


def test_part2() -> None:
    """Testing Day 2 - Part 2 Example"""
    data = day1.parse_to_list_of_list_of_ints(EXAMPLE_DATA)
    assert 45000 == day1.part2(data)
