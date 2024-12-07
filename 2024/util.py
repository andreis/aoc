import inspect
from itertools import tee
import os
import re
from types import GeneratorType

import unittest
from unittest.mock import patch, mock_open

# -- Env flags --

debug = bool(os.getenv("DEBUG"))
testing = bool(os.getenv("TEST"))


# -- Helper functions --


def get_caller_filename():
    for frame_info in inspect.stack():
        filename = frame_info.filename
        if re.search(r"\d+\.py$", filename):
            return filename
    raise Exception("Could not find caller filename")


def dprint(msg):
    if debug:
        print(msg)


Tee = tee([], 1)[0].__class__


def memoized(f):
    cache = {}

    def ret(*args):
        if args not in cache:
            cache[args] = f(*args)
        if isinstance(cache[args], (GeneratorType, Tee)):
            cache[args], r = tee(cache[args])
            return r
        return cache[args]

    return ret


@memoized
def read_input():
    ext = ".test" if bool(os.getenv("TEST")) else ".input"
    with open(get_caller_filename().replace(".py", ext)) as f:
        for line in f:
            yield line.strip()
    return


# -- Unit tests --


class MemoizationTest(unittest.TestCase):
    @patch.dict(os.environ, {"TEST": "1"})
    @patch("builtins.open", new_callable=mock_open, read_data="line1\nline2\nline3")
    @patch("__main__.get_caller_filename")
    def test_read_input_memoized(self, mock_get_caller_filename, mock_file):
        mock_get_caller_filename.return_value = "test_file.py"

        # First call should open the file
        list(read_input())
        mock_file.assert_called_once_with("test_file.test")

        # Second call should NOT open the file again
        list(read_input())
        mock_file.assert_called_once_with("test_file.test")  # Still only called once


if __name__ == "__main__":
    unittest.main()
