
# ---------------------------------------------------------------------------- #
#                               Análise Sintática                              #
# ---------------------------------------------------------------------------- #

import ply.yacc as yacc
import ast

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
    if (hasInArray(p[1]) != -1):
        p[1] = myVariables[hasInArray(p[1])]['value']

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
    if (hasInArray(p[1]) != -1):
        match myVariables[hasInArray(p[1])]['type']:
            case 'int':
                p[1] = int(myVariables[hasInArray(p[1])]['value'])
            case 'float':
                p[1] = float(myVariables[hasInArray(p[1])]['value'])
            case 'char':
                p[1] = myVariables[hasInArray(p[1])]['value']
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
        myVariables.append({'name': p[2], 'type': p[4], 'value': None})
    elif len(p) == 7:
        if len(p[6]) == 3:
            myVariables.append({'name': p[2], 'type': p[4], 'value': p[6][1]})
        else:
            myVariables.append({'name': p[2], 'type': p[4], 'value': p[6]})


def p_attr(p):
    '''
    term :  VAR ATTR LIT_INT
          | VAR ATTR LIT_FLOAT
          | VAR ATTR LIT_CHAR
          | VAR ATTR expr
    '''
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


def p_output(p):
    '''
    term : OUTPUT PAR_START expr PAR_END
         | OUTPUT PAR_START ASP expr ASP PAR_END
    '''
    if len(p) <= 5:
        if hasInArray(p[3]) != -1:
            value = myVariables[hasInArray(p[3])]['value']
            typeVar = myVariables[hasInArray(p[3])]['type']
            if typeVar == 'int' or typeVar == 'float':
                print(value)
            elif typeVar == 'char':
                print(value)
        else:
            print(p[3])
    else:
        if len(p) == 7:
            print(p[4])


def p_input(p):
    '''
    term : INPUT PAR_START VAR PAR_END
    '''
    if hasInArray(p[3]) != -1:
        typeVar = myVariables[hasInArray(p[3])]['type']
        inputValue = input("Digite o valor para " +
                           myVariables[hasInArray(p[3])]['name'] + ': ')
        if typeVar == 'int' and type(int(inputValue)) is int:
            myVariables[hasInArray(p[3])]['value'] = int(inputValue)
        elif typeVar == 'float' and type(float(inputValue)) is float:
            myVariables[hasInArray(p[3])]['value'] = float(inputValue)
        elif typeVar == 'char' and len(inputValue) == 3:
            myVariables[hasInArray(p[3])]['value'] = inputValue[1]
        else:
            print("Não foi possível atribuir, erro de tipagem")


def p_cond(p):
    '''
    term : IF PAR_START expr PAR_END BLOCK_START term BLOCK_END
         | IF PAR_START expr PAR_END BLOCK_START term BLOCK_END ELSE BLOCK_START term BLOCK_END
    '''
    for idx, item in enumerate(p):
        print(str(idx) + ': ' + str(item))

    # if p[3]:
    #     ast.literal_eval(str(p[6]))
    # elif len(p) == 11:
    #     ast.literal_eval(str(p[10]))

    if p[3]:
        p[0] = ast.literal_eval(p[6])
    elif len(p) == 12:
        p[0] = ast.literal_eval(p[10])

    ast.literal_eval(str(p[0]))


def p_while(p):
    'term : WHILE PAR_START expr PAR_END BLOCK_START expr BLOCK_END'

    for idx, item in enumerate(p):
        print(str(idx) + ': ' + str(item))

    while p[3]:
        ast.literal_eval(p[6])


def p_line(p):
    '''
    term : term SEMICOLON
         | term SEMICOLON term
         | term SEMICOLON BLOCK_END
    '''


def p_error(t):
    if t is not None:
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

    let variavel_apenas_declarada: char;
    variavel_apenas_declarada = '4';
    output(variavel_apenas_declarada);

    let variavel_atribuida_por_input: int;
    input(variavel_atribuida_por_input);
    output(variavel_atribuida_por_input);
'''

data2 = '''
main {
    let variavel: int = 4;

    while(variavel == 4) {
        output(variavel);
    }
    
}
'''

# print('ENTRADA: ', data2)


print('\nSAIDA: ')

# result = parser.parse(data2)

ast.literal_eval('''
x = 5

print(x)
''')
