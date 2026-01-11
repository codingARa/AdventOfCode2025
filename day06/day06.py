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
RESULT_PART1 = 5227286044585
RESULT_PART2 = None


def parse_input_lines(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    number_lists = []
    operator_list = []
    for line in lines:
        split_line = line.split()
        try:
            number_lists.append([int(num) for num in split_line])
        except ValueError:
            operator_list = split_line
    return number_lists, operator_list


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


def get_total_sum(puzzle_input) -> int:
    total = 0
    number_lists, operator_list = puzzle_input
    number_list_count = len(number_lists)

    for index, operator in enumerate(operator_list):
        match operator:
            case "*":
                logging.debug("Multiplication")
                column_total = 1
                for n in range(number_list_count):
                    column_total *= number_lists[n][index]
                total += column_total
            case "+":
                logging.debug("Addition")
                column_total = 0
                for n in range(number_list_count):
                    column_total += number_lists[n][index]
                total += column_total

    return total


def solution_part1(puzzle_input) -> int:
    logging.debug("solution_part1")
    return get_total_sum(puzzle_input)


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
