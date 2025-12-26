import logging
import sys
from functools import partial
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).parent.parent))

from aoc_utils import DaySolution, run_solutions, setup_parser

LOGFILENAME = "day03.log"
TEST_RESULT_PART1 = 357
TEST_RESULT_PART2 = None  # TODO: set expected result for part 2


def get_puzzle_test_input():
    return [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]


def test_part1():
    test_input = get_puzzle_test_input()
    assert solution_part1(test_input) == TEST_RESULT_PART1


def test_part2():
    test_input = get_puzzle_test_input()
    assert solution_part2(test_input) == TEST_RESULT_PART2


def get_puzzle_input(script_path: Path) -> list[str]:
    # TODO: implement reading from input file
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def find_max_pair(line: str) -> int:
    max_value = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            value = int(line[i] + line[j])
            if value > max_value:
                max_value = value
    logging.debug(f"Max pair in line '{line}' is\n{max_value}")
    return max_value


def solution_part1(puzzle_input: list[str]) -> int:
    logging.debug("solution_part1")
    max_pairs = []
    for line in puzzle_input:
        max_pairs.append(find_max_pair(line))
    return sum(max_pairs)


def solution_part2(puzzle_input: list[str]) -> int:
    logging.debug("solution_part2")
    # TODO: implement solution for part 2
    pass


if __name__ == "__main__":
    args = setup_parser(LOGFILENAME)
    day_solution = DaySolution(
        get_puzzle_test_input=get_puzzle_test_input,
        get_puzzle_input=partial(get_puzzle_input, Path(__file__)),
        solution_part1=solution_part1,
        solution_part2=solution_part2,
    )
    run_solutions(args, day_solution)
