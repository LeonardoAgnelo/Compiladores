import sys
import logging
from antlr4 import *
from lexer.lexerT1Lexer import lexerT1Lexer
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


def main():
    # Obtém o nome do arquivo de entrada e de saída a partir dos argumentos da linha de comando
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input = FileStream(input_file, encoding='utf-8')
    output = open(output_file, 'w')
    lexer = lexerT1Lexer(input, output)
    lexer.addErrorListener(LexerErrorListener(output))

    # Loop para gerar e processar os tokens
    while (token := lexer.nextToken()).type is not Token.EOF:
        token_type = lexer.ruleNames[token.type -1]
        if (token_type not in str(['IDENT','CADEIA','NUM_INT','NUM_REAL'])):
            token_type = f"'{token.text}'"
        
        output.write(f"<'{token.text}',{token_type}>\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        logging.error(error)
