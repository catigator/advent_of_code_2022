from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)
import numpy as np


INPUT_FILENAME = "aoc/day_08/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_08/EXAMPLE_01.txt"


def get_row_positions(y_start, y_end, x_start, x_end):
    ysign = np.sign(y_end - y_start)
    xsign = np.sign(x_end - x_start)
    if ysign == 0:
        ysign = 1
    if xsign == 0:
        xsign = 1
    y = range(y_start, y_end, ysign)
    x = range(x_start, x_end, xsign)
    if x == range(0, 0):
        x = range(x_start, x_start + 1)

    if y == range(0, 0):
        y = range(y_start, y_end + 1)

    positions = [(py, px) for py in y for px in x]
    return positions


def check_row(row, matrix, visible):
    # print("-----------")
    # print(f"row: {row}")
    pos = row[0]

    visible[pos[0]][pos[1]] = 1
    last_tree = matrix[pos[0]][pos[1]]
    # print(f"pos: {pos}, last_tree: {last_tree}")
    for i in range(1, len(row)):
        pos = row[i]
        tree = matrix[pos[0]][pos[1]]
        # print(f"pos: {pos} , tree: {tree}, last_tree: {last_tree}")
        if tree > last_tree:
            visible[pos[0]][pos[1]] = 1
            # print(f"Setting [{pos[0]}][{pos[1]}] to visible")
            last_tree = tree
        else:
            # this one isn't visible
            pass
    # print_matrix(visible)
    return visible


def get_visibility(matrix, visible):
    """

    Vert
    [[[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]],
     [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]],
      [[(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]],
       [[(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3)]],
        [[(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4)]]]
    """
    ylen = len(matrix)
    xlen = len(matrix[0])

    row_positions_vert = []
    row_positions_hori = []

    for y in range(len(matrix)):
        # Hori = left to right
        row_positions_hori.append(get_row_positions(y, y, 0, xlen))
    for x in range(len(matrix[0])):
        # Vert = up to down
        row_positions_vert.append(get_row_positions(0, ylen, x, x))

    for row in row_positions_hori:
        visible = check_row(row, matrix, visible)
        row.reverse()
        visible = check_row(row, matrix, visible)

    for row in row_positions_vert:
        visible = check_row(row, matrix, visible)
        row.reverse()
        visible = check_row(row, matrix, visible)

    a = 1


def print_matrix(matrix):
    for line in matrix:
        print(line)


def count_visible(visible):
    count = 0
    for y in range(len(visible)):
        for x in range(len(visible[y])):
            if visible[y][x] == 1:
                count += 1
    return count


def get_rows_from_tree(pos, matrix):
    ylen = len(matrix)
    xlen = len(matrix[0])

    y = pos[0]
    x = pos[1]

    rows = []
    top = get_row_positions(y, 0, x, x)
    right = get_row_positions(y, y, x, xlen)
    left = get_row_positions(y, y, x, 0)
    down = get_row_positions(y, y, x, 0)

@time_it
def solve_part_1():
    print("Day 08 - Part 1")
    matrix = read_input_int_matrix(INPUT_FILENAME)
    len_y = len(matrix)
    len_x = len(matrix[0])
    visible = np.zeros((len_y, len_x))
    # print_matrix(matrix)
    # print("-------")
    # print_matrix(visible)
    get_visibility(matrix, visible)
    num_visible = count_visible(visible)
    print(f"There are {num_visible} visible trees")


@time_it
def solve_part_2():
    print("Day 08 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()