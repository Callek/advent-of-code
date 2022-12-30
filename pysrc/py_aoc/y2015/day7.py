"""2015 - Day 7"""
import os
import re
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
        in_signals: list[int] | None = None,
        arg: int | None = None,
    ) -> int:
        ...


def run_or(
    in_signals: list[int] | None = None,
    arg: int | None = None,
) -> int:
    """Run a bitwise or"""
    assert arg is None
    assert in_signals is not None
    assert len(in_signals) == 2
    return (in_signals[0] | in_signals[1]) & MAX


def run_and(
    in_signals: list[int] | None = None,
    arg: int | None = None,
) -> int:
    """Run a bitwise or"""
    assert arg is None
    assert in_signals is not None
    assert len(in_signals) == 2
    return (in_signals[0] & in_signals[1]) & MAX


def run_rshift(
    in_signals: list[int] | None = None,
    arg: int | None = None,
) -> int:
    """Run a rshift"""
    assert isinstance(arg, int)
    assert in_signals is not None
    assert len(in_signals) == 1
    return (in_signals[0] >> arg) & MAX


def run_lshift(
    in_signals: list[int] | None = None,
    arg: int | None = None,
) -> int:
    """Run a lshift"""
    assert isinstance(arg, int)
    assert in_signals is not None
    assert len(in_signals) == 1
    return (in_signals[0] << arg) & MAX


def run_not(
    in_signals: list[int] | None = None,
    arg: int | None = None,
) -> int:
    """Run a lshift"""
    assert arg is None
    assert in_signals is not None
    assert len(in_signals) == 1
    return (~in_signals[0]) & MAX


def run_direct(
    in_signals: list[int] | None = None,
    arg: int | None = None,
) -> int:
    """Run a direct connection"""
    assert arg is None
    assert in_signals is not None
    assert len(in_signals) == 1
    return in_signals[0] & MAX


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
    depends: list[str] | None
    method: str | None
    arg: int | None

    def __init__(
        self,
        target_wire: str,
        signal: int,
        depends: list[str] | None = None,
        method: str | None = None,
        arg: int | None = None,
    ):
        """Init"""
        self.signal = signal
        self.depends = depends
        self.method = method
        self.arg = arg
        self.target_wire = target_wire


def parse_list_of_string(data: str) -> list[str]:
    """Parsing Logic"""
    return data.strip().splitlines()


def parse_instructions(data: list[str]) -> list[Instruction]:
    """Parse instructions"""
    regex = re.compile(
        r"^(?:(?#Signal -> ...)"
        r"(?:(?P<signal>\d+))|"
        r"(?#WIRE <method> WIRE2 -> ...)"
        r"(?:(?P<dep_one>[a-z]+) (?P<method>AND|OR) (?P<dep_two>[a-z]+))|"
        r"(?#NOT WIRE -> ...)"
        r"(?:(?P<method_two>NOT) (?P<dep_only>[a-z]+))|"
        r"(?#WIRE METHOD arg -> ...)"
        r"(?:(?P<dep_only_two>[a-z]+) (?P<method_three>RSHIFT|LSHIFT) (?P<arg>\d+))|"
        r"(?#Direct from other wire -> ...)"
        r"(?:(?P<dep_only_three>[a-z]+))|"
        r"(?#-> TARGET)"
        r")(?: \-\> (?P<target>[a-z]+))$"
    )
    instructions = []
    for line in data:
        print(f"DEBUG: {line}")
        instruction_args: dict = {}
        match_obj = regex.fullmatch(line)
        assert match_obj
        match_groups = match_obj.groupdict()
        if match_groups.get("signal", None):
            instruction_args["signal"] = int(match_groups["signal"])
        else:
            instruction_args["signal"] = -1
        method = (
            match_groups["method"]
            or match_groups["method_two"]
            or match_groups["method_three"]
        )
        dep_one = (
            match_groups["dep_one"]
            or match_groups["dep_only"]
            or match_groups["dep_only_two"]
        )
        if match_groups.get("dep_two"):
            instruction_args["depends"] = [dep_one, match_groups["dep_two"]]
        elif dep_one:
            instruction_args["depends"] = [dep_one]
        elif match_groups["dep_only_three"]:
            instruction_args["depends"] = [match_groups["dep_only_three"]]
            method = "DIRECT"
        if method:
            instruction_args["method"] = method
        if match_groups.get("arg", None):
            instruction_args["arg"] = int(match_groups["arg"])
        instruction_args["target_wire"] = match_groups["target"]

        instructions.append(Instruction(**instruction_args))
    return instructions


def solve(instructions: list[Instruction], target: str | None = None) -> dict[str, int]:
    """Solve for specific wire"""
    wires: dict[str, Instruction] = {instr.target_wire: instr for instr in instructions}
    if target:
        queue = deque([wires[target]])
    else:
        queue = deque(wires.values())
    while queue:
        current_wire = queue.popleft()
        if current_wire.signal >= 0:
            # We are solved
            continue
        deps = current_wire.depends or []
        dep_wires = [wires[dep] for dep in deps]
        dep_signals = [wire.signal for wire in dep_wires]
        if current_wire.depends:
            if not all(dep_signal >= 0 for dep_signal in dep_signals):
                for next_wire in current_wire.depends:
                    if wires[next_wire] not in queue:
                        queue.append(wires[next_wire])
                queue.append(current_wire)
                continue

        assert current_wire.method
        current_wire.signal = METHODS[current_wire.method](
            in_signals=dep_signals, arg=current_wire.arg
        )

    return {wire.target_wire: wire.signal for wire in wires.values()}


def part1(instructions: list[Instruction]) -> int:
    """Part 1"""
    return solve(instructions, target="a")["a"]


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_list_of_string(raw_data)
    instructions = parse_instructions(data)
    print(f"{__doc__} - Part 1: {part1(instructions)}")
    # print(f"{__doc__} - Part 2: {part2(commands)}")
