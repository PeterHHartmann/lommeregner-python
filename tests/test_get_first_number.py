import unittest
from src.main import get_number, parse_number_input


class TestGetFirstNumber(unittest.TestCase):

    def test_not_a_number(self):
        self.assertEqual(parse_number_input("1"), 1)
