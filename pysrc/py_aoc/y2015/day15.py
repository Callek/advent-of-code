"""2015 - Day 15"""
import os
import re
from collections import Counter
from dataclasses import dataclass
from itertools import combinations_with_replacement
from math import prod
from pathlib import Path


inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/15/input.txt")
)

# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
INGREDIENT_RE = re.compile(
    r"^(?P<name>[a-zA-Z]+)\: capacity (?P<capacity>-?\d+), durability (?P<durability>-?\d+), "
    r"flavor (?P<flavor>-?\d+), texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)$"
)


@dataclass(frozen=True)
class Ingredient:
    """A descriptor of an Ingredient"""

    name: str

    # per teaspoon
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def capacity_for_teaspoons(self, teaspoons: int) -> int:
        """Capacity for number of teaspoons"""
        return teaspoons * self.capacity

    def durability_for_teaspoons(self, teaspoons: int) -> int:
        """Durability for number of teaspoons"""
        return teaspoons * self.durability

    def flavor_for_teaspoons(self, teaspoons: int) -> int:
        """Flavor for number of teaspoons"""
        return teaspoons * self.flavor

    def texture_for_teaspoons(self, teaspoons: int) -> int:
        """Texture for number of teaspoons"""
        return teaspoons * self.texture

    def all_for_teaspoons(self, teaspoons: int) -> dict[str, int]:
        """All count for this teaspoon"""
        return {
            "capacity": self.capacity_for_teaspoons(teaspoons),
            "durability": self.durability_for_teaspoons(teaspoons),
            "flavor": self.flavor_for_teaspoons(teaspoons),
            "texture": self.texture_for_teaspoons(teaspoons),
        }


def parse_ingredients(raw_text: str) -> list[Ingredient]:
    """Parse out the people"""
    ingredients = []
    for line in raw_text.splitlines():
        match = INGREDIENT_RE.match(line)
        if not match:
            raise Exception(f"Huh {line}")
        name, capacity, durability, flavor, texture, calories = match.groups()
        assert all([name, capacity, durability, flavor, texture, calories])
        ingredients.append(
            Ingredient(
                name=name,
                capacity=int(capacity),
                durability=int(durability),
                flavor=int(flavor),
                texture=int(texture),
                calories=int(calories),
            )
        )
    return ingredients


def part1(ingredients: list[Ingredient]) -> int:
    """Part 1"""
    max_prod = 0
    for combination in combinations_with_replacement(ingredients, r=100):
        teaspoons_per_ingredient = Counter(combination)
        combined_result: Counter[str] = Counter()
        for ingredient, spoons in teaspoons_per_ingredient.items():
            combined_result.update(Counter(**ingredient.all_for_teaspoons(spoons)))
        max_prod = max(
            max_prod,
            # 0 is replaced for anything negative
            prod(max(0, val) for val in combined_result.values()),
        )
    return max_prod


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text().strip()
    ingredients = parse_ingredients(raw_data)
    print(f"{__doc__} - Part 1: {part1(ingredients)}")
    # print(f"{__doc__} - Part 2: {part2(deers)}")
