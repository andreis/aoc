from util import read_input
from itertools import product

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))


def get_regions(grid):
    n, m = len(grid), len(grid[0])
    regions = []
    visited = set()

    for i, j in product(range(n), range(m)):
        if (i, j) in visited:
            continue

        region = set()
        queue = [(i, j)]
        while queue:
            x, y = queue.pop()
            region.add((x, y))
            visited.add((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and (nx, ny) not in visited
                    and grid[nx][ny] == grid[i][j]
                ):
                    queue.append((nx, ny))
        regions.append(region)

    return regions


def external_edges(grid, i, j):
    n, m = len(grid), len(grid[0])
    res = list()
    for dx, dy in dirs:
        nx, ny = i + dx, j + dy
        if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny] != grid[i][j]:
            res.append(((i, j), (nx, ny)))
    return res


def perimeter(grid, region):
    return sum(len(external_edges(grid, x, y)) for x, y in region)


def adjusted_perimeter(grid, region):
    edges = set()
    for x, y in region:
        for edge in external_edges(grid, x, y):
            edges.add(edge)

    sides = 0
    while edges:
        start = edges.pop()
        edges.add(start)
        queue = [start]
        sides += 1
        while queue:
            cur = queue.pop()
            edges.remove(cur)
            l, r = edge_translate(cur), edge_translate(cur, -1)
            if l in edges:
                queue.append(l)
            if r in edges:
                queue.append(r)
    return sides


# (inside - outside) delta : direction
_edge_types = {
    (1, 0): 0,  # North
    (0, -1): 1,  # East
    (-1, 0): 2,  # South
    (0, 1): 3,  # West
}


def edge_dir(edge):
    return _edge_types[(edge[0][0] - edge[1][0], edge[0][1] - edge[1][1])]


# how we need to shift an edge to maintain orientation
_edge_trans = {
    0: (0, 1),  # North edges go East
    1: (1, 0),  # East edges go South
    2: (0, -1),  # South edges go West
    3: (-1, 0),  # West edges go North
}


def edge_translate(edge, sign=1):
    dir = edge_dir(edge)
    return (
        (
            edge[0][0] + sign * _edge_trans[dir][0],
            edge[0][1] + sign * _edge_trans[dir][1],
        ),
        (
            edge[1][0] + sign * _edge_trans[dir][0],
            edge[1][1] + sign * _edge_trans[dir][1],
        ),
    )


# direction : (inside - outside) delta
_edge_rot = {
    0: (-1, 0),  # North
    1: (0, 1),  # East
    2: (1, 0),  # South
    3: (0, -1),  # West
}


# not used anymore, had a different solution that walked the boundaries of each region
def edge_rotate(edge):
    dir = (edge_dir(edge) + 1) & 3
    return (edge[0], (edge[0][0] + _edge_rot[dir][0], edge[0][1] + _edge_rot[dir][1]))


def part_1():
    grid = list(read_input())
    regions = get_regions(grid)
    return sum(perimeter(grid, region) * len(region) for region in regions)


def part_2():
    grid = list(read_input())
    regions = get_regions(grid)
    return sum(adjusted_perimeter(grid, region) * len(region) for region in regions)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
