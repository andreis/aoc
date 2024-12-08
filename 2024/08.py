from util import *
from collections import defaultdict
from itertools import combinations, product


EMPTY = "."


def part_12():
    grid = list(read_input())
    n, m = len(grid), len(grid[0])
    antennae = defaultdict(list)
    for x, y in product(range(n), range(m)):
        if grid[x][y] == EMPTY:
            continue
        antennae[grid[x][y]].append((x, y))

    antinodes = set()
    harmonic_antinodes = set()
    for nodes in antennae.values():
        for a, b in combinations(nodes, 2):
            diff = (b[0] - a[0], b[1] - a[1])
            for c in (
                (a[0] - diff[0], a[1] - diff[1]),
                (b[0] + diff[0], b[1] + diff[1]),
            ):
                if 0 <= c[0] < n and 0 <= c[1] < m:
                    antinodes.add(c)
            for c, sign in ((a, -1), (b, 1)):
                while 0 <= c[0] < n and 0 <= c[1] < m:
                    harmonic_antinodes.add(c)
                    c = (c[0] + sign * diff[0], c[1] + sign * diff[1])

    print(f"Part 1: {len(antinodes)}")
    print(f"Part 2: {len(harmonic_antinodes)}")


part_12()
