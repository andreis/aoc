from util import *
from itertools import islice, product

ADD = 0
MUL = 1
CONCAT = 2


def check(target, nums, ops):
    for operators in product(ops, repeat=len(nums) - 1):
        result = nums[0]
        for op, num in zip(operators, islice(nums, 1, None)):
            if op == CONCAT:
                result = int(str(result) + str(num))
            elif op == ADD:
                result += num
            elif op == MUL:
                result *= num
            else:
                raise Exception("Unknown operator")
        if result == target:
            return target
    return 0


def solve(lines, ops):
    return sum(
        check(int(l), list(map(int, r.split())), ops)
        for l, r in map(lambda l: l.split(": "), lines)
    )


print(f"Part 1: {solve(read_input(), [ADD, MUL])}")
print(f"Part 2: {solve(read_input(), [ADD, MUL, CONCAT])}")
