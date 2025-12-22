import argparse
import logging
from pathlib import Path

LOGFILENAME = "day01.log"
DIAL_WIDTH = 100
INITIAL_DIAL_POSITION = 50


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Set loglevel to debug",
    )
    parser.add_argument(
        "-lf",
        "--logfile",
        action="store_true",
        help=f"Set logging output to file: {LOGFILENAME}",
    )
    parser.add_argument(
        "-t",
        "--testinput",
        action="store_true",
        help="Use test input data for run",
    )
    parser.add_argument(
        "-s1",
        "--solution1",
        action="store_true",
        help="Only run solution 1",
    )
    parser.add_argument(
        "-s2",
        "--solution2",
        action="store_true",
        help="Only run solution 2",
    )

    args = parser.parse_args()
    log_kwargs = None
    if args.debug or args.logfile:
        log_kwargs = {"format": "%(message)s", "level": logging.DEBUG}
        if args.logfile:
            log_kwargs["filename"] = LOGFILENAME
            print(f"set logging to output file {LOGFILENAME}")

    if args.debug:
        print("set log level to debug")

    if log_kwargs is not None:
        logging.basicConfig(**log_kwargs)

    return args


def get_test_input():
    return ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


def get_input():
    input_path = Path(__file__).parent / "input.txt"
    with open(input_path) as file:
        lines = [line for line in file.read().split("\n") if line]
    return lines


def get_direction(turn: str) -> int:
    if turn[0] == "R":
        return 1
    else:
        return -1


def get_value(turn: str) -> int:
    return int(turn[1:])


def solution_part1(input) -> int:
    logging.debug("solution_part1")
    zero_count = 0
    position = INITIAL_DIAL_POSITION

    for turn in input:
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


def solution_part2(input) -> int:
    logging.debug("solution_part2")
    zero_count = 0
    old_position = INITIAL_DIAL_POSITION

    for turn in input:
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
    args = setup_parser()

    if args.testinput:
        print("using testdata")
        print("--------------\n")
        input = get_test_input()
    else:
        print("using input file")
        print("----------------\n")
        input = get_input()

    if args.solution1 is False and args.solution2 is False:
        args.solution1 = True
        args.solution2 = True

    if args.solution1:
        sol1 = solution_part1(input)
        print(f"Part 1: {sol1}")
        print("=======\n")

    if args.solution2:
        sol2 = solution_part2(input)
        print(f"Part 2: {sol2}")
        print("=======\n")
