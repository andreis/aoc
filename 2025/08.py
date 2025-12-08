from itertools import product
from os import environ


def node_dist(pair):
    return sum((x - y) ** 2 for x, y in zip(*pair)) ** 0.5


def find(p, n):
    while n != p[n]:
        p[n] = p[p[n]]
        n = p[n]
    return n


def part1(nodes, n_closest=10):
    edges = sorted((p for p in product(nodes, nodes) if p[0] < p[1]), key=node_dist)
    p, s = {n: n for n in nodes}, {n: 1 for n in nodes}

    for u, v in edges[:n_closest]:
        if (r1 := find(p, u)) != (r2 := find(p, v)):
            p[r2] = r1
            s[r1] += s[r2]
            s[r2] = 0

    return (S := sorted(s.values()))[-1] * S[-2] * S[-3]


def part2(nodes):
    edges = sorted((p for p in product(nodes, nodes) if p[0] < p[1]), key=node_dist)
    p, clusters = {n: n for n in nodes}, len(nodes)

    for u, v in edges:
        if (r1 := find(p, u)) != (r2 := find(p, v)):
            p[r2] = r1
            if (clusters := clusters - 1) == 1:
                return u[0] * v[0]


lines = open("08.sample.txt" if environ.get("DEBUG") else "08.txt").read().splitlines()
nodes = [tuple(map(int, l.split(","))) for l in lines]

print(part1(nodes, 10 if environ.get("DEBUG") else 1000))
print(part2(nodes))
