from unittest import TestCase
from unittest.mock import patch
from src.main import get_number


class TestGetFirstNumber(TestCase):

    @patch("builtins.input", return_value="1")
    def test_not_a_number(self, input):
        self.assertEqual(get_number(), 1)
