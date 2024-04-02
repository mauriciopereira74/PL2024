import sys
import ply.lex as lex

states = (
    ('on', 'inclusive'),
    ('off', 'inclusive')
)

tokens = ('ON', 'OFF', 'NUMBER', 'EQUALS')

t_ignore = ' \t\n'

def t_ON(t):
    r'on'
    t.lexer.begin('on')
    return t

def t_OFF(t):
    r'off'
    t.lexer.begin('off')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_EQUALS(t):
    r'='
    return t

def t_on_NUMBER(t):
    r'\d+'
    t.lexer.total_on += int(t.value)
    return t

def t_off_NUMBER(t):
    r'\d+'
    t.lexer.total_off = 0
    return t

def t_on_EQUALS(t):
    r'='
    print(f"'=': {t.lexer.total_on}")

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python somador.py <file_path>")
        return

    file_path = sys.argv[1]
    
    lexer = lex.lex()
    lexer.total_on = 0
    lexer.total_off = 0

    with open(file_path, 'r') as file:
        lexer.input(file.read())

        for token in lexer:
            pass

if __name__ == "__main__":
    main()
