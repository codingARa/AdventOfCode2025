import logging
import sys
from functools import partial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from aoc_utils import DaySolution, run_solutions, setup_parser

LOGFILENAME = "day04.log"
# TODO-ARA: Set test results, when known
TEST_RESULT_PART1 = 13
TEST_RESULT_PART2 = -1


def get_puzzle_test_input():
    return [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]


def get_puzzle_input(script_path: Path) -> list[str]:
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def solution_part1(puzzle_input: list[str]) -> int:
    logging.debug("solution_part1")
    pass


def solution_part2(puzzle_input: list[str]) -> int:
    logging.debug("solution_part2")
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
