# Trabalho 1 de Compiladores - Analisador Léxico

## Docente
Daniel Lucrédio  

## Discente
Leonardo Nogueira Agnelo - 77801  
João Gabriel Gonçalves - 769690  
Victor Fernandes Dell Elba Gomes - 769839 

### Pré-requisitos
Certifique-se de ter os seguintes requisitos instalados em seu sistema:

Python 3

Java Development Kit (JDK) - versão 8 ou superior

ANTLR4-Tools

ANTLR4 Python Runtime

### COMO EXECUTAR
    # Instale o runtime para python
    $ pip install antlr4-python3-runtime

    # Instale as ferramentas do ANTLR4
    $ pip install antlr4-tools

    # Gerar Lexer
    $ antlr4 -Dlanguage=Python3 lexerT1.g4 -o "Lexer"

    # Teste do Lexer
    $ py main.py "casos-de-teste\1.casos_teste_t1\entrada\30-algoritmo_2-2_apostila_LA_erro_linha_5txt" "saida.txt"

    # Corretor Automatico
    $ java -jar "corretor\Corretor.jar" "py main.py" gcc "temp" "casos-de-teste" "779801" t1
