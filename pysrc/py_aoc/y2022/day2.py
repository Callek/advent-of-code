"""2022 - Day 2"""
import os
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2022/days/2/input.txt")
)


def parse_hand_plays(data: str) -> list[tuple[str, str]]:
    """Parse plays in each hand

    A | X == Rock
    B | Y == Paper
    C | Z == Scissors

    A | B | C == Them
    X | Y | Z == You

    For Part 2, we learn X/Y/Z indicates win outcome.

    returns an array of hands
    """
    return [tuple(hand.split(" ")) for hand in data.strip().split("\n")]


def outcome_score(hand: tuple[str, str]) -> int:
    """Outcome Score for hand

    Lose = 0, Draw = 3, Win = 6"""
    match hand:
        case ("A", "Z") | ("B", "X") | ("C", "Y"):
            # Lose
            return 0
        case ("A", "X") | ("B", "Y") | ("C", "Z"):
            # Draw
            return 3
        case ("A", "Y") | ("B", "Z") | ("C", "X"):
            # Win
            return 6


def outcome_score_part2(hand: tuple[str, str]) -> int:
    """Outcome Score for hand - Part 2

    In this part the second letter is the outcome
    Lose (X) = 0, Draw (Y) = 3, Win (Z) = 6"""
    match hand[1]:
        case "X":
            # Lose
            return 0
        case "Y":
            # Draw
            return 3
        case "Z":
            # Win
            return 6


def played_score(hand: tuple[str, str]) -> int:
    """Score for the choice we play

    Rock = 1, Paper = 2, Scissors = 3
    """
    match hand[1]:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3


def played_score_part2(hand: tuple[str, str]) -> int:
    """Returns the score for a specific hand, part2

    Score for choice we play:
    Rock (A) = 1, Paper (B) = 2, Scissors (C) = 3
    Lose = X, Draw = Y, Z = Win
    """
    # Maps of Direction => final score
    rock = {"X": 3, "Y": 1, "Z": 2}
    paper = {"X": 1, "Y": 2, "Z": 3}
    scissors = {"X": 2, "Y": 3, "Z": 1}
    match hand[0]:
        case "A":
            return rock[hand[1]]
        case "B":
            return paper[hand[1]]
        case "C":
            return scissors[hand[1]]


def hand_score(hand: tuple[str, str], do_part2=False) -> int:
    """Calculate the score for a specific hand

    Played Score + Outcome Score
    """
    played_score_fn = played_score
    outcome_score_fn = outcome_score
    if do_part2:
        played_score_fn = played_score_part2
        outcome_score_fn = outcome_score_part2
    return played_score_fn(hand) + outcome_score_fn(hand)


def part1(hands: list[tuple[str, str]]) -> int:
    """Part 1

    Total Score for all hands
    """
    return sum(hand_score(hand) for hand in hands)


def part2(hands: list[tuple[str, str]]) -> int:
    """Part 2

    Total Score for all hands, with our move based on win/lose/draw
    """
    return sum(hand_score(hand, do_part2=True) for hand in hands)


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    hands = parse_hand_plays(raw_data)
    print(f"{__doc__} - Part 1: {part1(hands)}")
    print(f"{__doc__} - Part 2: {part2(hands)}")
