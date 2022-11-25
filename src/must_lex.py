# ---------------------------------------------------------------------------- #
#                                Análise Léxica                                #
# ---------------------------------------------------------------------------- #

import ply.lex as lex

# tokens das palavras reservadas
reserved = {
    'main': 'MAIN',
    'input': 'INPUT',
    'output': 'OUTPUT',
    'while': 'WHILE',
    'for': 'FOR',
    'else': 'ELSE',
    'if': 'IF',
    'let': 'LET',
    'const': 'CONST',
    'int': 'INT',
    'char': 'CHAR',
    'float': 'FLOAT'
}

# lista dos tokens
tokens = [
    # 'MAIN_START',
    'SEMICOLON',
    'SUM',
    'SUB',
    'MULT',
    'DIV',
    'MOD',
    'ATTR',
    'COLON',
    'BLOCK_START',
    'BLOCK_END',
    'PAR_START',
    'PAR_END',
    'VAR',
    'SEPARATOR',
    'LIT_INT',
    'LIT_FLOAT',
    'LIT_CHAR',
    'AND',
    'OR',
    'NOT',
    'EQUALS',
    'NOT_EQUALS',
    'GREATER',
    'SMALLER',
    'GREATER_EQUALS',
    'SMALLER_EQUALS',
    'ASP'

] + list(reserved.values())

# regex para os tokens
# t_MAIN_START = r'main'
t_SEMICOLON = r';'
t_SUM = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_ATTR = r'='
t_COLON = r':'
t_BLOCK_START = r'{'
t_BLOCK_END = r'}'
t_PAR_START = r'\('
t_PAR_END = r'\)'
t_SEPARATOR = r','
t_LIT_INT = r'-?\d+'
t_LIT_FLOAT = r'-?\d+.\d+'
t_LIT_CHAR = r"'\w'"
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_GREATER = r'>'
t_SMALLER = r'<'
t_GREATER_EQUALS = r'>='
t_SMALLER_EQUALS = r'<='
t_ASP = r'"'


def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VAR')

    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# constroi o analisador lexico
lexer = lex.lex()

data1 = '''
main {
    let variavel_char: char = '5';
    output(variavel_char);
    const PI: float = 3.14;
    output(PI);
    output("texto");
    let variavel_apenas_declarada: char;
    variavel_apenas_declarada = '4';
    output(variavel_apenas_declarada);
    let variavel_atribuida_por_input: int;
    input(variavel_atribuida_por_input);
    output(variavel_atribuida_por_input);
}
'''

data2 = '''
main {
    let variavel: int = 4;

    if(variavel == 4) {
        variavel = 3;
        output(variavel);
    } else {
        variavel = 9;
        output(variavel);
    }
}
'''


lexer.input(data2)

while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
