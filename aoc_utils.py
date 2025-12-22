import argparse
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


def setup_parser(logfilename: str):
    """Setup argument parser with common AoC options."""
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
        help=f"Set logging output to file: {logfilename}",
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
            log_kwargs["filename"] = logfilename
            print(f"set logging to output file {logfilename}")

    if args.debug:
        print("set log level to debug")

    if log_kwargs is not None:
        logging.basicConfig(**log_kwargs)

    return args


def get_puzzle_input(script_path: Path):
    """Read puzzle input from input.txt in the same directory as the script."""
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = [line for line in file.read().split("\n") if line]
    return lines


@dataclass
class DaySolution:
    """Container for daily AoC solution functions."""

    get_test_puzzle_input: Callable
    get_puzzle_input: Callable
    solution_part1: Callable
    solution_part2: Callable


def run_solutions(args, day_solution: DaySolution):
    """Execute solutions based on command line arguments."""
    if args.testinput:
        print("using testdata\n")
        puzzle_input = day_solution.get_test_puzzle_input()
    else:
        print("using puzzle input file\n")
        puzzle_input = day_solution.get_puzzle_input()

    if args.solution1 is False and args.solution2 is False:
        args.solution1 = True
        args.solution2 = True

    if args.solution1:
        sol1 = day_solution.solution_part1(puzzle_input)
        print(f"solution part 1: {sol1}")
        print("=======\n")

    if args.solution2:
        sol2 = day_solution.solution_part2(puzzle_input)
        print(f"solution part 2: {sol2}")
        print("=======\n")
