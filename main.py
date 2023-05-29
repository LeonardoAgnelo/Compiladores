import sys
import logging
from antlr4 import *
from lexer.lexerT1Lexer import lexerT1Lexer
from antlr4.error.ErrorListener import ErrorListener

class LexerErrorListener(ErrorListener):
    def __init__(self, outfile):
        super().__init__()
        self.outfile = outfile
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        errText = recognizer._input.getText(recognizer._tokenStartCharIndex, recognizer._input.index)
        errText = recognizer.getErrorDisplay(errText)
        print(len(errText))
        if(len(errText) <= 1):
            self.outfile.write("Linha " + str(line) + ": " + errText + " - simbolo nao identificado\n")
        elif('{' in errText or '}' in errText):
            self.outfile.write("Linha " + str(line) + ": comentario nao fechado\n")
        elif('"' in errText):
            self.outfile.write("Linha " + str(line) + ": cadeia literal nao fechada\n")
        raise Exception()


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input = FileStream(input_file, encoding='utf-8')
    output = open(output_file, 'w')
    lexer = lexerT1Lexer(input, output)
    lexer.addErrorListener(LexerErrorListener(output))

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