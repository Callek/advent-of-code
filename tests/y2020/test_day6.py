"""2020 - Day 6"""
from py_aoc.y2020 import day6
import pytest

TEST_DATA1 = """abcx
abcy
abcz
"""

TEST_DATA2 = """abc

a
b
c

ab
ac

a
a
a
a

b
"""


@pytest.mark.parametrize("test,answer", ((TEST_DATA1, 6), (TEST_DATA2, 11)))
def test_day6_sets(test, answer) -> None:
    """Test sets"""
    sets = day6.create_sets(test)
    assert day6.sum_yes_answers(sets) == answer


@pytest.mark.parametrize("test,answer", ((TEST_DATA1, 3), (TEST_DATA2, 6)))
def test_day6_all_yes(test, answer) -> None:
    """Test all yes"""
    sets = day6.create_sets_all_yes(test)
    assert day6.sum_yes_answers(sets) == answer
