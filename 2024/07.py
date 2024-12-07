from util import *
from itertools import islice, product

ADD = lambda x, y: x + y
MUL = lambda x, y: x * y
CONCAT = lambda x, y: int(str(x) + str(y))


def check(target, nums, ops):
    for operators in product(ops, repeat=len(nums) - 1):
        result = nums[0]
        for op, num in zip(operators, islice(nums, 1, None)):
            result = op(result, num)
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
