# https://adventofcode.com/2024/day/1

first, second = list(), list()
with open("01.input") as f:
    for line in f:
        l, r = line.strip().split()
        first.append(int(l))
        second.append(int(r))

print(sum(map(lambda t: abs(t[0] - t[1]), zip(sorted(first), sorted(second)))))

from collections import Counter

cl, cr = Counter(first), Counter(second)

print(sum(item * cr.get(item, 0) for item in cl))
