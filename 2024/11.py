from util import *
from functools import cache
from math import log10
from collections import Counter


@cache
def blink(stone):
    if stone == 0:
        return (1,)

    n_digits = int(log10(stone)) + 1

    if not n_digits & 1:
        return (
            stone // (10 ** (n_digits // 2)),
            stone % (10 ** (n_digits // 2)),
        )

    return (stone * 2024,)


stones = Counter(list(map(int, list(read_input())[0].split(" "))))

for _ in range(75):
    new_stones = Counter()
    for stone in stones:
        for next_stone in blink(stone):
            new_stones[next_stone] += stones[stone]
    stones = new_stones

print(f"{stones.total()}")
