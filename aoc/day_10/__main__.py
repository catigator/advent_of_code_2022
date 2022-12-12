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
    signal_strengths = []
    x = 1

    for line in split_lines:
        command = line[0]

        if command != "noop":

            if cycle + 1 == 20 or (cycle + 1 - 20) % 40 == 0:
                signal_strength = (cycle+1) * x
                signal_strengths.append(signal_strength)

            cycle += 2

            if cycle == 20 or (cycle - 20) % 40 == 0:
                signal_strength = cycle * x
                signal_strengths.append(signal_strength)

            val = int(line[1])
            x += val
        else:
            cycle += 1

            if cycle == 20 or (cycle - 20) % 40 == 0:
                signal_strength = cycle * x
                signal_strengths.append(signal_strength)

        if cycle > 220:
            if cycle == 20 or (cycle - 20) % 40 == 0:
                signal_strength = cycle * x
                signal_strengths.append(signal_strength)
            break

    print(f"X is {x} after {cycle} cycles")
    signal_sum = sum(signal_strengths)
    print(f"The sum of these signal strengths is {signal_sum}")

    return x, cycle, signal_strengths


def drawing_sprite(cycle, x):
    if x - 1 <= cycle <= x + 1:
        return True
    return False


def crt_char(cycle, x):
    if drawing_sprite(cycle % 40, x):
        return "#"
    else:
        return "."


def process_lines_2(split_lines):
    cycle = 0
    signal_strengths = []
    x = 1
    crt = ""
    crt_pos = 0
    cycle_x_tuples = []

    for line in split_lines:
        command = line[0]

        if command != "noop":

            if cycle + 1 == 20 or (cycle + 1 - 20) % 40 == 0:
                signal_strength = (cycle+1) * x
                signal_strengths.append(signal_strength)

            cycle_x_tuples.append((cycle, x))
            cycle_x_tuples.append((cycle + 1, x))
            cycle += 2

            if cycle == 20 or (cycle - 20) % 40 == 0:
                signal_strength = cycle * x
                signal_strengths.append(signal_strength)

            val = int(line[1])
            x += val
        else:
            cycle_x_tuples.append((cycle, x))
            cycle += 1

            if cycle == 20 or (cycle - 20) % 40 == 0:
                signal_strength = cycle * x
                signal_strengths.append(signal_strength)

        if cycle > 220:
            if cycle == 20 or (cycle - 20) % 40 == 0:
                signal_strength = cycle * x
                signal_strengths.append(signal_strength)
        # if cycle > 243:
        #     break

    for i, tup in enumerate(cycle_x_tuples):
        if i % 40 == 0:
            crt += "\n"
        crt += crt_char(tup[0], tup[1])
    print(crt)
    # It's PLPAFBCL !
    print("")

    print(f"X is {x} after {cycle} cycles")
    signal_sum = sum(signal_strengths)
    print(f"The sum of these signal strengths is {signal_sum}")

    return x, cycle, signal_strengths


@time_it
def solve_part_1():
    print("Day 10 - Part 1")
    lines = read_input_lines(INPUT_FILENAME)
    split_lines = [line.split() for line in lines]
    x, cycle, signal_strengths = process_lines(split_lines)
    print(f"The signal strength total is {sum(signal_strengths)}")
    print(x, cycle)


@time_it
def solve_part_2():
    print("Day 10 - Part 2")
    print("Day 10 - Part 1")
    lines = read_input_lines(INPUT_FILENAME)
    split_lines = [line.split() for line in lines]
    x, cycle, signal_strengths = process_lines_2(split_lines)
    print(f"The signal strength total is {sum(signal_strengths)}")
    print(x, cycle)


if __name__ == "__main__":
    solve_part_1()
    solve_part_2()