"""2015 - Day 11"""
import pytest
from py_aoc.y2015 import day11


@pytest.mark.parametrize(
    ("password", "valid"),
    (("hijklmmn", True), ("abbceffg", False), ("abbcegjk", False)),
)
def test_straight_validation(password: str, valid: bool) -> None:
    """Test straight of letters"""
    assert valid == day11.validate_consecutive_string(password)


@pytest.mark.parametrize(
    ("password", "valid"),
    (("hijklmmn", False), ("abbceffg", True), ("abbcegjk", False)),
)
def test_doubles_validation(password: str, valid: bool) -> None:
    """Check if validation of double letters works"""
    assert valid == day11.validate_doubles(password)


@pytest.mark.parametrize(
    ("password", "valid"),
    (("hijklmmn", False), ("abbcoffg", False), ("ablcegjk", False), ("abbceffg", True)),
)
def test_bad_chars(password: str, valid: bool) -> None:
    """Check if a bad character is valid"""
    assert valid == day11.validate_bad_letters(password)


@pytest.mark.parametrize(
    ("password", "next_pw"), (("abcdefgh", "abcdffaa"), ("ghijklmn", "ghjaabcc"))
)
def test_part1(password: str, next_pw: str) -> None:
    """Test Part 1"""

    assert next_pw == day11.part1(password)
