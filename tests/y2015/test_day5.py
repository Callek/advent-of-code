"""2015 - Day 5"""
import pytest

from py_aoc.y2015 import day5


@pytest.mark.parametrize(
    "string,expect",
    (
        ("dvszwmarrgswjxmb", False),
        ("aaa", True),
        ("aei", True),
        ("xazegov", True),
        ("aeiouaeiouaeiou", True),
    ),
)
def test_vowel(string: str, expect: int) -> None:
    """has three vowel"""
    assert expect == day5.has_three_vowels(string)


@pytest.mark.parametrize(
    "string,expect",
    (
        ("jchzalrnumimnmhp", False),
        ("xx", True),
        ("abcdde", True),
        ("aabbccdd", True),
    ),
)
def test_double_letter(string: str, expect: int) -> None:
    """has double letters"""
    assert expect == day5.has_double_letter(string)


@pytest.mark.parametrize(
    "string,expect",
    (
        ("haegwjzuvuyypxyu", False),
        ("jchzalrnumimnmhp", True),
        ("ugknbfddgicrmopn", True),
        ("aabbccdd", False),
    ),
)
def test_naughty(string: str, expect: int) -> None:
    """has naught letters"""
    assert expect == day5.no_naughty_string(string)


@pytest.mark.parametrize(
    "string,expect",
    (
        ("xyxy", True),
        ("aabcdefgaa", True),
        ("aaa", False),
    ),
)
def test_paired(string: str, expect: int) -> None:
    """has paired letter"""
    assert expect == day5.has_paired_letters(string)


@pytest.mark.parametrize(
    "string,expect",
    (
        ("xyx", True),
        ("abcdefeghi", True),
        ("aaa", True),
        ("abcdefg", False),
        ("abcdaefg", False),
    ),
)
def test_repeat(string: str, expect: int) -> None:
    """has repeat letter"""
    assert expect == day5.has_repeat_letter(string)


def test_part1() -> None:
    """Part 1"""
    assert 2 == day5.part1(
        [
            "ugknbfddgicrmopn",
            "aaa",
            "jchzalrnumimnmhp",
            "haegwjzuvuyypxyu",
            "dvszwmarrgswjxmb",
        ]
    )


def test_part2() -> None:
    """Part 2"""
    assert 2 == day5.part2(
        [
            "qjhvhtzxzqqjkmpb",
            "xxyxx",
            "uurcxstgmygtbstg",
            "ieodomkazucvgmuy",
        ]
    )
