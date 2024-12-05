from util import *


def xmas_line(line):
    return line.count("XMAS") + line.count("SAMX")


def xmas_column(buf):
    # buf is a 4-line buffer
    total = 0
    for i in range(len(buf[0])):
        total += int(
            buf[0][i] == "X"
            and buf[1][i] == "M"
            and buf[2][i] == "A"
            and buf[3][i] == "S"
        )
        total += int(
            buf[0][i] == "S"
            and buf[1][i] == "A"
            and buf[2][i] == "M"
            and buf[3][i] == "X"
        )
    return total


def xmas_diagonal(buf):
    # buf is a 4-line buffer
    total = 0
    for i in range(len(buf[0]) - 3):
        total += int(
            buf[0][i] == "X"
            and buf[1][i + 1] == "M"
            and buf[2][i + 2] == "A"
            and buf[3][i + 3] == "S"
        )
        total += int(
            buf[0][i] == "S"
            and buf[1][i + 1] == "A"
            and buf[2][i + 2] == "M"
            and buf[3][i + 3] == "X"
        )
        total += int(
            buf[0][i + 3] == "X"
            and buf[1][i + 2] == "M"
            and buf[2][i + 1] == "A"
            and buf[3][i] == "S"
        )
        total += int(
            buf[0][i + 3] == "S"
            and buf[1][i + 2] == "A"
            and buf[2][i + 1] == "M"
            and buf[3][i] == "X"
        )
    return total


def part_1():
    buf = list()
    total = 0
    for line in read_input():
        if len(buf) < 4:
            buf.append(line)
        else:
            buf = buf[1:] + [line]

        total += xmas_line(buf[-1])
        if len(buf) < 4:
            continue
        total += xmas_column(buf)
        total += xmas_diagonal(buf)

    print(f"Part 1: {total}")


def xmas_cross(buf):
    # buf is a 3-line buffer
    total = 0
    for i in range(1, len(buf[0]) - 1):
        if buf[1][i] != "A":
            continue
        total += int(
            (
                buf[0][i - 1] == "M"
                and buf[2][i + 1] == "S"
                or buf[0][i - 1] == "S"
                and buf[2][i + 1] == "M"
            )
            and (
                buf[0][i + 1] == "M"
                and buf[2][i - 1] == "S"
                or buf[0][i + 1] == "S"
                and buf[2][i - 1] == "M"
            )
        )
    return total


def part_2():
    buf = list()
    total = 0
    for line in read_input():
        if len(buf) < 3:
            buf.append(line)
        else:
            buf = buf[1:] + [line]
        if len(buf) < 3:
            continue
        total += xmas_cross(buf)
    print(f"Part 2: {total}")


part_1()
part_2()
