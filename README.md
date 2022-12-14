# Linguagem **Must**

**Must** é uma linguagem de programação experimental baseada em Rust desenvolvida utilizando o [PLY](https://www.dabeaz.com/ply/) (Python Lex-Yacc). Essa linguagem foi feita como requisito avaliativo para a disciplina de Compiladores, ministrada pela Profa. Thatyana de Faria Piola Seraphim.

Os desenvolvedores do projeto são:

- [Gabriel Akio](http://github.com/GabrielOnohara)
- [Fabio Amorelli](http://github.com/fabioavf)

A documentação das produções também está [disponível](docs.md).

## Instalação

Para instalar esse projeto e testá-lo, faça [download do repositório como zip](https://github.com/fabioavf/must-lang/archive/refs/heads/main.zip) ou o clone:

```sh
git clone https://github.com/fabioavf/must-lang
```

## Utilização

A implementação utilizada faz uma geração de código em C que, posteriormente, pode ser compilada.

Portanto, no arquivo `must_yacc.py` você pode encontrar algumas strings com códigos de exemplo para variadas funcionalidades. Além disso, caso queira escrever seu próprio código, basta substituir a string de entrada em `result = parser.parse(data)`.

Para rodar gerar o código, basta inserir o seguinte comando no terminal:

```sh
python3 src/must_yacc.py
```

Feito isso, um arquivo `codigo gerado.c` será criado e você poderá compilá-lo.
