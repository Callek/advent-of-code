"""2020 - Day 3"""
import os
from functools import reduce
from typing import Dict
from typing import Tuple

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2020/days/3/input.txt")
)


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        raw_data = infile.read().splitlines()

    slopes: Dict[Tuple[int, int], int] = {  # [x][y]
        (3, 1): -1,
        (1, 1): -1,
        (5, 1): -1,
        (7, 1): -1,
        (1, 2): -1,
    }
    map_ = raw_data[:]  # [y][x]

    def find_trees_using_slope(slope: Tuple[int, int]) -> int:
        position = (0, 0)  # [x][y]
        trees = 0
        while position[1] < len(map_):
            if map_[position[1]][position[0]] == ".":
                pass  # no tree
            elif map_[position[1]][position[0]] == "#":
                trees += 1  # tree
            else:
                raise Exception("Invalid Input")

            position = (slope[0] + position[0], slope[1] + position[1])
            if position[1] < len(map_) and position[0] >= len(map_[position[1]]):
                # Wrap around
                position = (position[0] - len(map_[position[1]]), position[1])
        return trees

    for slope in slopes:
        slopes[slope] = find_trees_using_slope(slope)
        print(f"Trees hit with slope {slope}: {slopes[slope]}")

    print(
        f"Multiplication of all trees on checked slopes: {reduce(lambda x, y: x*y, slopes.values())}"
    )
