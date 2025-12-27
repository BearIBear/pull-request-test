import unittest
from io import StringIO
import sys
from bear import print_bear

class TestBear(unittest.TestCase):
    def test_print_bear(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        print_bear("Test Message")
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Test Message", output)
        self.assertIn("__", output)

if __name__ == '__main__':
    unittest.main()
