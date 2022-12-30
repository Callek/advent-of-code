"""2015 - Day 6"""
from py_aoc.y2015 import day6

TEST_DATA = """turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
"""


def test_parsing() -> None:
    """Test Parsing"""
    data = day6.parse_list_of_string(TEST_DATA)
    commands = day6.parse_commands(data)

    expected = [
        day6.COMMAND(day6.turn_on, day6.COORD(0, 0), day6.COORD(999, 999)),
        day6.COMMAND(day6.toggle, day6.COORD(0, 0), day6.COORD(999, 0)),
        day6.COMMAND(day6.turn_off, day6.COORD(499, 499), day6.COORD(500, 500)),
    ]
    assert expected == commands


def test_part1() -> None:
    """Test Part 1"""

    data = day6.parse_list_of_string(TEST_DATA)
    commands = day6.parse_commands(data)
    assert 998996 == day6.part1(commands)


def test_part2() -> None:
    """Test Part 2"""

    data = day6.parse_list_of_string(TEST_DATA)
    commands = day6.parse_commands(data)
    assert 1001996 == day6.part2(commands)
