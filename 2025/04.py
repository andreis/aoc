from itertools import product

DEBUG = False

dirs = ((0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1))


def within_bounds(point, size):
    return all(0 <= p < s for p, s in zip(point, size))


def neighbours(point, grid):
    size = (len(grid), len(grid[0]))
    points = list()

    for dx, dy in dirs:
        nx, ny = point[0] + dx, point[1] + dy
        if not within_bounds((nx, ny), size):
            continue
        if grid[nx][ny] == "@":
            points.append((nx, ny))

    return points


def accessible(point, grid):
    return grid[point[0]][point[1]] == "@" and len(neighbours(point, grid)) < 4


def all_removable(grid):
    size = (len(grid), len(grid[0]))
    points = list()

    for i, j in product(*map(range, size)):
        if accessible((i, j), grid):
            points.append((i, j))

    return points


def cleanup(grid):
    total = 0

    while True:
        to_remove = all_removable(grid)
        if not to_remove:
            break
        total += len(to_remove)
        for i, j in to_remove:
            grid[i][j] = "."

    return total


with open("04.sample.txt" if DEBUG else "04.txt") as f:
    answer1 = answer2 = 0
    grid = list(map(list, map(str.strip, f.readlines())))
    answer1 = len(all_removable(grid))
    answer2 = cleanup(grid)
    print(answer1, answer2)
