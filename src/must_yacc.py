
# ---------------------------------------------------------------------------- #
#                               Análise Sintática                              #
# ---------------------------------------------------------------------------- #

import ply.yacc as yacc

from must_lex import tokens

precedence = (
    ('left', 'SUM', 'SUB'),
    ('left', 'MULT', 'DIV'),
    ('left', 'AND', 'OR'),
    ('right', 'NOT')
)


def p_expr_operations(p):
    '''
    expr : expr SUM expr
         | expr SUB expr
         | expr MULT factor
         | expr DIV factor
         | expr MOD expr
    '''

    match p[2]:
        case '+':
            p[0] = p[1] + p[3]
        case '-':
            p[0] = p[1] - p[3]
        case '*':
            p[0] = p[1] * p[3]
        case '/':
            p[0] = p[1] / p[3]
        case '%':
            p[0] = p[1] % p[3]


def p_expr_relationals(p):
    '''
    expr : expr EQUALS expr
         | expr NOT_EQUALS expr
         | expr GREATER expr
         | expr SMALLER expr
         | expr GREATER_EQUALS expr
         | expr SMALLER_EQUALS expr
    '''

    match p[2]:
        case '==':
            p[0] = p[1] == p[3]
        case '!=':
            p[0] = p[1] != p[3]
        case '>':
            p[0] = p[1] > p[3]
        case '<':
            p[0] = p[1] < p[3]
        case '>=':
            p[0] = p[1] >= p[3]
        case '<=':
            p[0] = p[1] <= p[3]


def p_expr_logicals(p):
    '''
    expr : expr AND expr
         | expr OR expr
         | NOT expr
    '''

    if p[1] == '!':
        p[0] = not p[2]

    match p[2]:
        case '&&':
            p[0] = p[1] and p[3]
        case '||':
            p[0] = p[1] or p[3]


def p_decl(p):
    '''
    term : LET VAR COLON INT
         | LET VAR COLON FLOAT
         | LET VAR COLON CHAR
         | LET VAR COLON INT ATTR LIT_INT
         | LET VAR COLON FLOAT ATTR LIT_FLOAT
         | LET VAR COLON CHAR ATTR LIT_CHAR
    '''

    if len(p) == 5:
        for i in p:
            print(i)
    elif len(p) == 7:
        inputString = p[2] + '=' + p[4] + '(' + p[6] + ')'
        print(inputString)
        eval(inputString)


def p_expr_term(p):
    'expr : term'

    p[0] = p[1]


def p_main(p):
    'term : MAIN BLOCK_START expr BLOCK_END'


def p_term_literal_int(p):
    'factor : LIT_INT'
    p[0] = int(p[1])


def p_term_literal_float(p):
    'factor : LIT_FLOAT'
    p[0] = float(p[1])


def p_term_literal_char(p):
    'term : LIT_CHAR'
    p[0] = p[1][1]


def p_term_literal_var(p):
    'term : VAR'
    p[0] = p[1]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_expr_factor(p):
    'factor : PAR_START expr PAR_END'
    p[0] = p[2]


def p_output(p):
    'term : OUTPUT PAR_START expr PAR_END'

    print(eval(p[3]))


def p_line(p):
    '''
    term : term SEMICOLON
    term : term SEMICOLON term
    '''


def p_error(t):
    print("Syntax error at '%s'" % t.value)


parser = yacc.yacc()

print('\n----- fim codigo -----\n')

data = '''
main {
    let minhavariavel: float = 0.3;
    output(minhavariavel);
}
'''

print('ENTRADA: ', data)


print('\n\nSAIDA: ')

parser.parse(data)

# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)
