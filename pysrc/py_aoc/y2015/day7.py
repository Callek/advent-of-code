"""2015 - Day 7"""
import os
import re
from copy import copy
from dataclasses import dataclass
from collections import deque
from pathlib import Path
from typing import Protocol

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/7/input.txt")
)


MAX = 0xFFFF


class Method(Protocol):
    """An arbitrary method"""

    # pylint: disable=too-few-public-methods
    def __call__(
        self,
        arg_left: int | None = None,
        arg_right: int | None = None,
    ) -> int:
        ...


def run_or(
    arg_left: int | None = None,
    arg_right: int | None = None,
) -> int:
    """Run a bitwise or"""
    assert arg_left is not None
    assert arg_right is not None
    return (arg_left | arg_right) & MAX


def run_and(
    arg_left: int | None = None,
    arg_right: int | None = None,
) -> int:
    """Run a bitwise and"""
    assert arg_left is not None
    assert arg_right is not None
    return (arg_left & arg_right) & MAX


def run_rshift(
    arg_left: int | None = None,
    arg_right: int | None = None,
) -> int:
    """Run a rshift"""
    assert arg_left is not None
    assert arg_right is not None
    return (arg_left >> arg_right) & MAX


def run_lshift(
    arg_left: int | None = None,
    arg_right: int | None = None,
) -> int:
    """Run a lshift"""
    assert arg_left is not None
    assert arg_right is not None
    return (arg_left << arg_right) & MAX


def run_not(
    arg_left: int | None = None,
    arg_right: int | None = None,
) -> int:
    """Run a lshift"""
    assert arg_left is None
    assert arg_right is not None
    return (~arg_right) & MAX


def run_direct(
    arg_left: int | None = None,
    arg_right: int | None = None,
) -> int:
    """Run a direct connection"""
    assert arg_left is not None
    assert arg_right is None
    return (arg_left) & MAX


METHODS: dict[str, Method] = {
    "AND": run_and,
    "OR": run_or,
    "LSHIFT": run_lshift,
    "RSHIFT": run_rshift,
    "NOT": run_not,
    "DIRECT": run_direct,
}


@dataclass
class Instruction:
    """A single instruction"""

    # pylint: disable=too-few-public-methods

    target_wire: str
    signal: int
    arg_one: str | None
    arg_two: str | None
    method: str | None

    def __init__(
        self,
        target_wire: str,
        signal: int,
        method: str,
        arg_one: str | None = None,
        arg_two: str | None = None,
    ):
        """Init"""
        self.signal = signal
        self.method = method
        self.arg_one = arg_one
        self.arg_two = arg_two
        self.target_wire = target_wire


def parse_list_of_string(data: str) -> list[str]:
    """Parsing Logic"""
    return data.strip().splitlines()


def parse_instructions(data: list[str]) -> list[Instruction]:
    """Parse instructions"""
    regex = re.compile(
        r"^(?:(?#Signal -> ... || )"
        r"(?#Direct from other wire -> ...)"
        r"(?:(?P<arg_left_one>(?:\d+|[a-z]+)))|"
        r"(?#WIRE <method> WIRE2 -> ...)"
        r"(?#WIRE METHOD arg -> ...)"
        r"(?:(?P<arg_left_two>(?:\d+|[a-z]+)) (?P<method_one>AND|OR|RSHIFT|LSHIFT)"
        r" (?P<arg_right_one>(?:\d+|[a-z]+)))|"
        r"(?#NOT WIRE -> ...)"
        r"(?:(?P<method_two>NOT) (?P<arg_right_two>(?:\d+|[a-z]+)))|"
        r"(?#-> TARGET)"
        r")(?: \-\> (?P<target>[a-z]+))$"
    )
    instructions = []
    for line in data:
        instruction_args: dict = {}
        match_obj = regex.fullmatch(line)
        assert match_obj
        match_groups = match_obj.groupdict()

        instruction_args["target_wire"] = match_groups["target"]
        instruction_args["signal"] = -1

        method = match_groups["method_one"] or match_groups["method_two"] or "DIRECT"
        instruction_args["method"] = method

        arg_one = match_groups["arg_left_one"] or match_groups["arg_left_two"]
        instruction_args["arg_one"] = arg_one
        arg_two = match_groups["arg_right_one"] or match_groups["arg_right_two"]
        instruction_args["arg_two"] = arg_two

        instructions.append(Instruction(**instruction_args))
    return instructions


def get_arg(wires: dict[str, Instruction], arg: str | None) -> tuple[int | None, bool]:
    """Gets an arg"""
    ret = None
    requeue = False
    if arg:
        if arg.isdigit():
            ret = int(arg)
            return ret, requeue
        wire = wires.get(arg)
        if wire and wire.signal >= 0:
            ret = wire.signal
        else:
            requeue = True
    return ret, requeue


def solve(
    instructions: list[Instruction],
    target: str | None = None,
    override: dict[str, Instruction] | None = None,
) -> dict[str, int]:
    """Solve for specific wire"""
    wires: dict[str, Instruction] = {
        instr.target_wire: copy(instr) for instr in instructions
    }
    if override:
        wires.update(override)
    queue = deque(wires.values())
    if target:
        queue = deque([wires[target]])
    while queue:
        current_wire = queue.popleft()
        if current_wire.signal >= 0:
            # We are solved
            continue
        arg_left_signal: int | None = None
        requeue_left: bool = False
        arg_left_signal, requeue_left = get_arg(wires, current_wire.arg_one)
        if (
            requeue_left
            and current_wire.arg_one
            and wires.get(current_wire.arg_one) not in queue
        ):
            queue.append(wires[current_wire.arg_one])

        arg_right_signal: int | None = None
        requeue_right: bool = False
        arg_right_signal, requeue_right = get_arg(wires, current_wire.arg_two)
        if (
            requeue_right
            and current_wire.arg_two
            and wires.get(current_wire.arg_two) not in queue
        ):
            queue.append(wires[current_wire.arg_two])

        if requeue_left or requeue_right:
            queue.append(current_wire)
            continue

        assert current_wire.method
        current_wire.signal = METHODS[current_wire.method](
            arg_left=arg_left_signal, arg_right=arg_right_signal
        )

    return {wire.target_wire: wire.signal for wire in wires.values()}


def part1(instructions: list[Instruction]) -> int:
    """Part 1"""
    return solve(instructions, target="a")["a"]


def part2(instructions: list[Instruction]) -> int:
    """Part 2"""
    first_pass_a = solve(instructions, target="a")["a"]
    override = {"b": Instruction(target_wire="b", signal=first_pass_a, method="DIRECT")}
    return solve(instructions, target="a", override=override)["a"]


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_list_of_string(raw_data)
    instructions = parse_instructions(data)
    print(f"{__doc__} - Part 1: {part1(instructions)}")
    print(f"{__doc__} - Part 2: {part2(instructions)}")
