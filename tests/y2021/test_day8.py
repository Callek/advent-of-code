"""2021 - Day 8"""
from py_aoc.y2021 import day8


EXAMPLE_DATA = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


def test_display_data() -> None:
    """Test data retrieval"""
    data = day8.get_display_data(EXAMPLE_DATA)
    assert all(isinstance(display, day8.Display) for display in data)
    assert data[0].number_map == {
        0: "abdefg",
        1: "be",
        2: "abcdf",
        3: "bcdef",
        4: "bceg",
        5: "cdefg",
        6: "acdefg",
        7: "bde",
        8: "abcdefg",
        9: "bcdefg",
    }
    assert data[4].output_raw == ["cefg", "abcdefg", "bfg", "abefg"]
    assert data[6].display_raw == [
        "bcdfg",
        "dfg",
        "abcdefg",
        "cefg",
        "abdefg",
        "abcdef",
        "bcdef",
        "abcdg",
        "bcdefg",
        "fg",
    ]


def test_part1() -> None:
    """Test Part 1"""
    data = day8.get_display_data(EXAMPLE_DATA)
    assert day8.part1(data) == 26


def test_part2() -> None:
    """Test Part 2"""
    data = day8.get_display_data(EXAMPLE_DATA)
    assert day8.part2(data) == 61229
