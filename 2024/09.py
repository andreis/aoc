from util import *

FILE = 0
BLANK = 1


def checksum(mem):
    return sum((mem[i] or 0) * i for i in range(len(mem)))


def build_mem():
    typ = BLANK
    fid = 0
    mem = list()
    for c in list(read_input())[0]:
        typ = typ ^ 1
        if typ == FILE:
            mem.extend([fid] * int(c))
            fid += 1
        else:
            mem.extend([None] * int(c))
    return mem


def compact_byte(mem):
    blank_idx = 0
    file_idx = len(mem) - 1
    while blank_idx < file_idx:
        if mem[blank_idx] is not None:
            blank_idx += 1
        elif mem[file_idx] is None:
            file_idx -= 1
        else:
            mem[blank_idx], mem[file_idx] = mem[file_idx], mem[blank_idx]
            blank_idx += 1
            file_idx -= 1


def compact_file(mem):
    file_idx = len(mem)
    last_fid = float("inf")
    biggest_blank = -1

    def scan_next_file():
        nonlocal file_idx, last_fid

        while file_idx == len(mem) or file_idx > 0 and mem[file_idx] is None:
            file_idx -= 1

        file_r = file_idx
        while file_idx > 0 and mem[file_idx] == mem[file_r]:
            file_idx -= 1

        file_l = file_idx + 1
        cur_fid = mem[file_l]
        if cur_fid > last_fid:
            return None
        last_fid = cur_fid
        return file_l, file_r + 1

    def scan_next_blank(min_len):
        nonlocal biggest_blank

        biggest_blank = 0
        mem_idx = 0
        found = None
        while mem_idx <= file_idx:
            if mem[mem_idx] is not None:
                mem_idx += 1
                continue
            mem_l = mem_idx
            while mem_idx <= file_idx and mem[mem_idx] is None:
                mem_idx += 1
            mem_r = mem_idx
            if mem_r - mem_l > biggest_blank:
                biggest_blank = mem_r - mem_l

            if mem_r - mem_l < min_len or found:
                continue
            found = mem_l, mem_r
        return found

    while file_idx > 0:
        found_file = scan_next_file()
        if not found_file:
            continue
        file_l, file_r = found_file
        if file_r - file_l > biggest_blank and biggest_blank != -1:
            continue
        found = scan_next_blank(file_r - file_l)
        if not found:
            continue
        mem[found[0] : found[0] + file_r - file_l] = mem[file_l:file_r]
        mem[file_l:file_r] = [None] * (file_r - file_l)


def part_1():
    mem = build_mem()
    compact_byte(mem)
    print(f"Part 1: {checksum(mem)}")


def part_2():
    mem = build_mem()
    compact_file(mem)
    print(f"Part 2: {checksum(mem)}")


part_1()
part_2()
