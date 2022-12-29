"""2020 - Day 8"""
from py_aoc.y2020 import day8

TEST_DATA = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def test_day8() -> None:
    """Test Part 1"""
    acc = day8.part1(TEST_DATA)
    assert acc == 5


def test_day8_part2() -> None:
    """Test Part 2"""
    acc = day8.part2(TEST_DATA)
    assert acc == 8
