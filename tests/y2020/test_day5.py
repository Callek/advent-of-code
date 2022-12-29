"""2020 - Day 5"""

from py_aoc.y2020 import day5
import pytest

from typing import List


@pytest.mark.parametrize(
    "seat,expected",
    (
        ("FBFBBFFRLR", 44),
        ("BFFFBBFRRR", 70),
        ("FFFBBBFRRR", 14),
        ("BBFFBBFRLL", 102),
    ),
)
def test_seat_row(seat: str, expected: int) -> None:
    """Test getting seat row"""
    assert day5.get_row(seat) == expected


@pytest.mark.parametrize(
    "seat,expected",
    (
        ("FBFBBFFRLR", 5),
        ("BFFFBBFRRR", 7),
        ("FFFBBBFRRR", 7),
        ("BBFFBBFRLL", 4),
    ),
)
def test_columns(seat: str, expected: int) -> None:
    """Test getting seat column"""
    assert day5.get_column(seat) == expected


@pytest.mark.parametrize(
    "seat,expected",
    (
        ("FBFBBFFRLR", 357),
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ),
)
def test_seat_id(seat: str, expected: int) -> None:
    """Test getting seat ID"""
    assert day5.get_seat_id(seat) == expected


@pytest.mark.parametrize(
    "seats", (["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"],)
)
def test_get_max_seat_id(seats: List[str]) -> None:
    """Test get max seat ID"""
    assert day5.get_max_seat_id(seats) == 820
