from subprocess import CalledProcessError, run, check_output


COMMAND_LEXER = 'echo "{}" | bash src/lexer.sh'
COMMAND_PARSER = 'echo "{}" | bash src/lexer.sh | bash src/parser.sh'


def _check(expr, cmd):
    return check_output(cmd.format(expr), shell=True)


def check_token(expr):
    return _check(expr, COMMAND_LEXER)


def check_parse(expr):
    return _check(expr, COMMAND_PARSER)


def _run(expr, cmd):
    return run(cmd.format(expr), shell=True, check=True)


def run_token(expr):
    return _run(expr, COMMAND_LEXER)


def run_parse(expr):
    return _run(expr, COMMAND_PARSER)
