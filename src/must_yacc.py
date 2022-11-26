
# ---------------------------------------------------------------------------- #
#                               Análise Sintática                              #
# ---------------------------------------------------------------------------- #

import ply.yacc as yacc

from must_lex import tokens

myVariables = []
# boolStack = []

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

def p_main(p):
    'programa : MAIN BLOCK_START exprs BLOCK_END'
    f = open("codigo_gerado.c", "w")
    f.write(f"#include <stdio.h>\nint main(){{\n   {p[3]}\n   return 0;\n}}")
    f.close()

def p_exprs_void(p):
    '''
    exprs :  
    '''
    p[0] = ""

def p_exprs_no_semicolon(p):
    '''
    exprs : expr 
    '''   
    p[0] = p[1]
    

def p_exprs_single(p):
    '''
        exprs : expr SEMICOLON 
    '''   
    p[0] = p[1] + f";\n   "

def p_expr_many_no_semicolon(p):
    '''
        exprs : exprs expr  
    '''   
    p[0] = p[1] + p[2]

def p_expr_many(p):
    '''
        exprs : exprs expr SEMICOLON 
    '''   
    p[0] = p[1] + p[2] + f";\n   "

def p_output_string(p):
    '''
    expr : OUTPUT PAR_START ASP VAR ASP PAR_END
    '''       
    if len(p) == 7:
        p[0] = f'printf("{p[4]}\\n")'

def p_output_var(p):
    '''
    expr : OUTPUT PAR_START VAR PAR_END
    '''   
    if(hasInArray(p[3]) != -1):
        if(myVariables[hasInArray(p[3])]['type'] == 'int'):
            p[0] = f'printf("%d\\n",{p[3]})'
        elif(myVariables[hasInArray(p[3])]['type'] == 'float'):
            p[0] = f'printf("%f\\n",{p[3]})'
        if(myVariables[hasInArray(p[3])]['type'] == 'char'):
            p[0] = f'printf("%c\\n",{p[3]})'

def p_input_var(p):
    '''
    expr : INPUT PAR_START VAR PAR_END
    '''
    if(hasInArray(p[3]) != -1):
        if(myVariables[hasInArray(p[3])]['type'] == 'int'):
            p[0] = f'printf("Digite um valor para {p[3]}: ");\n   scanf("%d", &{p[3]})'
        elif(myVariables[hasInArray(p[3])]['type'] == 'float'):
            p[0] = f'printf("Digite um valor para {p[3]}: ");\n   scanf("%f", &{p[3]})'
        if(myVariables[hasInArray(p[3])]['type'] == 'char'):
            p[0] = f'printf("Digite um valor para {p[3]}: ");\n   scanf("%c", &{p[3]})'

#FUNCOES PARA INT
#FUNCOES PARA INT
#FUNCOES PARA INT

def p_decl_int(p):
    '''
    expr : LET VAR COLON INT
    '''
    myVariables.append({'name': p[2], 'type': 'int' , 'value': None, 'mutabilty': 'let'})
    p[0] = f'int {p[2]}'

def p_attr_int(p):
    '''
    expr :  VAR ATTR LIT_INT
    '''
    if hasInArray(p[1]) != -1:
        myVariables[hasInArray(p[1])]['value'] = p[3]

    p[0] = f'{p[1]} = {p[3]}'

def p_decl_let_int_attr(p):
    '''
    expr : LET VAR COLON INT ATTR LIT_INT
    '''
    myVariables.append({'name': p[2], 'type': 'int' , 'value': None, 'mutabilty': 'let'})
    p[0] = f'int {p[2]} = {p[6]}'


def p_decl_const_int_attr(p):
    '''
    expr : CONST VAR COLON INT ATTR LIT_INT
    '''
    myVariables.append({'name': p[2], 'type': 'int' , 'value': None, 'mutabilty': 'const'})
    p[0] = f'const int {p[2]} = {p[6]}'

#FUNCOES PARA FLOAT
#FUNCOES PARA FLOAT
#FUNCOES PARA FLOAT

def p_decl_float(p):
    '''
    expr : LET VAR COLON FLOAT
    '''
    myVariables.append({'name': p[2], 'type': 'float' , 'value': None, 'mutabilty': 'let'})
    p[0] = f'float {p[2]}'

