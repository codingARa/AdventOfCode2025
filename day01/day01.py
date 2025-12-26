import logging
import sys
from functools import partial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from aoc_utils import DaySolution, run_solutions, setup_parser

LOGFILENAME = "day01.log"
DIAL_WIDTH = 100
INITIAL_DIAL_POSITION = 50


def get_puzzle_input(script_path: Path) -> list[str]:
    """Read puzzle input from input.txt in the same directory as the script."""
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = [line for line in file.read().split("\n") if line]
    return lines


def get_puzzle_test_input():
    return ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


def get_direction(turn: str) -> int:
    if turn[0] == "R":
        return 1
    else:
        return -1


def get_value(turn: str) -> int:
    return int(turn[1:])


def solution_part1(puzzle_input: list[str]) -> int:
    logging.debug("solution_part1")
    zero_count = 0
    position = INITIAL_DIAL_POSITION

    for turn in puzzle_input:
        direction = get_direction(turn)
        value = get_value(turn)

        logging.debug(f"direction: {turn[0]} ({direction}) ({value})")

        position = (position + direction * value) % DIAL_WIDTH
        logging.debug(f"position: {position}")
        if position == 0:
            zero_count += 1
            logging.debug("\tDial points to 0")
            logging.debug(f"zero_count: {zero_count}")
        logging.debug("---\n")

    return zero_count


def solution_part2(puzzle_input: list[str]) -> int:
    logging.debug("solution_part2")
    zero_count = 0
    old_position = INITIAL_DIAL_POSITION

    for turn in puzzle_input:
        direction = get_direction(turn)
        value = get_value(turn)

        logging.debug(f"turn: {turn}")
        logging.debug(f"direction: {direction}")

        rotation = value / DIAL_WIDTH
        new_position = (old_position + direction * value) % DIAL_WIDTH

        logging.debug(f"old_position: {old_position}")
        logging.debug(f"new_position: {new_position}")
        logging.debug(f"rotation: {rotation}")

        if abs(rotation) >= 1:
            to_add = int(abs(rotation))
            logging.debug(f"\tDial turned more than once - to_add: {to_add}")
            zero_count += to_add

        if new_position == 0:
            zero_count += 1
            old_position = new_position
            logging.debug("\tDial points to 0")
            logging.debug(f"zero_count: {zero_count}")
            logging.debug("---\n")
            continue

        if direction > 0 and new_position < old_position:
            zero_count += 1
            logging.debug("\tDial past 0 with dir > 0")
        elif direction < 0 and new_position > old_position and old_position != 0:
            zero_count += 1
            logging.debug("\tDial past 0 with dir < 0")

        old_position = new_position

        logging.debug(f"zero_count: {zero_count}")
        logging.debug("---\n")

    return zero_count


if __name__ == "__main__":
    args = setup_parser(LOGFILENAME)
    day_solution = DaySolution(
        get_puzzle_test_input=get_puzzle_test_input,
        get_puzzle_input=partial(get_puzzle_input, Path(__file__)),
        solution_part1=solution_part1,
        solution_part2=solution_part2,
    )
    run_solutions(args, day_solution)
