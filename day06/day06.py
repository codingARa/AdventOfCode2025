import logging
import sys
from functools import partial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from aoc_utils import DaySolution, run_solutions, setup_parser

LOGFILENAME = "day06.log"
TEST_RESULT_PART1 = 4277556
TEST_RESULT_PART2 = 3263827
# Expected results for the actual puzzle input - received after solving the puzzle
RESULT_PART1 = 5227286044585
RESULT_PART2 = 10227753257799


def parse_input_lines_part1(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    number_lists = []
    operator_list = []
    for line in lines:
        split_line = line.split()
        try:
            number_lists.append([int(num) for num in split_line])
        except ValueError:
            operator_list = split_line
    return number_lists, operator_list


def parse_input_lines_part2(lines: list[str]):
    columns = zip(*lines)
    return list(columns)


def get_puzzle_test_input():
    return [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]


def get_puzzle_input(script_path: Path):
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = file.readlines()
    return lines


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
    parse_input = parse_input_lines_part1(puzzle_input)
    return get_total_sum(parse_input)


def get_total_sum_vertically(puzzle_input) -> int:
    total = 0

    column_total = None
    operator = None
    for ts in puzzle_input:
        new_operator = ts[-1]
        if new_operator != " ":
            operator = new_operator

        number_tuple = ts[0:-1]
        new_number = None
        number_string = ""
        for n in number_tuple:
            number_string += n
        number_string = number_string.strip()
        if number_string == "":
            # new column reached
            total += column_total
            column_total = None
            continue
        else:
            new_number = int(number_string.strip())

        match operator:
            case "*":
                logging.debug("Multiplication")
                if column_total is None:
                    column_total = 1
                column_total *= new_number
            case "+":
                logging.debug("Addition")
                if column_total is None:
                    column_total = 0
                column_total += new_number
            case _:
                logging.debug("new column")

    total += column_total
    return total


def solution_part2(puzzle_input) -> int:
    logging.debug("solution_part2")
    parse_input = parse_input_lines_part2(puzzle_input)
    return get_total_sum_vertically(parse_input)


if __name__ == "__main__":
    args = setup_parser(LOGFILENAME)
    day_solution = DaySolution(
        get_puzzle_test_input=get_puzzle_test_input,
        get_puzzle_input=partial(get_puzzle_input, Path(__file__)),
        solution_part1=solution_part1,
        solution_part2=solution_part2,
    )
    run_solutions(args, day_solution)
