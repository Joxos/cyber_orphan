import os
import subprocess
from utils.config import SRC_PATH


def get_all_py_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files


def format_and_fix(directory):
    py_files = get_all_py_files(directory)
    subprocess.run(["ruff", "check", "--fix", *py_files], check=True)
    subprocess.run(["ruff", "format", *py_files], check=True)


if __name__ == "__main__":
    format_and_fix(SRC_PATH)
