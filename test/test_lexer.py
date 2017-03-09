import unittest
from .util import *


class TestLexer(unittest.TestCase):
    """Basic test cases for lexer"""
    def test_valid_number(self):
        tokens = b'NAT 0123456789\nNAT 9876543210\n'
        self.assertEqual(check_token('0123456789 9876543210'), tokens)

    def test_valid_operators(self):
        tokens = b'OPT +\nOPT -\nOPT *\nOPT /\n'
        self.assertEqual(check_token('+ - * /'), tokens)

    def test_valid_expression(self):
        tokens = b'NAT 1\nOPT +\nNAT 22\nOPT *\nNAT 333\n'
        self.assertEqual(check_token('1+22   *333'), tokens)

    def test_invalid_character(self):
        with self.assertRaises(CalledProcessError):
            run_token('!')

    def test_invalid_operator(self):
        with self.assertRaises(CalledProcessError):
            run_token('1++')
