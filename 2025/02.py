import concurrent.futures
import os
import sys
import threading
import time

# Turns out single-threaded is 10x faster lmao
USE_THREADING = False


def is_silly(n):
  str_n = str(n)
  if len(str_n) & 1:
    return False
  return str_n[:len(str_n)//2] == str_n[len(str_n)//2:]

def is_very_silly(n):
  str_n = str(n)
  for repeat_size in range(1, len(str_n)//2 + 1):
    if len(str_n) % repeat_size != 0:
      continue
    pattern = str_n[:repeat_size]
    found = True
    for i in range(repeat_size, len(str_n), repeat_size):
      if str_n[i:i+repeat_size] != pattern:
        found = False
        break
    if found:
      return True
  return False

def check_very_silly_single_threaded(all_numbers):
  results = []
  total = len(all_numbers)
  for idx, n in enumerate(all_numbers):
    results.append(is_very_silly(n))
    if (idx + 1) % max(1, total // 100) == 0:
      percent = (idx + 1) / total * 100
      sys.stdout.write(f"\rChecking is_very_silly: {idx+1}/{total} ({percent:5.1f}%)")
      sys.stdout.flush()
  sys.stdout.write("\n")
  return results

def check_very_silly_multi_threaded(all_numbers):
  total_numbers = len(all_numbers)

  # Progress indicator setup
  progress = [0]
  lock = threading.Lock()
  def update_progress():
    while True:
      with lock:
        done = progress[0]
      percent = done / total_numbers * 100
      sys.stdout.write(f"\rChecking is_very_silly: {done}/{total_numbers} ({percent:5.1f}%)")
      sys.stdout.flush()
      if done >= total_numbers:
        break
      time.sleep(0.2)
    sys.stdout.write("\n")

  progress_thread = threading.Thread(target=update_progress)
  progress_thread.daemon = True
  progress_thread.start()

  cpu_count = os.cpu_count() or 4

  is_very_silly_results = [None] * total_numbers
  def is_very_silly_with_index(args):
    idx, n = args
    result = is_very_silly(n)
    with lock:
      progress[0] += 1
    return idx, result

  with concurrent.futures.ThreadPoolExecutor(max_workers=cpu_count) as executor:
    for idx, result in executor.map(is_very_silly_with_index, enumerate(all_numbers)):
      is_very_silly_results[idx] = result

  progress_thread.join()
  return is_very_silly_results

def check_very_silly(all_numbers, use_threading=None):
  if use_threading is None:
    use_threading = USE_THREADING

  if use_threading:
    return check_very_silly_multi_threaded(all_numbers)
  else:
    return check_very_silly_single_threaded(all_numbers)

def iterate_range(str_range):
  start, end = str_range.split("-")
  for i in range(int(start), int(end) + 1):
    yield i

with open("02.txt") as f:
  all_numbers = [n for str_range in f.readlines()[0].strip().split(",") for n in iterate_range(str_range)]

  start_time = time.time()
  is_silly_results = [is_silly(n) for n in all_numbers]
  part1_time = time.time() - start_time

  start_time = time.time()
  mode = "multi-threaded" if USE_THREADING else "single-threaded"
  print(f"Part 2: Running in {mode} mode...")
  is_very_silly_results = check_very_silly(all_numbers)
  part2_time = time.time() - start_time

  answer1 = sum(n for n, silly in zip(all_numbers, is_silly_results) if silly)
  answer2 = sum(n for n, very_silly in zip(all_numbers, is_very_silly_results) if very_silly)

  print(f"\nPart 1 time: {part1_time:.2f}s")
  print(f"Part 2 time: {part2_time:.2f}s ({mode})")
  print(f"\nAnswers: {answer1} {answer2}")