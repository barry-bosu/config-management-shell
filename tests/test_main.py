import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from main import expand_environment_variables

class TestShellEmulator(unittest.TestCase):

    def test_expand_home_variable(self):
        os.environ["HOME"] = "test_home"
        result = expand_environment_variables("$HOME")
        self.assertEqual(result, "test_home")

    def test_expand_variable_inside_text(self):
        os.environ["TEST_VAR"] = "value"
        result = expand_environment_variables("path_$TEST_VAR")
        self.assertEqual(result, "path_value")

    def test_text_without_variable(self):
        result = expand_environment_variables("hello")
        self.assertEqual(result, "hello")


if __name__ == "__main__":
    unittest.main()