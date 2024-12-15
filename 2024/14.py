from util import read_input
from collections import Counter
from itertools import product
import os
from time import sleep
from PIL import Image

n = 101
m = 103


def parse_line(line):
    p_str, v_str = line.split(" ")
    p = tuple(map(int, p_str.split("=")[1].split(",")))
    v = tuple(map(int, v_str.split("=")[1].split(",")))
    return p, v


def get_position(p, v, steps):
    x, y = p
    dx, dy = v

    return (x + dx * steps) % n, (y + dy * steps) % m


def get_quadrant(pos):
    if pos[0] == 50 or pos[1] == 51:
        # assigned to special, ignored bucket
        return "N/A"
    return (int(pos[0] < 50), int(pos[1] < 51))


def gen_image(robots, iteration):
    filename = f"robots/{iteration:04d}.png"
    img = Image.new("1", (n, m), color=1)
    pixels = img.load()
    for p, v in robots:
        pos = get_position(p, v, iteration)
        if 0 <= pos[0] < n and 0 <= pos[1] < m:
            pixels[pos[0], pos[1]] = 0
    img.save(filename)


def part_1():
    quadrants = Counter()
    for line in read_input():
        p, v = parse_line(line)
        pos = get_position(p, v, 100)
        quadrants[get_quadrant(pos)] += 1
    res = 1
    for x, y in product(range(2), range(2)):
        res *= quadrants[(x, y)]
    return res


def part_2():
    robots = list(parse_line(line) for line in read_input())
    os.makedirs("robots", exist_ok=True)
    for iteration in range(10000):
        gen_image(robots, iteration)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
