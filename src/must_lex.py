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

#entrada de teste para output de string comum
data0 = '''
    main {
        output("Hello");
        output("World");
    }
'''

#entrada de teste para decl attr e output de variavel inteiras
data1 = '''
main {
    let variavel_int: int;
    variavel_int = 3;
    output(variavel_int);
    const constante_int: int = 2;
    output(constante_int);
    let variavel_int2: int = 5;
    output(variavel_int2);
}
'''

#entrada de teste para decl attr e output de variavel float
data2 = '''
main {
    let variavel_float: float;
    variavel_float = 3;
    output(variavel_float);
    const constante_float: float = 2.0;
    output(constante_float);
    let variavel_float2: float;
    input(variavel_float2);
    output(variavel_float2);
}
'''

#entrada de teste para decl attr e output de variavel char
data3 = '''
main {
    let variavel_char: char;
    variavel_char = '3';
    output(variavel_char);
    const constante_char: char = 'a';
    output(constante_char);
    let variavel_char2: char;
    input(variavel_char2);
    output(variavel_char2);
}
'''

#entrada de teste para attr com operacao aritmetica
data4 = '''
main {
    let variavel_int: int;
    variavel_int = 3 + 4;
    output(variavel_int);
    let variavel_int2: int;
    variavel_int2 = (variavel_int * 4) + 3;
    output(variavel_int2);
}
'''

#entrada de teste para cond logical e relacional verdadeiro
data5 = '''
main {
    let variavel_int: int;
    variavel_int = 3 + 4;
    let variavel_char: char;
    variavel_char = '3';
    if(variavel_int == 7 && variavel_char == '3'){
        variavel_int = variavel_int - 7;
        output(variavel_int);
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

#entrada de teste para cond logical e relacional falso com else
data6 = '''
main {
    let variavel_int: int;
    variavel_int = 3 + 4;
    let variavel_char: char;
    variavel_char = '3';
    if(variavel_int == 7 && variavel_char == '2'){
        variavel_int = variavel_int - 7;
        output(variavel_int);
    }else{
        output(variavel_char);
    }
}
'''

#entrada de teste para while
data7 = '''
main {
    let variavel_int: int;
    variavel_int =3;
    while(variavel_int > 0 ){
        output(variavel_int);
        variavel_int = variavel_int - 1;
    }
}
'''

#entrada de teste para for
data8 = '''
main {
    let variavel_int: int;
    variavel_int = 3;
    for(i=3; i>0; i=i-1){
        output(variavel_int);
        variavel_int = variavel_int - 1;
    }
}
'''
# data1 = '''
# main {
#     let variavel_char: char = '5';
#     output(variavel_char);
#     const PI: float = 3.14;
#     output(PI);
#     output("texto");
#     let variavel_apenas_declarada: char;
#     variavel_apenas_declarada = '4';
#     output(variavel_apenas_declarada);
#     let variavel_atribuida_por_input: int;
#     input(variavel_atribuida_por_input);
#     output(variavel_atribuida_por_input);
# }
# '''

# data2 = '''
# main {
#     let variavel: int = 5;
#     if(variavel == 5){
#         variavel = 3 + 4;
#         output(variavel)
#     }
# }
# '''
# data3 = '''
# main {
#     let variavel: int = 5;
#     while(variavel == 5){
#         variavel = 3 + 4;
#         output(variavel)
#     }
# }
# '''

lexer.input(data8)

while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
