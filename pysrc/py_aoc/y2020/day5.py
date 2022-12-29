"""2020 - Day 5"""
# pylint: disable=broad-except

import os
from typing import List

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2020/days/5/input.txt")
)


TOTAL_ROWS = 128  # 0-based
TOTAL_COLUMNS = 8


def bisect(bisect_range: range, rules: List[str], low_char: str, high_char: str) -> int:
    """Bisect a range"""
    for bisection in rules:
        half = len(bisect_range) // 2
        if bisection == low_char:
            bisect_range = bisect_range[:half]
        elif bisection == high_char:
            bisect_range = bisect_range[half:]
        else:
            raise Exception(f"Unexpected Input {bisection}")
    assert len(bisect_range) == 1
    return bisect_range[0]


def get_row(seat: str) -> int:
    """Get my row, based on seat"""
    rows = range(TOTAL_ROWS)
    return bisect(
        bisect_range=rows,
        rules=list(seat.upper())[:7],
        low_char="F",
        high_char="B",
    )


def get_column(seat: str) -> int:
    """Get column of seat"""
    columns = range(TOTAL_COLUMNS)
    return bisect(
        bisect_range=columns,
        rules=list(seat.upper())[7:],
        low_char="L",
        high_char="R",
    )


cache = {}


def get_seat_id(seat: str) -> int:
    """Derive a seat ID"""
    row = get_row(seat)
    column = get_column(seat)
    seat_id = (row * 8) + column
    cache[seat_id] = True
    return seat_id


def get_max_seat_id(seats: List[str]) -> int:
    """Max seat ID from IDs"""
    return max(get_seat_id(seat) for seat in seats)


def main() -> None:
    """Main"""
    with open(inputfile) as infile:
        raw_data = infile.read()

    seats = raw_data.strip().split("\n")
    max_seat = get_max_seat_id(seats)
    print(f"max seat id {max_seat} out of {len(seats)} seats")

    my_seat = -1
    for seat_id in range(max_seat):
        if cache.get(seat_id):
            # Someone is sitting here
            continue
        if cache.get(seat_id - 1) and cache.get(seat_id + 1):
            my_seat = seat_id
            break
    print(f"My Seat is {my_seat}, hope its an aisle.")
