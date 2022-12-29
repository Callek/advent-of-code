"""2015 - Day 1"""
import pytest

from py_aoc.y2015 import day2


@pytest.mark.parametrize(
    "box,expect",
    (
        (day2.BOX(2, 3, 4), 58),
        (day2.BOX(1, 1, 10), 43),
    ),
)
def test_paper_for_present(box: day2.BOX, expect: int) -> None:
    """Test single boxes"""
    assert expect == day2.paper_for_present(box)


def test_part1() -> None:
    """Test Part 1"""
    raw_data = "2x3x4\n1x1x10\n"
    boxes = day2.parse_box_dimensions(raw_data)
    assert 101 == day2.part1(boxes)
