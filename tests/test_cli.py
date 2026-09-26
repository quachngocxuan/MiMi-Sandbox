import subprocess
import sys
import unittest


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "mimi_demo", *args], capture_output=True, text=True, timeout=30
    )


class CliTest(unittest.TestCase):
    def test_wordcount(self):
        r = run("wordcount", "MiMi giao việc")
        self.assertEqual((r.returncode, r.stdout.strip()), (0, "3"))

    def test_slugify(self):
        r = run("slugify", "Hello MiMi World")
        self.assertEqual((r.returncode, r.stdout.strip()), (0, "hello-mimi-world"))

    def test_leap(self):
        self.assertEqual(run("leap", "1900").stdout.strip(), "no")
        self.assertEqual(run("leap", "2024").stdout.strip(), "yes")

    def test_unknown_command_fails(self):
        r = run("nope")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("usage", (r.stderr + r.stdout).lower())
