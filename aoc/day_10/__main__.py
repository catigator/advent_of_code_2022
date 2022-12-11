from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)


INPUT_FILENAME = "aoc/day_10/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_10/EXAMPLE_02.txt"

def process_lines(split_lines):
    cycle = 0
    adds = []
    to_delete = []
    signal_strengths = []
    x_vals = []
    vals = []
    x = 1
    for line in split_lines:
        cycle += 1
        command = line[0]
        x_vals.append(x)

        if cycle % 20 == 0:
            signal_strengths.append(cycle*x)

        if command != "noop":
            val = int(line[1])

            vals.append(val)
            if command == "addx":
                num = int(val)
                adds.append((cycle+2, num))
        else:
            vals.append(0)
        for i, add in enumerate(adds):
            if add[0] == cycle:
                x += add[1]
                to_delete.append(i)
        for i in to_delete:
            adds.pop(i)
        to_delete = []
    print(f"X is {x} after {cycle} cycles")

    to_delete = []

    for just_looping_through_the_last_cycles in range(221 - len(split_lines)):
        cycle += 1
        x_vals.append(x)
        if cycle % 20 == 0:
            signal_strengths.append(cycle*x)
        for i, add in enumerate(adds):
            if add[0] == cycle:
                x += add[1]
                to_delete.append(i)
        for i in to_delete:
            adds.pop(i)
        to_delete = []

    return x, cycle, signal_strengths


@time_it
def solve_part_1():
    print("Day 10 - Part 1")
    lines = read_input_lines(EXAMPLE_FILENAME)
    split_lines = [line.split() for line in lines]
    x, cycle, signal_strengths = process_lines(split_lines)
    print(f"The signal strength total is {sum(signal_strengths)}")
    print(x, cycle)


@time_it
def solve_part_2():
    print("Day 10 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()