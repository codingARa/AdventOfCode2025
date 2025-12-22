import logging
import sys
from functools import partial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from aoc_utils import DaySolution, get_puzzle_input, run_solutions, setup_parser

LOGFILENAME = "day02.log"


def get_puzzle_test_input():
    return [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]


def test_part1():
    test_input = get_puzzle_test_input()
    assert solution_part1(test_input) == 1227775554


def test_part2():
    test_input = get_puzzle_test_input()
    assert solution_part2(test_input) == 0


def solution_part1(puzzle_input: list[str]) -> int:
    logging.debug("solution_part1")
    return 1


def solution_part2(puzzle_input: list[str]) -> int:
    logging.debug("solution_part2")
    return 1


if __name__ == "__main__":
    args = setup_parser(LOGFILENAME)
    day_solution = DaySolution(
        get_test_puzzle_input=get_puzzle_test_input,
        get_puzzle_input=partial(get_puzzle_input, Path(__file__)),
        solution_part1=solution_part1,
        solution_part2=solution_part2,
    )
    run_solutions(args, day_solution)
