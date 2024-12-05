import inspect
import os
import re

debug = bool(os.getenv("DEBUG"))
testing = bool(os.getenv("TEST"))


def get_caller_filename():
    for frame_info in inspect.stack():
        filename = frame_info.filename
        if re.search(r"\d+\.py$", filename):
            return filename
    raise Exception("Could not find caller filename")


def dprint(msg):
    if debug:
        print(msg)


def read_input():
    ext = ".test" if bool(os.getenv("TEST")) else ".input"
    with open(get_caller_filename().replace(".py", ext)) as f:
        for line in f:
            yield line.strip()
    return
