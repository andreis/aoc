from functools import cache, reduce
from os import environ


lines = open("07.sample.txt" if environ.get("DEBUG") else "07.txt").read().splitlines()


def part1(lines):
    def step(state, line):  # reducer a bit forced lol
        beams, ans = state
        hits = [i for i, c in enumerate(line) if c == "^" and beams[i]]
        new_beams = beams[:]

        for i in hits:
            new_beams[i] = False
            new_beams[i - 1] = new_beams[i + 1] = True

        return new_beams, ans + len(hits)

    return reduce(step, lines, ([c == "S" for c in lines[0]], 0))[1]


def part2(lines):
    splitter_rows = [line for line in lines if "^" in line]

    @cache
    def dfs(x, c):
        if x == len(splitter_rows):
            return 1
        if not (0 <= c < len(lines[0])):
            return 0
        if splitter_rows[x][c] == "^":
            return dfs(x + 1, c - 1) + dfs(x + 1, c + 1)
        return dfs(x + 1, c)

    return dfs(0, lines[0].index("S"))


print(part1(lines))
print(part2(lines))
