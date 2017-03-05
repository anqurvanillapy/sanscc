import unittest
from subprocess import CalledProcessError, run, check_output


COMMAND = 'echo "{}" | bash src/lexer.sh'


def _check(cmd):
    return check_output(COMMAND.format(cmd), shell=True)


def _run(cmd):
    return run(COMMAND.format(cmd), shell=True, check=True)


class TestLexer(unittest.TestCase):
    """Basic test cases for lexer"""
    def test_valid_expression(self):
        tokens = b'INT 1\nOPT +\nINT 22\nOPT *\nINT 333\n'
        self.assertEqual(_check('1+22 *333'), tokens)

    def test_invalid_expression(self):
        with self.assertRaises(CalledProcessError):
            _run('!')
