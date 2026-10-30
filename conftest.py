"""
Lets `pytest` run every lesson's Boot.dev-style main_test.py.

Every lesson has its own main.py, and every main_test.py does
`from main import ...`. If pytest imported them all into one interpreter,
Python would cache the first `main` module it saw and hand that same module
to every other lesson. So instead, each main_test.py runs in its own
subprocess from its own directory, exactly like `python main_test.py`.

    pytest                              # every lesson
    pytest ch03_big_o                   # one chapter
    pytest ch03_big_o/order_1           # one lesson
    pytest -k order_nm                  # lessons matching a name
"""

import subprocess
import sys

import pytest


class LessonFailed(Exception):
    pass


def pytest_collect_file(parent, file_path):
    if file_path.name == "main_test.py":
        return LessonFile.from_parent(parent, path=file_path)


class LessonFile(pytest.File):
    def collect(self):
        yield LessonItem.from_parent(self, name=self.path.parent.name)


class LessonItem(pytest.Item):
    def runtest(self):
        result = subprocess.run(
            [sys.executable, self.path.name],
            cwd=self.path.parent,
            capture_output=True,
            text=True,
            timeout=120,
        )
        output = result.stdout + result.stderr
        if result.returncode != 0 or "============= PASS" not in result.stdout:
            raise LessonFailed(output)

    def repr_failure(self, excinfo, style=None):
        if isinstance(excinfo.value, LessonFailed):
            return str(excinfo.value)
        return super().repr_failure(excinfo, style=style)

    def reportinfo(self):
        return self.path, None, f"{self.path.parent.name}/main_test.py"
