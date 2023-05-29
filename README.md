# Trabalho 1 de Compiladores - Analisador Léxico

## Docente
Daniel Lucrédio  

## Discente
Leonardo Nogueira Agnelo - 77801  
João Gabriel Gonçalves - 769690  
Victor Fernandes Dell Elba Gomes -   

### COMO EXECUTAR
    # Instale o runtime para python
    $ pip install antlr4-python3-runtime

    # Instale as ferramentas do ANTLR4
    $ pip install antlr4-tools

    # gerar lexer
    $ antlr4 -Dlanguage=Python3 lexerT1.g4 -o "Lexer"

    # Teste do lexer
    $ py main.py "casos-de-teste\1.casos_teste_t1\entrada\30-algoritmo_2-2_apostila_LA_erro_linha_5txt" "saida.txt"

    # Corretor automatico
    $ java -jar "corretor\Corretor.jar" "py main.py" gcc "temp" "casos-de-teste" "779801" t1
