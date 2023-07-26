# Trabalho de Compiladores

## Docente
Daniel Lucrédio  

## Discente
Leonardo Nogueira Agnelo - 779801  
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
    $ antlr4 -Dlanguage=Python3 LA.g4 -visitor -o "Parser"

    # Teste do Lexer
    $ py main.py "casos-de-teste\3.casos_teste_t3\entrada\4.algoritmo_3-2_apostila_LA.txt" "saida.txt"

    # Corretor Automatico
    $ java -jar "corretor\Corretor.jar" "py main.py" gcc "temp" "casos-de-teste" "779801, 769690, 769839" t4
