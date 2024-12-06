from itertools import product
from util import *
from collections import defaultdict

EMPTY = "."
WALL = "#"
GUARD = "^"

DIRS = [
    (-1, 0),  # N
    (0, +1),  # W
    (+1, 0),  # S
    (0, -1),  # E
]


def part_1():
    print(f"Part 1: {count_steps(list(read_input()))}")


def count_steps(grid):
    n, m = len(grid), len(grid[0])

    x = 0
    for line in grid:
        if GUARD in line:
            guard_pos = (
                x,
                line.find(GUARD) if type(line) == str else line.index(GUARD),
            )
            break
        x += 1

    def within_bounds(x, y):
        return 0 <= x < n and 0 <= y < m

    def move(x, y, direction):
        # 4 tries
        for _ in range(4):
            nx, ny = x + DIRS[direction][0], y + DIRS[direction][1]
            if within_bounds(nx, ny) and grid[nx][ny] == WALL:
                direction = (direction + 1) & 3
                continue
            return nx, ny, direction
        return False

    guard_x, guard_y = guard_pos
    guard_dir = 0  # starting position is N
    steps = defaultdict(set)
    while within_bounds(guard_x, guard_y):
        steps[(guard_x, guard_y)].add(guard_dir)
        move_res = move(guard_x, guard_y, guard_dir)
        if not move_res:
            return False
        guard_x, guard_y, guard_dir = move_res
        if guard_dir in steps[(guard_x, guard_y)]:
            return False

    return len(steps) - 1  # account for the last check


def part_2():
    grid = list(list(line) for line in read_input())
    n, m = len(grid), len(grid[0])

    total = 0
    for x, y in product(range(n), range(m)):
        # https://i.imgur.com/beryVOv.png
        if grid[x][y] == EMPTY:
            candidate_index += 1
            grid_copy = [line[:] for line in grid]
            grid_copy[x][y] = WALL
            if not count_steps(grid_copy):
                total += 1

    print(f"Part 2: {total}")


part_1()
part_2()
