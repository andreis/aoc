from util import *
from collections import defaultdict
from graphlib import TopologicalSorter


def check_line(fwd, line):
    seen_at = dict()
    for i, number in enumerate(line):
        seen_at[number] = i
    for i, number in enumerate(line):
        if number not in fwd:
            continue
        for check in (number for number in fwd[number] if number in seen_at):
            if i > seen_at[check]:
                return False
    return True


def process_input():
    lines = list(read_input())
    idx = -1
    for i in range(len(lines)):
        if not lines[i]:
            idx = i
            break

    if idx == -1:
        raise Exception("No empty line found")

    rules, updates = lines[:idx], lines[idx + 1 :]

    fwd = defaultdict(list)
    for rule in rules:
        l, r = rule.split("|")
        fwd[int(l)].append(int(r))

    correct, incorrect = list(), list()
    for update in map(lambda u: u.split(","), updates):
        numbers = list(map(int, update))
        (correct if check_line(fwd, numbers) else incorrect).append(numbers)

    return fwd, correct, incorrect


def part_1():
    _, correct, _ = process_input()
    print(f"Part 1: {sum(line[len(line)//2] for line in correct)}")


def part_2():
    fwd, _, incorrect = process_input()
    total = 0

    for i, line in enumerate(incorrect):
        dprint(f"Processing line {i+1} out of {len(incorrect)}")
        exists = set(line)
        sorter = TopologicalSorter()

        for k, v in fwd.items():
            for number in v:
                if k not in exists or number not in exists:
                    continue
                sorter.add(k, number)

        order = list(number for number in sorter.static_order() if number in exists)
        total += order[len(order) // 2]

    print(f"Part 2: {total}")


part_1()
part_2()
