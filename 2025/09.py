from itertools import combinations, product
from os import environ


def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def part1(points):
    return max(area(a, b) for a, b in product(points, points))


def part2(points):
    best = 0
    edges = list(zip(points, points[1:] + points[:1]))

    for u, v in combinations(points, 2):
        if area(u, v) <= best:
            continue

        x1, x2 = sorted((u[0], v[0]))
        y1, y2 = sorted((u[1], v[1]))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2

        if not sum((ey1 > my) != (ey2 > my) and ex1 > mx for (ex1, ey1), (ex2, ey2) in edges) % 2:
            continue

        if not any(
            (x1 < ex1 < x2 if ex1 == ex2 else max(x1, min(ex1, ex2)) < min(x2, max(ex1, ex2)))
            and (y1 < ey1 < y2 if ey1 == ey2 else max(y1, min(ey1, ey2)) < min(y2, max(ey1, ey2)))
            for (ex1, ey1), (ex2, ey2) in edges
        ):
            best = area(u, v)

    return best


lines = open("09.sample.txt" if environ.get("DEBUG") else "09.txt").read().splitlines()
points = [tuple(map(int, line.split(","))) for line in lines]
print(part1(points))
print(part2(points))
