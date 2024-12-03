from re import findall


def process(text):
    total = 0
    for match in findall("mul\(\d{1,3},\d{1,3}\)", text):
        a, b = map(int, match[4:-1].split(","))
        total += a * b
    return total


def process_do_dont(text):
    total = 0
    dos = text.split("do()")
    for do in dos:
        sections = do.split("don't()")
        for match in findall("mul\(\d{1,3},\d{1,3}\)", sections[0]):
            a, b = map(int, match[4:-1].split(","))
            total += a * b
    return total


with open("03.input") as f:
    lines = f.readlines()
    text = "".join(map(lambda l: l.strip(), lines))
    print(process(text))
    print(process_do_dont(text))
