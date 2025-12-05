from bisect import bisect_right
from functools import reduce
from math import inf
from os import environ


def binsrc(ranges, target):
    idx = bisect_right(ranges, (target, inf)) - 1
    return idx >= 0 and ranges[idx][0] <= target <= ranges[idx][1]


def compress(ranges):
    return reduce(
        lambda acc, r: (
            acc[:-1] + [(acc[-1][0], max(acc[-1][1], r[1]))]
            if acc and r[0] <= acc[-1][1]
            else acc + [r]
        ),
        sorted(ranges),
        [],
    )


with open("05.sample.txt" if environ.get("DEBUG") else "05.txt") as f:
    block1, block2 = f.read().split("\n\n")
    ranges = compress(tuple(map(int, l.split("-"))) for l in block1.split())
    ids = map(int, block2.split())

    print(sum(binsrc(ranges, _id) for _id in ids))
    print(sum(b - a + 1 for a, b in ranges))
