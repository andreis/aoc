with open("01.txt") as f:
  answer1 = answer2 = 0
  cur = 50
  for line in f.readlines():
    sign = -1 if line.startswith("L") else 1
    dist = int(line[1:])
    n_turns = dist // 100
    dist = dist % 100
    prev = cur
    cur += sign * dist
    answer2 += n_turns + (int(cur < 1 or cur > 99) if prev != 0 else 0)
    cur = (cur + 100) % 100
    if cur == 0:
      answer1 += 1
print(answer1, answer2)