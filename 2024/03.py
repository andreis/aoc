from re import findall
from util import *


def process(text):
    total = 0
    for match in findall(r"mul\(\d{1,3},\d{1,3}\)", text):
        a, b = map(int, match[4:-1].split(","))
        total += a * b
    return total


def process_do_dont(text):
    total = 0
    dos = text.split("do()")
    for do in dos:
        sections = do.split("don't()")
        for match in findall(r"mul\(\d{1,3},\d{1,3}\)", sections[0]):
            a, b = map(int, match[4:-1].split(","))
            total += a * b
    return total


text = "".join(read_input())
print(f"Part 1: {process(text)}")
print(f"Part 2: {process_do_dont(text)}")