def p_attr_float(p):
    '''
    expr :  VAR ATTR LIT_FLOAT
    '''
    if hasInArray(p[1]) != -1:
        myVariables[hasInArray(p[1])]['value'] = p[3]

    p[0] = f'{p[1]} = {p[3]}'

def p_decl_let_float_attr(p):
    '''
    expr : LET VAR COLON FLOAT ATTR LIT_FLOAT
    '''
    myVariables.append({'name': p[2], 'type': 'float' , 'value': None, 'mutabilty': 'let'})
    p[0] = f'float {p[2]} = {p[6]}'


def p_decl_const_float_attr(p):
    '''
    expr : CONST VAR COLON FLOAT ATTR LIT_FLOAT
    '''
    myVariables.append({'name': p[2], 'type': 'float' , 'value': None, 'mutabilty': 'const'})
    p[0] = f'const float {p[2]} = {p[6]}'


#FUNCOES PARA CHAR
#FUNCOES PARA CHAR
#FUNCOES PARA CHAR

def p_decl_char(p):
    '''
    expr : LET VAR COLON CHAR
    '''
    myVariables.append({'name': p[2], 'type': 'char' , 'value': None, 'mutabilty': 'let'})
    p[0] = f'char {p[2]}'

def p_attr_char(p):
    '''
    expr :  VAR ATTR LIT_CHAR
    '''
    if hasInArray(p[1]) != -1:
        myVariables[hasInArray(p[1])]['value'] = p[3]

    p[0] = f'{p[1]} = {p[3]}'

def p_decl_let_char_attr(p):
    '''
    expr : LET VAR COLON CHAR ATTR LIT_CHAR
    '''
    myVariables.append({'name': p[2], 'type': 'char' , 'value': None, 'mutabilty': 'let'})
    p[0] = f'char {p[2]} = {p[6]}'


def p_decl_const_char_attr(p):
    '''
    expr : CONST VAR COLON CHAR ATTR LIT_CHAR
    '''
    myVariables.append({'name': p[2], 'type': 'char' , 'value': None, 'mutabilty': 'const'})
    p[0] = f'const char {p[2]} = {p[6]}'

def p_attr(p):
    '''
    expr :  VAR ATTR expr
    '''
    if hasInArray(p[1]) != -1:
        myVariables[hasInArray(p[1])]['value'] = p[3]
    p[0] = f'{p[1]} = {p[3]}'

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
            p[0] = f"{p[1]} + {p[3]}" 
        case '-':
            p[0] = f"{p[1]} - {p[3]}" 
        case '*':
            p[0] = f"{p[1]} * {p[3]}" 
        case '/':
            p[0] = f"{p[1]} / {p[3]}" 
        case '%':
            p[0] = f"{p[1]} % {p[3]}" 

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
            p[0] = f"{p[1]} == {p[3]}"
        case '!=':
            p[0] = f"{p[1]} != {p[3]}"
        case '>':
            p[0] = f"{p[1]} > {p[3]}"
        case '<':
            p[0] = f"{p[1]} < {p[3]}"
        case '>=':
            p[0] = f"{p[1]} >= {p[3]}"
        case '<=':
            p[0] = f"{p[1]} <= {p[3]}"


def p_expr_logicals(p):
    '''
    expr : expr AND expr
         | expr OR expr
         | NOT expr
    '''

    if p[1] == '!':
        p[0] = f"!{p[2]}"

    match p[2]:
        case '&&':
            p[0] = f"{p[1]} && {p[3]}"
        case '||':
            p[0] = f"{p[1]} || {p[3]}"

def p_cond_if_only(p):
    '''
    expr : IF PAR_START exprs PAR_END BLOCK_START exprs BLOCK_END
    '''      
    p[0] = f"if({p[3]}){{ \n {p[6]} \n }} "

def p_cond_if_else(p):
    '''
    expr : IF PAR_START exprs PAR_END BLOCK_START exprs BLOCK_END ELSE BLOCK_START exprs BLOCK_END
    '''         
    p[0] = f"if({p[3]}){{ \n {p[6]} \n }} else {{ \n {p[10]} }}"

def p_while(p):    
    '''
    expr : WHILE PAR_START exprs PAR_END BLOCK_START exprs BLOCK_END
    ''' 
    p[0] = f"while({p[3]}){{ \n {p[6]} \n }}"

def p_exprs_no_semicolon(p):
    '''
    exprsfor : expr 
    '''   
    p[0] = p[1]

