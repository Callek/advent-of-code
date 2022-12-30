"""2015 - Day 7"""
from py_aoc.y2015 import day7

TEST_DATA = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
y -> j
1 AND x -> k
"""


def test_parsing() -> None:
    """Test Parsing"""
    data = day7.parse_list_of_string(TEST_DATA)
    commands = day7.parse_instructions(data)

    expected = [
        day7.Instruction(target_wire="x", signal=-1, arg_one="123", method="DIRECT"),
        day7.Instruction(target_wire="y", signal=-1, arg_one="456", method="DIRECT"),
        day7.Instruction(
            target_wire="d", signal=-1, method="AND", arg_one="x", arg_two="y"
        ),
        day7.Instruction(
            target_wire="e", signal=-1, method="OR", arg_one="x", arg_two="y"
        ),
        day7.Instruction(
            target_wire="f", signal=-1, method="LSHIFT", arg_one="x", arg_two="2"
        ),
        day7.Instruction(
            target_wire="g", signal=-1, method="RSHIFT", arg_one="y", arg_two="2"
        ),
        day7.Instruction(target_wire="h", signal=-1, method="NOT", arg_two="x"),
        day7.Instruction(target_wire="i", signal=-1, method="NOT", arg_two="y"),
        day7.Instruction(target_wire="j", signal=-1, method="DIRECT", arg_one="y"),
        day7.Instruction(
            target_wire="k", signal=-1, method="AND", arg_one="1", arg_two="x"
        ),
    ]
    assert expected == commands


def test_solve_for() -> None:
    """Test Solve For"""

    data = day7.parse_list_of_string(TEST_DATA)
    commands = day7.parse_instructions(data)
    assert day7.solve(commands, "f")["f"] == 492
    assert day7.solve(commands) == {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "j": 456,
        "k": 1,
        "x": 123,
        "y": 456,
    }
