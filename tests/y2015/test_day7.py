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
"""


def test_parsing() -> None:
    """Test Parsing"""
    data = day7.parse_list_of_string(TEST_DATA)
    commands = day7.parse_instructions(data)

    expected = [
        day7.Instruction(target_wire="x", signal=123),
        day7.Instruction(target_wire="y", signal=456),
        day7.Instruction(target_wire="d", signal=-1, method="AND", depends=["x", "y"]),
        day7.Instruction(target_wire="e", signal=-1, method="OR", depends=["x", "y"]),
        day7.Instruction(
            target_wire="f", signal=-1, method="LSHIFT", depends=["x"], arg=2
        ),
        day7.Instruction(
            target_wire="g", signal=-1, method="RSHIFT", depends=["y"], arg=2
        ),
        day7.Instruction(target_wire="h", signal=-1, method="NOT", depends=["x"]),
        day7.Instruction(target_wire="i", signal=-1, method="NOT", depends=["y"]),
        day7.Instruction(target_wire="j", signal=-1, method="DIRECT", depends=["y"]),
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
        "x": 123,
        "y": 456,
    }
