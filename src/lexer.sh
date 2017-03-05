#   Lexer
#   =====
#
#   Tokenize the flow of bytes by creating an array of specialized strings as
#   tokens, in spite of reordering them by the syntax.
#
#   Note: Use printf '%s\n' "${tokens[@]}" to print the elements of tokens array
#   separated by newlines.

row=1
col=0

tokens=()
buf=""

# Error messages.
INVALID_SYNTAX="invalid syntax"

function append_token() {
    if [[ "$buf" != "" ]]; then
        tokens+=("$buf")
        buf=""
    fi
}

while IFS= read -N 1 c; do
    ((col++))
    case "$c" in
        $'\n')
            ((row++))
            ((col=0))
            append_token
            ;;
        $' ')
            append_token
            ;;
        [_a-z0-9] )
            buf="$buf$c"
            ;;
        *)
            echo "$row:$col "$INVALID_SYNTAX" \"$c\""
            exit 1
            ;;
    esac
done <&0
