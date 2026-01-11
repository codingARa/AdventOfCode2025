import logging
import sys
from functools import partial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from aoc_utils import DaySolution, run_solutions, setup_parser

LOGFILENAME = "day06.log"
TEST_RESULT_PART1 = 4277556
TEST_RESULT_PART2 = None
# Expected results for the actual puzzle input - received after solving the puzzle
RESULT_PART1 = None
RESULT_PART2 = None


def parse_input_lines(lines: list[str]):
    # TODO-ARA
    pass


def get_puzzle_test_input():
    lines = [
        "123 328  51 64 \n",
        " 45 64  387 23 \n",
        "  6 98  215 314\n",
        "*   +   *   + \n",
    ]
    return parse_input_lines(lines)


def get_puzzle_input(script_path: Path):
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = file.readlines()
    return parse_input_lines(lines)


def solution_part1(puzzle_input) -> int:
    logging.debug("solution_part1")
    pass


def solution_part2(puzzle_input) -> int:
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
