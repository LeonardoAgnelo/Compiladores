import sys
import logging
from antlr4 import *
from Parser.LALexer import LALexer
from Parser.LAParser import LAParser
from antlr4.error.ErrorListener import ErrorListener

class LexerErrorListener(ErrorListener):
    """
    Classe personalizada que trata erros léxicos durante a análise.
    Herda da classe ErrorListener do ANTLR.
    """
    def __init__(self, outfile):
        super().__init__()
        self.outfile = outfile
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Método chamado quando ocorre um erro léxico.
        
        Parâmetros:
            - recognizer: O reconhecedor do lexer.
            - offendingSymbol: O símbolo que causou o erro.
            - line: O número da linha onde o erro ocorreu.
            - column: A coluna onde o erro ocorreu.
            - msg: A mensagem de erro.
            - e: A exceção relacionada ao erro.
        """
        errText = recognizer._input.getText(recognizer._tokenStartCharIndex, recognizer._input.index)
        errText = recognizer.getErrorDisplay(errText)
        if(len(errText) <= 1):
            self.outfile.write("Linha " + str(line) + ": " + errText + " - simbolo nao identificado\n")
        elif('{' in errText or '}' in errText):
            self.outfile.write("Linha " + str(line) + ": comentario nao fechado\n")
        elif('"' in errText):
            self.outfile.write("Linha " + str(line) + ": cadeia literal nao fechada\n")
        raise Exception()
    
    
class ParserErrorListener(ErrorListener):
    def __init__(self, outfile):
        super().__init__()
        self.outfile = outfile
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.outfile.write("Linha " + str(line) + ": erro sintatico proximo a " + offendingSymbol.text + '\n')
        self.outfile.write("Fim da compilacao\n")
        raise Exception()


def main():
    # Obtém o nome do arquivo de entrada e de saída a partir dos argumentos da linha de comando
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input = FileStream(input_file, encoding='utf-8')
    output = open(output_file, 'w')
    lexer = LALexer(input, output)
    tokens = CommonTokenStream(lexer)
    parser = LAParser(tokens, output)
    lexer.addErrorListener(LexerErrorListener(output))
    parser.addErrorListener(ParserErrorListener(output))
    
    parser.programa()   

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        logging.error(error)
