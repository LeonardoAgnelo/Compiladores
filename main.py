import sys
import logging
import re
from antlr4 import *
from Parser.LALexer import LALexer
from Parser.LAParser import LAParser
from antlr4.error.ErrorListener import ErrorListener
from Parser.LAVisitor import LAVisitor

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
        self.outfile.write("Fim da compilacao\n")
        raise Exception()
    
    
class ParserErrorListener(ErrorListener):
    def __init__(self, outfile):
        super().__init__()
        self.outfile = outfile
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        ttext = offendingSymbol.text
        if ttext == "<EOF>":
            ttext = "EOF"
        self.outfile.write("Linha " + str(line) + ": erro sintatico proximo a " + ttext + '\n')
        self.outfile.write("Fim da compilacao\n")
        raise Exception()
    
class Visitor(LAVisitor):
    def __init__(self, outfile):
        super().__init__()
        self.identificadores = {}
        self.outfile = outfile
        self.identificadorparcela = None

    def handle(self, tree):
        self.visit(tree)
        self.outfile.write("Fim da compilacao\n")

    def visitVariavel(self, ctx:LAParser.VariavelContext, registro = False, registroIdent = None):
        registroCriado = False
        for identificador in ctx.identificador():
            if ctx.tipo().registro():
                #Cria dict para escopo/registro
                registroCriado = True
                if identificador.getText() not in self.identificadores:
                    self.identificadores[identificador.getText()] = {}
                    self.identificadores[identificador.getText()]["tipo"] = "registro"
                    self.visitRegistro(ctx.tipo().registro(), identificador.getText())
            if identificador.getText() not in self.identificadores and not (registroCriado or registro):
                self.identificadores[identificador.getText()] = ctx.tipo().getText()
            elif identificador.getText() in self.identificadores and not (registroCriado or registro):
                self.outfile.write("Linha " + str(identificador.start.line) + ": identificador " + identificador.getText() +" ja declarado anteriormente\n")
            if registro:
                self.identificadores[registroIdent][identificador.getText()] = ctx.tipo().getText()
        return self.visitChildren(ctx)

    def visitRegistro(self, ctx:LAParser.RegistroContext, identificador = None):
        for variavel in ctx.variavel():
            if identificador:
                self.visitVariavel(variavel, True, identificador)
            #print(self.identificadores)

    def visitTipo_estendido(self, ctx:LAParser.Tipo_estendidoContext):
        tipo = ctx.tipo_basico_ident().getText()
        tipoPointer = tipo.replace("^", "")
        if tipoPointer not in ['inteiro', 'literal', 'real', 'logico']:
            self.outfile.write("Linha " + str(ctx.tipo_basico_ident().start.line) + ": tipo " + ctx.tipo_basico_ident().getText() +" nao declarado\n")
        return self.visitChildren(ctx)

    def visitIdentificador(self, ctx:LAParser.IdentificadorContext):
        found = False
        for ident in ctx.IDENT():
            for identificador in self.identificadores:
                if type(self.identificadores[identificador]) is dict:
                    if ident.getText() in self.identificadores[identificador].keys():
                        found = True
            if ident.getText() in self.identificadores:
                    found = True
            if not found:
                self.outfile.write("Linha " + str(ctx.start.line) + ": identificador " + ident.getText() +" nao declarado\n")
        return self.visitChildren(ctx)

    def visitParcela_unario(self, ctx:LAParser.Parcela_unarioContext):
        if self.identificadorparcela is not None:
            if ctx.NUM_INT() is not None and self.identificadores[self.identificadorparcela.replace("^", "")] not in ['inteiro', 'real']:
                self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
            elif ctx.NUM_REAL() is not None and self.identificadores[self.identificadorparcela.replace("^", "")] not in ['real','inteiro']:
                self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
            elif ctx.identificador() is not None and self.identificadores[self.identificadorparcela.replace("^", "")] not in [self.identificadores[ctx.identificador().getText()], 'logico']:
                if self.identificadores[ctx.identificador().getText().replace("&", "")] in ['inteiro','real'] and self.identificadores[self.identificadorparcela.replace("^", "")].replace("^", "") not in ['inteiro', 'real']:
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
        return self.visitChildren(ctx)

    def visitParcela_nao_unario(self, ctx:LAParser.Parcela_nao_unarioContext):
        if self.identificadorparcela is not None:
            if "." in self.identificadorparcela:
                identificador = self.identificadorparcela.split('.')
                if ctx.CADEIA() is not None and self.identificadores[identificador[0]][identificador[1]] != 'literal':
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
            else:
                if ctx.CADEIA() is not None and self.identificadores[self.identificadorparcela.replace("^", "")] != 'literal':
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
                elif ctx.identificador() is not None and self.identificadores[self.identificadorparcela.replace("^", "")].replace("^", "") not in [self.identificadores[ctx.identificador().getText().replace("&", "")], 'logico']:
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
        return self.visitChildren(ctx)

    def visitParcela_logica(self, ctx:LAParser.Parcela_logicaContext):
        if ctx.exp_relacional() is None and self.identificadorparcela is not None:
            self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
        return self.visitChildren(ctx)

    def visitCmdAtribuicao(self, ctx:LAParser.CmdAtribuicaoContext):
        self.identificadorparcela = ctx.identificador().getText()
        if ctx.POINTER():
            self.identificadorparcela = "^" + ctx.identificador().getText()
        self.visitChildren(ctx.expressao())
        self.identificadorparcela = None
        return self.visitChildren(ctx)




def main():
    # Obtém o nome do arquivo de entrada e de saída a partir dos argumentos da linha de comando
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input = FileStream(input_file, encoding='utf-8')
    output = open(output_file, 'w')
    lexer = LALexer(input, output)
    tokens = CommonTokenStream(lexer)
    parser = LAParser(tokens, output)
    val = parser.programa()
    visitor = Visitor(output)
    lexer.addErrorListener(LexerErrorListener(output))
    parser.addErrorListener(ParserErrorListener(output))
    visitor.handle(val)

    
       

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        logging.error(error)
