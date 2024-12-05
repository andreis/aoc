from util import *

first, second = list(), list()
for line in read_input():
    l, r = line.split()
    first.append(int(l))
    second.append(int(r))

print(sum(map(lambda t: abs(t[0] - t[1]), zip(sorted(first), sorted(second)))))

from collections import Counter

cl, cr = Counter(first), Counter(second)

print(sum(item * cr.get(item, 0) for item in cl))
