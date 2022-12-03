"""
Test of generic py_aoc things
"""
from py_aoc import __version__


def test_version():
    """Test version matches"""
    assert __version__ == "0.1.0"
