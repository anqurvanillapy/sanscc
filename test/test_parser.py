import unittest
from .util import *


class TestParser(unittest.TestCase):
    """Basic test cases for parser"""
    def test_valid_expression(self):
        postfix = b'1 2 + 3 / \n'
        self.assertEqual(check_parse('1+ 2 /3  '), postfix)

    def test_invalid_expression(self):
        with self.assertRaises(CalledProcessError):
            run_parse('+ 1')
