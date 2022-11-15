
# ---------------------------------------------------------------------------- #
#                               Análise Sintática                              #
# ---------------------------------------------------------------------------- #

import ply.yacc as yacc

from must_lex import tokens
myVariables = []
def hasInArray(name):
    index = 0
    for v in myVariables:
        if v['name'] == name:
            return index
        index += 1
    
    return -1


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
         | CONST VAR COLON INT
         | CONST VAR COLON FLOAT
         | CONST VAR COLON CHAR
         | CONST VAR COLON INT ATTR LIT_INT
         | CONST VAR COLON FLOAT ATTR LIT_FLOAT
         | CONST VAR COLON CHAR ATTR LIT_CHAR
    '''

    if len(p) == 5:
        myVariables.append({'name': p[2], 'type': p[4] , 'value': None})
    elif len(p) == 7:
        myVariables.append({'name': p[2], 'type': p[4] , 'value': p[6]})

def p_other(p):
    'term : VAR ATTR expr'
    if hasInArray(p[1]) != -1:
        if myVariables[hasInArray(p[1])]['type'] == 'char':
            myVariables[hasInArray(p[1])]['value'] = p[3][1]
        else: 
            myVariables[hasInArray(p[1])]['value'] = p[3]

def p_expr_term(p):
    'expr : term'
    p[0] = p[1]

def p_main(p):
    'term : MAIN BLOCK_START expr BLOCK_END'

def p_term_literal_char(p):
    'term : LIT_CHAR'
    p[0] = p[1][1]


def p_term_literal_var(p):
    'term : VAR'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_term_literal_int(p):
    'factor : LIT_INT'
    p[0] = int(p[1])


def p_term_literal_float(p):
    'factor : LIT_FLOAT'
    p[0] = float(p[1])

def p_expr_factor(p):
    'factor : PAR_START expr PAR_END'
    p[0] = p[2]

# se quisermos ir somando strings com variaveis ainda precisa implementar
# def p_exprCont(p):
#     '''
#     exprcont : expr 
#              | ASP expr ASP
#              | exprcont SUM exprcont
#     ''' 

def p_output(p):
    '''
    term : OUTPUT PAR_START expr PAR_END
         | OUTPUT PAR_START ASP expr ASP PAR_END
    '''         
    if len(p) <= 5:
        if hasInArray(p[3]) != -1:
            value = myVariables[hasInArray(p[3])]['value'];
            typeVar = myVariables[hasInArray(p[3])]['type'];
            if typeVar == 'int' or typeVar == 'float':
                print(value)
            elif typeVar == 'char':
                print(value[1])
        else:
            print(p[3])
    else:
        if len(p) ==7: 
            print(p[4])
        else:
            print

def p_line(p):
    '''
    term : term SEMICOLON
    term : term SEMICOLON term
    term : term SEMICOLON BLOCK_END
    '''


def p_error(t):
    if t is not None :
        print("Syntax error at '%s'" % t.value)



parser = yacc.yacc()

print('\n----- fim codigo -----\n')
data1 = '''
main {
    let variavel_char: char = '5';
    output(variavel_char);
    const PI: float = 3.14;
    output(PI);
    output("texto");
    let variavel_apenas_declarada: int;
    variavel_apenas_declarada = 4;
    output(variavel_apenas_declarada);
}
'''

data2 = '''
main {
    let variavelchar: char = '5';
    if(char == 5){
        variavelchar = '3;
        output(variavelchar)
    }
}
'''

print('ENTRADA: ', data1)


print('\nSAIDA: ')

result = parser.parse(data1)

