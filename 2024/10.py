from util import *
from itertools import product


def part_12():
    grid = list(list(map(int, line)) for line in read_input())
    starts = set()
    n, m = len(grid), len(grid[0])
    for x, y in product(range(n), range(m)):
        if grid[x][y] == 0:
            starts.add((x, y))

    def count_trails(x, y, ends=None):
        if ends is None:
            ends = set()

        if grid[x][y] == 9:
            ends.add((x, y))
            return
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == grid[x][y] + 1:
                count_trails(nx, ny, ends)

        return len(ends)

    def count_ratings(x, y, ends=None, path=None):
        if ends is None:
            ends = set()
        if path is None:
            path = [(x, y)]

        if grid[x][y] == 9:
            ends.add(tuple(path))
            return
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == grid[x][y] + 1:
                path.append((nx, ny))
                count_ratings(nx, ny, ends, path)
                path.pop()

        return len(ends)

    total_1 = total_2 = 0
    for x, y in starts:
        total_1 += count_trails(x, y)
        total_2 += count_ratings(x, y)
    print(f"Part 1: {total_1}")
    print(f"Part 2: {total_2}")


part_12()
