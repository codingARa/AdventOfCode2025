import argparse
import logging


def setupParser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Set loglevel to debug",
    )

    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def getTestInput():
    return ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


def test_part1():
    test_input = getTestInput()
    assert solution_part1(test_input) == 3


def test_part2():
    test_input = getTestInput()
    assert solution_part2(test_input) == 4


def getInput():
    with open("input.txt") as file:
        line = [l for l in file.read().split("\n") if l]
    return line


def solution_part1(input) -> int:
    logging.debug("solution_part1")
    zero_count = 0
    position = 50
    dial_width = 100
    for turn in input:
        dir = 1 if turn[0] == "R" else -1
        value = int(turn[1:])
        logging.debug(f"turn[0]: {turn[0]}")
        logging.debug(f"dir: {dir}")
        logging.debug(f"value: {value}")
        position = (position + dir * value) % dial_width
        if position == 0:
            zero_count += 1

    return zero_count


def solution_part2(input) -> int:
    return 4


if __name__ == "__main__":
    setupParser()
    input = getInput()

    sol1 = solution_part1(input)
    print("Part 1: ", sol1)

    # sol2 = solution_part2(input)
    # print("Part 2: ", sol2)
