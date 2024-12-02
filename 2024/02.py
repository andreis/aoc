# https://adventofcode.com/2024/day/2


def is_safe(nums):
    if len(nums) == 1:
        return False
    if nums[0] == nums[1]:
        return False
    asc = bool(nums[0] < nums[1])
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            return False
        if asc and nums[i - 1] > nums[i] or not asc and nums[i - 1] < nums[i]:
            return False
        diff = abs(nums[i - 1] - nums[i])
        if diff < 1 or diff > 3:
            return False
    return True


def is_safe_ignore_one(nums):
    # we can optionally eliminate one number
    if len(nums) == 1:
        return False
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[i + 1 :]):
            return True
    return False


safe = 0
safe_ignore_one = 0
with open("02.input") as f:
    for line in f:
        nums = list(map(int, line.strip().split()))
        if is_safe(nums):
            safe += 1
        if is_safe_ignore_one(nums):
            safe_ignore_one += 1


print(f"safe: {safe}")
print(f"safe_ignore_one: {safe_ignore_one}")


print("== Test 1")
tests_1 = {
    "7 6 4 2 1": True,
    "1 2 7 8 9": False,
    "9 7 6 2 1": False,
    "1 3 2 4 5": False,
    "8 6 4 4 1": False,
    "1 3 6 7 9": True,
}
for vals, expected in tests_1.items():
    print(f"{vals}: {is_safe(list(map(int, vals.split())))} == {expected}")


print("== Test 2")
tests_2 = {
    "7 6 4 2 1": True,
    "1 2 7 8 9": False,
    "9 7 6 2 1": False,
    "1 3 2 4 5": True,
    "8 6 4 4 1": True,
    "1 3 6 7 9": True,
}
for vals, expected in tests_2.items():
    print(f"{vals}: {is_safe_ignore_one(list(map(int, vals.split())))} == {expected}")
