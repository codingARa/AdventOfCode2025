import logging
import sys
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).parent.parent))

from aoc_utils import DaySolution, run_solutions, setup_parser

LOGFILENAME = "day02.log"
TEST_RESULT_PART1 = 1227775554
TEST_RESULT_PART2 = 4174379265


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
    assert solution_part1(test_input) == TEST_RESULT_PART1


def test_part2():
    test_input = get_puzzle_test_input()
    assert solution_part2(test_input) == TEST_RESULT_PART2


def get_puzzle_input(script_path: Path) -> list[str]:
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = file.readlines()
        id_pairs = []
        for line in lines:
            line = line.strip("\n")
            id_pairs += line.split(",")
    return id_pairs


@dataclass
class PuzzleRange:
    start: int
    end: int


def get_puzzle_ranges_from_puzzle_input(puzzle_input: list[str]) -> list[PuzzleRange]:
    ranges = []
    for line in puzzle_input:
        range_pair = line.split("-")
        ranges.append(PuzzleRange(start=int(range_pair[0]), end=int(range_pair[1])))
    return ranges


def chunk_string(string: str, chunk_length: int) -> list[str]:
    if chunk_length <= 0:
        raise ValueError(f"chunk_length must be greater than 0, got {chunk_length}")
    chunks = []
    for index in range(0, len(string), chunk_length):
        chunks.append(string[index : index + chunk_length])
    return chunks


def solution_part1(puzzle_input: list[str]) -> int:
    logging.debug("solution_part1")
    puzzle_ranges = get_puzzle_ranges_from_puzzle_input(puzzle_input)
    logging.debug(f"puzzle ranges: {puzzle_ranges}")
    return get_answer_by_iterating_over_puzzle_ranges(
        puzzle_ranges, id_is_invalid_part1
    )


def get_answer_by_iterating_over_puzzle_ranges(
    puzzle_ranges: list[PuzzleRange], check_function: Callable[[str], bool]
) -> int:
    invalid_ids = []
    for p_range in puzzle_ranges:
        logging.debug(f"checking range {p_range.start}-{p_range.end} ...")
        for current_id in range(p_range.start, p_range.end + 1):
            if check_function(str(current_id)):
                logging.debug(f"The id {current_id} IS invalid!")
                invalid_ids.append(current_id)
            else:
                logging.debug(f"The id {current_id} is NOT invalid...")
            logging.debug("---\n")
    logging.debug(f"invalid ids: {invalid_ids}")
    answer = sum(invalid_ids)
    logging.debug(f"answer: {answer}")
    return answer


def id_is_invalid_part1(current_id: str) -> bool:
    length_current_id = len(current_id)
    logging.debug(f"checking id {current_id} ...")
    if (length_current_id % 2) == 0:
        substrings = chunk_string(current_id, length_current_id // 2)
        return all(x == substrings[0] for x in substrings)
    else:
        return False


def solution_part2(puzzle_input: list[str]) -> int:
    logging.debug("solution_part2")
    puzzle_ranges = get_puzzle_ranges_from_puzzle_input(puzzle_input)
    logging.debug(f"puzzle ranges: {puzzle_ranges}")
    return get_answer_by_iterating_over_puzzle_ranges(
        puzzle_ranges, id_is_invalid_part2
    )


def id_is_invalid_part2(current_id: str) -> bool:
    length_current_id = len(current_id)
    logging.debug(f"checking id {current_id} ...")
    for index_width in range(length_current_id // 2, 0, -1):
        if (length_current_id % index_width) == 0:
            logging.debug(f"length of {current_id} is divisible by {index_width}")
            substrings = chunk_string(current_id, index_width)
            logging.debug(f"substrings: {substrings}")
            match_found = all(x == substrings[0] for x in substrings)
            if match_found:
                return True
    return False


if __name__ == "__main__":
    args = setup_parser(LOGFILENAME)
    day_solution = DaySolution(
        get_puzzle_test_input=get_puzzle_test_input,
        get_puzzle_input=partial(get_puzzle_input, Path(__file__)),
        solution_part1=solution_part1,
        solution_part2=solution_part2,
    )
    run_solutions(args, day_solution)