def p_exprs_for_no_breakline(p):
    '''
        exprsfor :  expr SEMICOLON exprsfor
    '''   
    p[0] = p[1] + f"; " + p[3] 


def p_for(p):    
    '''
    expr : FOR PAR_START exprsfor PAR_END BLOCK_START exprs BLOCK_END
    ''' 
    p[0] = f"for({p[3]}){{ \n {p[6]}  }}"

def p_expr_term(p):
    'expr : term'
    p[0] = p[1]

def p_term_literal_char(p):
    'term : LIT_CHAR'
    p[0] = p[1]


def p_term_literal_var(p):
    'term : VAR'
    p[0] = p[1]

def p_term_literal_int(p):
    'term : LIT_INT'
    p[0] = p[1]


def p_term_literal_float(p):
    'term : LIT_FLOAT'
    p[0] = p[1]


def p_term_par_expr(p):
    'term : PAR_START expr PAR_END'
    p[0] = f'({p[2]})'

def p_error(t):
    if t is not None :
        print("Syntax error at '%s'" % t.value)



parser = yacc.yacc()

print('\n----- fim codigo -----\n')
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
    variavel_int = 3;
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
    for(variavel_int = 3; variavel_int > 0; variavel_int = variavel_int - 1 ){
        output(variavel_int);
        variavel_int = variavel_int + 1;
    }
}
'''

print('ENTRADA: ', data8)

result = parser.parse(data8)



######################################  Codigo antigo ####################################
# def p_decl(p):
#     '''
#     expr : LET VAR COLON INT
#          | LET VAR COLON FLOAT
#          | LET VAR COLON CHAR
#          | LET VAR COLON INT ATTR LIT_INT
#          | LET VAR COLON FLOAT ATTR LIT_FLOAT
#          | LET VAR COLON CHAR ATTR LIT_CHAR
#          | CONST VAR COLON INT
#          | CONST VAR COLON FLOAT
#          | CONST VAR COLON CHAR
#          | CONST VAR COLON INT ATTR LIT_INT
#          | CONST VAR COLON FLOAT ATTR LIT_FLOAT
#          | CONST VAR COLON CHAR ATTR LIT_CHAR
#     '''

#     if len(p) == 5:
#         print('let aqui')
#     elif len(p) == 7:
        
#         if len(p[6]) == 3:
#             pass
#         else: 
#             pass

# def p_attr(p):
#     '''
#     expr :  VAR ATTR LIT_INT
#           | VAR ATTR LIT_FLOAT
#           | VAR ATTR LIT_CHAR
#           | VAR ATTR expr  
#     '''

# def p_expr_operations(p):
#     '''
#     expr : expr SUM expr
#          | expr SUB expr
#          | expr MULT factor
#          | expr DIV factor
#          | expr MOD expr
#     '''
#     if(hasInArray(p[1]) != -1):
#         p[1] = myVariables[hasInArray(p[1])]['value']
        
#     match p[2]:
#         case '+':
#             p[0] = p[1] + p[3]
#         case '-':
#             p[0] = p[1] - p[3]
#         case '*':
#             p[0] = p[1] * p[3]
#         case '/':
#             p[0] = p[1] / p[3]
#         case '%':
#             p[0] = p[1] % p[3]


# def p_expr_relationals(p):
#     '''
#     expr : expr EQUALS expr
#          | expr NOT_EQUALS expr
#          | expr GREATER expr
#          | expr SMALLER expr
#          | expr GREATER_EQUALS expr
#          | expr SMALLER_EQUALS expr
#     '''
#     if(hasInArray(p[1]) != -1):
#         match myVariables[hasInArray(p[1])]['type']:
#             case 'int':
#                 p[1] = int(myVariables[hasInArray(p[1])]['value'])
#             case 'float':
#                 p[1] = float(myVariables[hasInArray(p[1])]['value'])
#             case 'char':
#                 p[1] = myVariables[hasInArray(p[1])]['value']
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
#     expr : expr AND expr
#          | expr OR expr
#          | NOT expr
#     '''

#     if p[1] == '!':
#         p[0] = not p[2]

#     match p[2]:
#         case '&&':
#             p[0] = p[1] and p[3]
#         case '||':
#             p[0] = p[1] or p[3]


