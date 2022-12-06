from typing import List

from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)


INPUT_FILENAME = "aoc/day_06/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_06/EXAMPLE_01.txt"


def process_lines(lines: List[str], num_chars=4):
    first_markers = []
    for line in lines:
        first_markers.append(get_first_marker(line, num_chars))
    return first_markers


def get_first_marker(line, num_chars=4):
    for i in range(num_chars-1, len(line)):
        sequence = set(line[i-num_chars+1:i+1])
        if len(sequence) == num_chars:
            return i + 1
    return None


@time_it
def solve_part_1():
    print("Day 06 - Part 1")
    lines = read_input_lines(INPUT_FILENAME)
    first_markers = process_lines(lines)
    print(f"The first markers were {first_markers}")


@time_it
def solve_part_2():
    print("Day 06 - Part 2")
    lines = read_input_lines(INPUT_FILENAME)
    first_markers = process_lines(lines, 14)
    print(f"The first markers were {first_markers}")


if __name__ == "__main__":
    solve_part_1()
    solve_part_2()