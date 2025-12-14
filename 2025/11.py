from functools import cache


def paths(graph, start, end):
    @cache
    def dfs(current):
        if current == end:
            return 1
        if current not in graph:
            return 0
        return sum(map(dfs, graph[current]))

    return dfs(start)


def part1(graph):
    return paths(graph, "you", "out")


def part2(graph):
    if paths(graph, "dac", "fft"):
        return paths(graph, "svr", "dac") * paths(graph, "dac", "fft") * paths(graph, "fft", "out")
    return paths(graph, "svr", "fft") * paths(graph, "fft", "dac") * paths(graph, "dac", "out")


graph = {a: set(b.split()) for a, b in (l.split(": ") for l in open("11.txt").read().splitlines())}
print(part1(graph), part2(graph))
