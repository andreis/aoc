from util import read_input


def parse_numbers(line):
    line = line.replace("+", "=")
    return tuple(map(lambda s: int(s.split("=")[1]), line.split(": ")[1].split(", ")))


def parse_input():
    lines = list()

    for line in read_input():
        if line.startswith("Button A:"):
            ax, ay = parse_numbers(line)
        elif line.startswith("Button B:"):
            bx, by = parse_numbers(line)
        elif line.startswith("Prize:"):
            px, py = parse_numbers(line)
        else:
            lines.append((ax, ay, bx, by, px, py))
            continue
    lines.append((ax, ay, bx, by, px, py))
    return lines


"""
b = (AXPY - AYPX) / (AXBY - AYBX)
a = (PX - BX * b) / AX
"""


def solve(line):
    ax, ay, bx, by, px, py = line

    px += 10000000000000
    py += 10000000000000

    # check for division by zero
    if bx * ay == ax * by:
        # no solution
        return 0, 0

    b = round((ax * py - ay * px) / (ax * by - ay * bx))
    a = round((px - bx * b) / ax)

    # check the original equations
    if ax * a + b * bx == px and ay * a + b * by == py:
        return a, b

    return 0, 0


def part_12():
    tokens = 0
    for line in parse_input():
        a, b = solve(line)
        tokens += 3 * a + 1 * b
    return tokens


print(part_12())
