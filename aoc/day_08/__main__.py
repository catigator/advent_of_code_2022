from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)


INPUT_FILENAME = "aoc/day_08/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_08/EXAMPLE_01.txt"


def get_row_positions(y_start, y_end, x_start, x_end):
    y = range(y_start, y_end + 1)
    x = range(x_start, x_end + 1)

    positions = [[(py, px) for py in y] for px in x]
    return positions


def get_visibility(matrix, visible):
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            ylen = len(matrix)
            xlen = len(matrix[0])
            row_positions_vert = get_row_positions(y, y, 0, xlen)
            row_positions_hori = get_row_positions(0, ylen, x, x)
            a = 1



@time_it
def solve_part_1():
    print("Day 08 - Part 1")
    matrix = read_input_int_matrix(EXAMPLE_FILENAME)
    visible = [[0] * len(matrix)] * len(matrix[0])
    print(matrix)
    print(visible)
    get_visibility(matrix, visible)


@time_it
def solve_part_2():
    print("Day 08 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()