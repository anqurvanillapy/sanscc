#   Lexer
#   =====
#
#   Tokenize the flow of bytes by creating an array of specialized strings as
#   tokens, in spite of reordering them by the syntax.

while IFS= read -N 1 c; do
    token=""
    case "$c" in
        $' ' | $'\n')
            echo "skip!"
            ;;
        [a-z0-9])
            echo "yes!"
            ;;
        *)
            echo "no!"
            ;;
    esac
done <&0
