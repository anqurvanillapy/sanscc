#   Parser
#   ======
#
#   A very simple predictive parser, for syntax-directed translation.

# Lookahead symbol.
lookahead=""

# The output in postfix notation.
postfix=""

# Error messages.
INVALID_SYNTAX="invalid syntax"

function eat() {
    local t="$1"
    if [[ "$t" == "$lookahead" ]]; then
        read lookahead
    else
        echo "$INVALID_SYNTAX"
        exit 1
    fi
}

function _expr() {
    _term
    while true; do
        # Read the lookahead symbol into an array, for text spliting.
        local token_t
        read -a token_t <<< "$lookahead"
        if [[ "${token_t[0]}" == "OPT" ]]; then
            eat "$lookahead"
            _term
            postfix="$postfix${token_t[1]} "
        else
            return
        fi
    done
}

function _term() {
    local token_t
    read -a token_t <<< "$lookahead"
    if [[ "${token_t[0]}" == "NAT" ]]; then
        postfix="$postfix${token_t[1]} "
        eat "$lookahead"
    else
        echo "$INVALID_SYNTAX"
        exit 1
    fi
}

read lookahead
_expr
echo "$postfix"
