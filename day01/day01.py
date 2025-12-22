import argparse
import logging

LOGFILENAME = "day01.log"


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
    if args.debug:
        print("set log level to debug")
        logging.basicConfig(format="%(message)s", level=logging.DEBUG)
    if args.logfile:
        print(f"set logging to output file {LOGFILENAME}")
        logging.basicConfig(
            format="%(message)s", level=logging.DEBUG, filename=LOGFILENAME
        )

    return args


def get_test_input():
    return ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


def test_part1():
    test_input = get_test_input()
    assert solution_part1(test_input) == 3


def test_part2():
    test_input = get_test_input()
    assert solution_part2(test_input) == 6


def get_input():
    with open("input.txt") as file:
        lines = [line for line in file.read().split("\n") if line]
    return lines


def solution_part1(input) -> int:
    logging.debug("solution_part1")
    zero_count = 0
    position = 50
    dial_width = 100

    for turn in input:
        dir = 1 if turn[0] == "R" else -1
        value = int(turn[1:])

        logging.debug(f"dir: {turn[0]} ({dir}) ({value})")

        position = (position + dir * value) % dial_width
        logging.debug(f"position: {position}")
        if position == 0:
            zero_count += 1
            logging.debug(f"\tDial points to 0")
            logging.debug(f"zero_count: {zero_count}")
        logging.debug("---\n")

    return zero_count


def solution_part2(input) -> int:
    logging.debug("solution_part2")
    zero_count = 0
    old_position = 50
    dial_width = 100

    for turn in input:
        dir = 1 if turn[0] == "R" else -1
        value = int(turn[1:])

        logging.debug(f"turn: {turn}")
        logging.debug(f"dir: {dir}")

        rotation = value / dial_width
        new_position = (old_position + dir * value) % dial_width

        logging.debug(f"old_position: {old_position}")
        logging.debug(f"new_position: {new_position}")
        logging.debug(f"rotation: {rotation}")

        if abs(rotation) >= 1:
            to_add = int(abs(rotation))
            logging.debug(f"\tRotation Rule - to_add: {to_add}")
            zero_count += to_add

        if new_position == 0:
            zero_count += 1
            old_position = new_position
            logging.debug(f"\tDial points to 0")
            logging.debug(f"zero_count: {zero_count}")
            logging.debug("---\n")
            continue

        if dir > 0 and new_position < old_position:
            zero_count += 1
            logging.debug(f"\tDial past 0 with dir > 0")
        elif dir < 0 and new_position > old_position and old_position != 0:
            zero_count += 1
            logging.debug(f"\tDial past 0 with dir < 0")

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