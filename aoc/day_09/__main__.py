from collections import defaultdict

from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)
import numpy as np


INPUT_FILENAME = "aoc/day_09/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_09/EXAMPLE_04.txt"


DIRS = {
    "U": (0, 1),
    "R": (1, 0),
    "D": (0, -1),
    "L": (-1, 0)
}


def add_pos(a, b):
    return a[0] + b[0], a[1] + b[1]


def get_diff(a, b):
    """
    from a to b
    """
    return b[0] - a[0], b[1] - a[1]


def get_move(command):
    direction = DIRS[command[0]]
    mult = int(command[1])
    move = (direction[0]*mult, direction[1]*mult)
    return move, direction, mult


def get_tail_move(diff):
    direction = (np.sign(diff[0]), np.sign(diff[1]))
    return direction



def process_commands(split_lines):
    visited = defaultdict(int)
    tail = (0, 0)
    head = (0, 0)
    diff = (0, 0)
    visited[tail] += 1

    for line in split_lines:
        move, direction, mult = get_move(line)
        for i in range(mult):
            head = add_pos(head, direction)
            diff = get_diff(tail, head)
            are_touching = np.abs(diff[0]) <= 1 and np.abs(diff[1]) <= 1
            if not are_touching:
                tail_move = get_tail_move(diff)
                tail = add_pos(tail, tail_move)
                visited[tail] += 1
    return visited



@time_it
def solve_part_1():
    print("Day 09 - Part 1")
    lines = read_input_lines(INPUT_FILENAME)
    split_lines = [line.split() for line in lines]
    visited = process_commands(split_lines)
    print(f"The tail visits {len(visited)} locations at least once")


@time_it
def solve_part_2():
    print("Day 09 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()