# def p_decl(p):
#     '''
#     term : LET VAR COLON INT
#          | LET VAR COLON FLOAT
#          | LET VAR COLON CHAR
#          | LET VAR COLON INT ATTR LIT_INT
#          | LET VAR COLON FLOAT ATTR LIT_FLOAT
#          | LET VAR COLON CHAR ATTR LIT_CHAR
#          | CONST VAR COLON INT
#          | CONST VAR COLON FLOAT
#          | CONST VAR COLON CHAR
#          | CONST VAR COLON INT ATTR LIT_INT
#          | CONST VAR COLON FLOAT ATTR LIT_FLOAT
#          | CONST VAR COLON CHAR ATTR LIT_CHAR
#     '''

#     if len(p) == 5:
#         myVariables.append({'name': p[2], 'type': p[4] , 'value': None})
#     elif len(p) == 7:
#         if len(p[6]) == 3:
#             myVariables.append({'name': p[2], 'type': p[4] , 'value': p[6][1]})
#         else: 
#             myVariables.append({'name': p[2], 'type': p[4] , 'value': p[6]})


# def p_attr(p):
#     '''
#     term :  VAR ATTR LIT_INT
#           | VAR ATTR LIT_FLOAT
#           | VAR ATTR LIT_CHAR
#           | VAR ATTR expr  
#     '''
#     if hasInArray(p[1]) != -1:
#         if myVariables[hasInArray(p[1])]['type'] == 'char':
#             myVariables[hasInArray(p[1])]['value'] = p[3][1]
#         else: 
#             myVariables[hasInArray(p[1])]['value'] = p[3]





# def p_main(p):
#     'term : MAIN BLOCK_START expr BLOCK_END'


# def p_term_literal_char(p):
#     'term : LIT_CHAR'
#     p[0] = p[1][1]


# def p_term_literal_var(p):
#     'term : VAR'
#     p[0] = p[1]


# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]


# def p_term_literal_int(p):
#     'factor : LIT_INT'
#     p[0] = int(p[1])


# def p_term_literal_float(p):
#     'factor : LIT_FLOAT'
#     p[0] = float(p[1])


# def p_expr_factor(p):
#     'factor : PAR_START expr PAR_END'
#     p[0] = p[2]

# def p_cond(p):
#     '''
#     term : IF PAR_START expr PAR_END BLOCK_START expr BLOCK_END
#          | IF PAR_START expr PAR_END BLOCK_START expr BLOCK_END ELSE BLOCK_START expr BLOCK_END
#     '''
#     #falta adicionar o funcionamento
#     if p[3]:
#         boolStack.append(True)
#     elif len(p) == 12:
#         boolStack.append(False)
#     else:
#         boolStack.append(False)


# def p_output(p):
#     '''
#     term : OUTPUT PAR_START expr PAR_END
#          | OUTPUT PAR_START ASP expr ASP PAR_END
#     '''       
#     if len(p) <= 5:
#         if hasInArray(p[3]) != -1:
#             value = myVariables[hasInArray(p[3])]['value'];
#             typeVar = myVariables[hasInArray(p[3])]['type'];
#             if typeVar == 'int' or typeVar == 'float':
#                 print(value)
#             elif typeVar == 'char':
#                 print(value)
#         else:
#             print(p[3])
#     else:
#         if len(p) ==7: 
#             print(p[4])
# def p_input(p):
#     '''
#     term : INPUT PAR_START VAR PAR_END
#     '''
#     if hasInArray(p[3]) != -1:
#         typeVar = myVariables[hasInArray(p[3])]['type']
#         inputValue = input("Digite o valor para " + myVariables[hasInArray(p[3])]['name'] +': ')  
#         if typeVar == 'int' and  type(int(inputValue)) is int:
#             myVariables[hasInArray(p[3])]['value'] =  int(inputValue) 
#         elif typeVar == 'float' and  type(float(inputValue)) is float:
#             myVariables[hasInArray(p[3])]['value'] =  float(inputValue)  
#         elif typeVar == 'char' and len(inputValue) == 3:    
#             myVariables[hasInArray(p[3])]['value'] = inputValue[1]
#         else:
#             print("Não foi possível atribuir, erro de tipagem")


# def p_line(p):
#     '''
#     term : term SEMICOLON
#     term : term SEMICOLON term
#     term : term SEMICOLON BLOCK_END
#     '''

# def p_while(p):
#     '''
#     term : WHILE PAR_START expr PAR_END BLOCK_START term BLOCK_END
#     '''        
#     while p[3]:
#         p[0] = p[6]

##
######################################  Codigo antigo ####################################
