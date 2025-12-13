from os import environ
from itertools import combinations
from functools import reduce
from operator import xor
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def parse_input(lines):
    for line in lines:
        tokens = line.split()
        target = sum(1 << i for i, c in enumerate(tokens[0][1:-1]) if c == "#")
        buttons = [sum(1 << int(x) for x in t[1:-1].split(",")) for t in tokens[1:-1]]
        joltage = [int(x) for x in tokens[-1][1:-1].split(",")]
        yield target, buttons, joltage


def part1(targets, buttons):
    total = 0
    for target, buttons in zip(targets, buttons):
        for k in range(len(buttons) + 1):
            if any(reduce(xor, c, 0) == target for c in combinations(buttons, k)):
                total += k
                break
    return total


def part2(buttons, joltages):
    total = 0
    for mask_list, b_vec in zip(buttons, joltages):
        rows, cols = len(b_vec), len(mask_list)
        A = np.zeros((rows, cols))

        for j, mask in enumerate(mask_list):
            for i in range(rows):
                if (mask >> i) & 1:
                    A[i, j] = 1

        res = milp(c=np.ones(cols), constraints=LinearConstraint(A, b_vec, b_vec), integrality=np.ones(cols), bounds=Bounds(0, np.inf))

        if res.success:
            total += int(round(res.fun))

    return total


lines = open("10.sample.txt" if environ.get("DEBUG") else "10.txt").read().splitlines()
all_targets, all_buttons, all_joltages = zip(*parse_input(lines))

print(part1(all_targets, all_buttons))
print(part2(all_buttons, all_joltages))
