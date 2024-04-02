import sys
import ply.lex as lex

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'IDENTIFIER',
    'NUMBER',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'GREATER',
    'LESS',
    'EQUALS',
    'COMMA',
)

t_ignore = ' \t\n'

def t_SELECT(t):
    r'SELECT'
    return t

def t_FROM(t):
    r'FROM'
    return t

def t_WHERE(t):
    r'WHERE'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_GREATER_EQUAL(t):
    r'>='
    return t

def t_LESS_EQUAL(t):
    r'<='
    return t

def t_GREATER(t):
    r'>'
    return t

def t_LESS(t):
    r'<'
    return t

def t_EQUALS(t):
    r'='
    return t

def t_COMMA(t):
    r','
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python query_lexer.py <query>")
        return

    query = sys.argv[1]
    lexer = lex.lex()

    lexer.input(query)

    for token in lexer:
        print(token)

if __name__ == "__main__":
    main()
