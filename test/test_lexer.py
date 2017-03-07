import unittest
from subprocess import CalledProcessError, run, check_output


COMMAND = 'echo "{}" | bash src/lexer.sh'


def _check(cmd):
    return check_output(COMMAND.format(cmd), shell=True)


def _run(cmd):
    return run(COMMAND.format(cmd), shell=True, check=True)


class TestLexer(unittest.TestCase):
    """Basic test cases for lexer"""
    def test_valid_number(self):
        tokens = b'NAT 0123456789\nNAT 9876543210\n'
        self.assertEqual(_check('0123456789 9876543210'), tokens)

    def test_valid_operators(self):
        tokens = b'OPT +\nOPT -\nOPT *\nOPT /\n'
        self.assertEqual(_check('+ - * /'), tokens)

    def test_valid_expression(self):
        tokens = b'NAT 1\nOPT +\nNAT 22\nOPT *\nNAT 333\n'
        self.assertEqual(_check('1+22   *333'), tokens)

    def test_invalid_character(self):
        with self.assertRaises(CalledProcessError):
            _run('!')

    def test_invalid_operator(self):
        with self.assertRaises(CalledProcessError):
            _run('1++')
