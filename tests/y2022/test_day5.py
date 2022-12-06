"""2022 - Day 5"""
from py_aoc.y2022 import day5

EXAMPLE_DATA = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def test_parse() -> None:
    """day 5 parse test"""
    expect_stack_start = ["NZ", "DCM", "P"]
    expect_directions = [
        (1, 2, 1),
        (3, 1, 3),
        (2, 2, 1),
        (1, 1, 2),
    ]
    stack_start, stack_directions = day5.parse_data(EXAMPLE_DATA)
    assert stack_start == expect_stack_start
    assert stack_directions == expect_directions


def test_part1() -> None:
    """Test part1"""
    start, directions = day5.parse_data(EXAMPLE_DATA)
    assert "CMZ" == day5.part1(start, directions)
