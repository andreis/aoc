def solve_line(line, answer_size=2):
    line = line[::-1]

    answer = list(range(answer_size))
    for index in range(len(answer) - 1, -1, -1):
        hi = len(line) if index == answer_size - 1 else answer[index + 1]
        idx = hi - 1
        target = max(line[answer[index] : hi])
        while line[idx] != target:
            idx -= 1
        answer[index] = idx

    return int("".join(map(lambda x: str(line[x]), answer[::-1])))


with open("03.txt") as f:
    answer1 = answer2 = 0
    for line in f.readlines():
        line = list(map(int, line.strip()))
        answer1 += solve_line(line)
        answer2 += solve_line(line, 12)
    print(answer1, answer2)
