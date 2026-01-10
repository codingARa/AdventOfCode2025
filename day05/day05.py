import logging
import sys
from functools import partial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from aoc_utils import DaySolution, run_solutions, setup_parser

LOGFILENAME = "day05.log"
TEST_RESULT_PART1 = 3
TEST_RESULT_PART2 = None
# Expected results for the actual puzzle input - received after solving the puzzle
RESULT_PART1 = None
RESULT_PART2 = None


def parse_input_lines(lines: str) -> tuple[list[str].list[str]]:
    breakline = False
    ranges = []
    orders = []
    for line in lines:
        line = line.strip()
        if line == "":
            breakline = True
        if breakline:
            orders.append(line)
        else:
            ranges.append(line)
    return ranges, orders


def get_puzzle_test_input() -> tuple[list[str], list[str]]:
    lines = [
        "3-5\n",
        "10-14\n",
        "16-20\n",
        "12-18\n",
        "\n",
        "1\n",
        "5\n",
        "8\n",
        "11\n",
        "17\n",
        "32\n",
    ]
    return parse_input_lines(lines)


def get_puzzle_input(script_path: Path) -> tuple[list[str], list[str]]:
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = file.readlines()
    return parse_input_lines(lines)


def solution_part1(puzzle_input: tuple[list[str], list[str]]) -> int:
    logging.debug("solution_part1")
    pass


def solution_part2(puzzle_input: tuple[list[str], list[str]]) -> int:
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
