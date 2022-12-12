from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix, read_input_split_on_empty_line
)


INPUT_FILENAME = "aoc/day_11/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_11/EXAMPLE_01.txt"


def process_lines(lines):
    for i, line in enumerate(lines):
        monkey = int(line[0][7])
        starting_items = [ int(x) for x in line[1][16:].split(", ")]
        operator = line[2][21]
        actor = line[2][23:]
        test = int(line[3][19])
        true = int(line[4][25])
        false = int(line[5][26])
        a = 1

    return None
@time_it
def solve_part_1():
    print("Day 11 - Part 1")
    lines = read_input_split_on_empty_line(EXAMPLE_FILENAME)
    results = process_lines(lines)
    print(lines)

@time_it
def solve_part_2():
    print("Day 11 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()