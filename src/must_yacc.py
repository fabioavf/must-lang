# ---------------------------------------------------------------------------- #
#                               Análise Sintática                              #
# ---------------------------------------------------------------------------- #

import ply.yacc as yacc

from must_lex import tokens

precedence = (
    ('left', 'SUM', 'SUB'),
    ('left', 'MULT', 'DIV'),
)


def p_expr_operations(p):
    '''
    expr : expr SUM expr
         | expr SUB expr
         | expr MULT expr
         | expr DIV expr
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


# def p_expr_relationals(p):
#     '''
#     expr : expr '==' expr
#          | expr '!=' expr
#          | expr '>' expr
#          | expr '<' expr
#          | expr '>=' expr
#          | expr '<=' expr
#     '''

#     match p[2]:
#         case '==':
#             p[0] = p[1] == p[3]
#         case '!=':
#             p[0] = p[1] != p[3]
#         case '>':
#             p[0] = p[1] > p[3]
#         case '<':
#             p[0] = p[1] < p[3]
#         case '>=':
#             p[0] = p[1] >= p[3]
#         case '<=':
#             p[0] = p[1] <= p[3]


# def p_expr_logicals(p):
#     '''
#     expr : expr '&&' expr
#          | expr '||' expr
#          | '!' expr
#     '''

#     if p[1] == '!':
#         p[0] = not p[2]

#     match p[2]:
#         case '&&':
#             p[0] = p[1] and p[3]
#         case '||':
#             p[0] = p[1] or p[3]


# def p_expr_attr(p):
#     '''
#     attr : VAR '=' LIT_INT
#          | VAR '=' LIT_FLOAT
#          | VAR '=' LIT_CHAR
#          | VAR '=' VAR
#     '''


def p_expr_term(p):
    'expr : term'
    p[0] = p[1]


def p_term_literal_int(p):
    'term : LIT_INT'
    p[0] = p[1]


def p_term_literal_float(p):
    'term : LIT_FLOAT'
    p[0] = p[1]


def p_term_literal_char(p):
    'term : LIT_CHAR'
    p[0] = p[1]


def p_term_literal_var(p):
    'term : VAR'
    p[0] = p[1]


def p_error(t):
    print("Syntax error at '%s'" % t.value)


parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
