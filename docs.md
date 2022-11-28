# Documentação

Alguns detalhes sobre esse trabalho comparado ao inicial:

- Para o trabalho prático, foi preciso gerar os tokens literais, como o LIT_CHAR, LIT_INT e o LIT_FLOAT, assim como os tokens unitários de operadores lógicos, aritméticas e relacionais;
- Não foi possível gerar um comando de saída que intercalasse strings com variáveis na mesma expressão;
- Variáveis constantes precisam ter valor atribuído quando forem declarados, pois ao traduzir para linguagem C, esta requer atribuição obrigatória;
- As regras de produção mudaram significativamente, em algumas partes.
- Foi necessário adicionar mais regras curtas, pois o analisador sintático não conseguia acessar variáveis que ainda precisavam passar por mais uma produção.

## Novas produções:

##### Símbolo inicial

```
programa : MAIN BLOCK_START exprs BLOCK_END
```

##### Expressão vazia

```
exprs :
```

##### Expressão única sem ponto e vírgula

```
exprs : expr
```

##### Expressão única com ponto e vírgula

```
exprs : expr SEMICOLON
```

##### Expressões múltiplas sem ponto e vírgula

```
exprs : exprs expr
```

##### Expressões múltiplas com ponto e vírgula

```
exprs : exprs expr SEMICOLON
```

##### Expressão para output de string comum

```
expr : OUTPUT PAR_START ASP VAR ASP PAR_END
```

##### Expressão para output de variável

```
expr : OUTPUT PAR_START VAR PAR_END
```

##### Expressão para input de variável

```
expr : INPUT PAR_START VAR PAR_END
```

##### Expressão para declaração de inteiro

```
expr : LET VAR COLON INT
```

##### Expressão para atribuição de inteiro

```
expr :  VAR ATTR LIT_INT
```

##### Expressão para declaração de int com atribuição

```
expr : LET VAR COLON INT ATTR LIT_INT
```

##### Expressão para declaração de constante com atribuição obrigatória

```
expr : CONST VAR COLON INT ATTR LIT_INT
```

A mesma sequência de produções para inteiros foi criada para float e char como mostrado a seguir:

##### Para float

```
expr : LET VAR COLON FLOAT
```

```
expr :  VAR ATTR LIT_FLOAT
```

```
expr : LET VAR COLON FLOAT ATTR LIT_FLOAT
```

```
expr : CONST VAR COLON FLOAT ATTR LIT_FLOAT
```

##### Para char

```
expr : LET VAR COLON CHAR
```

```
expr :  VAR ATTR LIT_CHAR
```

```
expr : LET VAR COLON CHAR ATTR LIT_CHAR
```

```
expr : CONST VAR COLON CHAR ATTR LIT_CHAR
```

##### Expressão para atribuição geral

```
expr : VAR ATTR expr
```

##### Expressão para operadores aritméticos

```
expr : expr SUM expr
     | expr SUB expr
     | expr MULT expr
     | expr DIV expr
     | expr MOD expr
```

##### Expressão para operadores relacionais

```
expr : expr EQUALS expr
     | expr NOT_EQUALS expr
     | expr GREATER expr
     | expr SMALLER expr
     | expr GREATER_EQUALS expr
     | expr SMALLER_EQUALS expr
```

##### Expressão para operadores lógicos

```
expr : expr AND expr
     | expr OR expr
     | NOT expr
```

##### Expressão de condicional com único if

```
expr : IF PAR_START exprs PAR_END BLOCK_START exprs BLOCK_END
```

##### Expressão de condicional com if-else

```
expr : IF PAR_START exprs PAR_END BLOCK_START exprs BLOCK_END ELSE BLOCK_START exprs BLOCK_END
```

##### Expressão de loop while

```
expr : WHILE PAR_START exprs PAR_END BLOCK_START exprs BLOCK_END
```

Para o loop for, foi necessário criar expressões auxiliares, denominadas como `exprfor`, pois a precedência de expressão e ponto e vírgula muda dentro do parênteses. Seguem as expressões criadas:

##### Expressão única sem ponto e virgula

```
exprsfor : expr
```

##### Expressão múltipla que adiciona a nova expr à esquerda do ;

```
exprsfor : expr SEMICOLON exprsfor
```

##### Expressão para loop for

```
expr : FOR PAR_START exprsfor PAR_END BLOCK_START exprs BLOCK_END
```

##### Expressão que torna termo

```
expr : term
```

##### Termo que torna variável

```
term : VAR
```

##### Termo que torna int literal

```
term : LIT_INT
```

##### Termo que torna float literal

```
term : LIT_FLOAT
```

##### Termo que torna char literal

```
term : LIT_CHAR
```

##### Termo para adição de parênteses

```
term : PAR_START expr PAR_END
```
