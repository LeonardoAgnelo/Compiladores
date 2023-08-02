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
        self.customTipos = {}
        self.funcoes = {}
        self.constantes = {}

    def handle(self, tree):
        self.visit(tree)
        #self.outfile.write("Fim da compilacao\n")


    def visitDeclaracao_global(self, ctx:LAParser.Declaracao_globalContext):

        self.funcoes[ctx.IDENT().getText()] = {}
        if ctx.tipo_estendido():
            self.funcoes[ctx.IDENT().getText()]["tipo"] = ctx.tipo_estendido().getText()
        else:
            self.funcoes[ctx.IDENT().getText()]["tipo"] = "procedimento"
            if ctx.cmd():
                for comando in ctx.cmd():
                    self.visitCmd(comando, True)
        self.visitParametros(ctx.parametros(), ctx.IDENT())

    
    def visitParametros(self, ctx:LAParser.ParametrosContext, funcaoIdent = None):
        if funcaoIdent:
            self.funcoes[funcaoIdent.getText()]["parametros"] ={}
            for parametro in ctx.parametro():
                for identificador in parametro.identificador():
                    self.funcoes[funcaoIdent.getText()]["parametros"][identificador.getText()] = parametro.tipo_estendido().getText()
        return self.visitChildren(ctx)

    def visitCmd(self, ctx:LAParser.CmdContext, procedimento = False):
        if procedimento:
            if ctx.cmdRetorne():
                if ctx.cmdRetorne().expressao():
                    self.outfile.write("Linha " + str(ctx.start.line) + ": comando retorne nao permitido nesse escopo\n")
        else:
            return self.visitChildren(ctx)
        
    def visitCorpo(self, ctx:LAParser.CorpoContext):
        for comando in ctx.cmd():
            self.visitCmd(comando, True)
        return self.visitChildren(ctx)

    def visitVariavel(self, ctx:LAParser.VariavelContext, registro = False, registroIdent = None, tipo = False):
        registroCriado = False
        for identificador in ctx.identificador():
            if ctx.tipo().registro() and not tipo:
                #Cria dict para escopo/registro
                registroCriado = True
                if identificador.getText() not in self.identificadores:
                    self.identificadores[identificador.getText()] = {}
                    self.identificadores[identificador.getText()]["tipo"] = "registro"
                    self.visitRegistro(ctx.tipo().registro(), identificador.getText())
            if identificador.getText() not in self.identificadores and identificador.getText() not in self.funcoes and identificador.getText() not in self.constantes and not (registroCriado or registro or tipo):
                if '[' in identificador.getText() and ']' in identificador.getText():
                    identificadorSplit = identificador.getText().split('[')[0]
                    self.identificadores[identificadorSplit] = {}
                    dimensao = identificador.getText().split('[')[1].split(']')[0]
                    if dimensao.isnumeric():
                        dimensao = int(dimensao)
                    else:
                        if dimensao in self.constantes:
                            if self.constantes[dimensao].isnumeric():
                                dimensao = int(self.constantes[dimensao])
                    for i in range(dimensao):
                        self.identificadores[identificadorSplit][i] = ctx.tipo().getText()
                else:
                    self.identificadores[identificador.getText()] = ctx.tipo().getText()
            elif (identificador.getText() in self.identificadores or identificador.getText() in self.funcoes or identificador.getText() in self.constantes) and not (registroCriado or registro):
                self.outfile.write("Linha " + str(identificador.start.line) + ": identificador " + identificador.getText() +" ja declarado anteriormente\n")
            if registro:
                self.identificadores[registroIdent][identificador.getText()] = ctx.tipo().getText()
            if tipo:
                if registroIdent not in self.customTipos:
                    self.customTipos[registroIdent] = {}
                self.customTipos[registroIdent][identificador.getText()] = ctx.tipo().getText()
            if ctx.tipo().getText() in self.customTipos:
                if identificador.getText() in self.customTipos:
                    self.outfile.write("Linha " + str(identificador.start.line) + ": identificador " + identificador.getText() +" ja declarado anteriormente\n")
                else:
                    self.identificadores[identificador.getText()] = self.customTipos[ctx.tipo().getText()]
        return self.visitChildren(ctx)

    def visitRegistro(self, ctx:LAParser.RegistroContext, identificador = None, tipo = False):
        for variavel in ctx.variavel():
            if identificador and not tipo:
                self.visitVariavel(variavel, True, identificador)
            elif identificador and tipo:
                self.visitVariavel(variavel, False, identificador, True)

    def visitTipo_estendido(self, ctx:LAParser.Tipo_estendidoContext):
        tipo = ctx.tipo_basico_ident().getText()
        tipoPointer = tipo.replace("^", "")
        if tipoPointer not in ['inteiro', 'literal', 'real', 'logico'] and tipoPointer not in self.customTipos:
            self.outfile.write("Linha " + str(ctx.tipo_basico_ident().start.line) + ": tipo " + ctx.tipo_basico_ident().getText() +" nao declarado\n")
        return self.visitChildren(ctx)
    
    def visitDeclaracao_local(self, ctx:LAParser.Declaracao_localContext):
        if ctx.tipo() and ctx.tipo().registro():
            return self.visitRegistro(ctx.tipo().registro(), ctx.IDENT().getText(), True)
        if ctx.valor_constante():
            self.constantes[ctx.IDENT().getText()] = ctx.valor_constante().getText()
        return self.visitChildren(ctx)

    def findIdentificador(self, identificador, ctx):
        if "." in identificador:
            identificadorsplit = identificador.split('.')
            if identificadorsplit[0] not in self.identificadores:
                self.outfile.write("Linha " + str(ctx.start.line) + ": identificador " + identificador +" nao declarado\n")
                return False
            elif identificadorsplit[1] not in self.identificadores[identificadorsplit[0]]:
                self.outfile.write("Linha " + str(ctx.start.line) + ": identificador " + identificador +" nao declarado\n")
                return False
        elif "[" in identificador:
            identificadorsplit = identificador.split('[')[0]
            if identificadorsplit not in self.identificadores:
                self.outfile.write("Linha " + str(ctx.start.line) + ": identificador " + identificador +" nao declarado\n")
                return False
        elif identificador not in self.identificadores and identificador not in self.constantes:
            self.outfile.write("Linha " + str(ctx.start.line) + ": identificador " + identificador +" nao declarado\n")
            return False
        return True
    
    def visitCmdLeia(self, ctx:LAParser.CmdLeiaContext):
        for identificador in ctx.identificador():
            self.findIdentificador(identificador.getText(), ctx)
        return self.visitChildren(ctx)

    def visitParcela_unario(self, ctx:LAParser.Parcela_unarioContext):
        if self.identificadorparcela is not None:
            if "." in self.identificadorparcela:
                identificador = self.identificadorparcela.split('.')
                if ctx.NUM_INT() is not None and self.identificadores[identificador[0]][identificador[1]] not in ['inteiro', 'real']:
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
                elif ctx.NUM_REAL() is not None and self.identificadores[identificador[0]][identificador[1]] not in ['real','inteiro']:
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
            elif "[" in self.identificadorparcela:
                vetor = self.identificadorparcela.split("[")[0]
                if ctx.NUM_INT() is not None and self.identificadores[vetor][0] not in ['inteiro', 'real']:
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
            elif ctx.identificador() and "[" in ctx.identificador().getText():
                vetor = ctx.identificador().getText().split("[")[0]
                if self.identificadores[self.identificadorparcela.replace("^", "")] not in [self.identificadores[vetor][0], 'logico']:
                    if self.identificadores[vetor][0] in ['inteiro','real'] and self.identificadores[self.identificadorparcela.replace("^", "")].replace("^", "") not in ['inteiro', 'real']:
                        self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
            else:
                if ctx.NUM_INT() is not None and self.identificadores[self.identificadorparcela.replace("^", "")] not in ['inteiro', 'real', '^inteiro', '^real']:
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
                elif ctx.NUM_REAL() is not None and self.identificadores[self.identificadorparcela.replace("^", "")] not in ['real','inteiro']:
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
                elif ctx.identificador() is not None and self.identificadores[self.identificadorparcela.replace("^", "")] not in [self.identificadores[ctx.identificador().getText()], 'logico']:
                    if self.identificadores[ctx.identificador().getText().replace("&", "")] in ['inteiro','real'] and self.identificadores[self.identificadorparcela.replace("^", "")].replace("^", "") not in ['inteiro', 'real']:
                        self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
        if ctx.identificador():
            self.findIdentificador(ctx.identificador().getText(), ctx)
        
        if ctx.IDENT():
            parametros = self.funcoes[ctx.IDENT().getText()]["parametros"]
            if len(parametros) != len(ctx.expressao()):
                self.outfile.write("Linha " + str(ctx.start.line) + ": incompatibilidade de parametros na chamada de " + str(ctx.IDENT()) + "\n")
            else:
                for x, ex in enumerate(ctx.expressao()):
                    if ex.getText() in self.identificadores:
                        if self.identificadores[ex.getText()] != parametros[list(parametros)[x]]:
                            self.outfile.write("Linha " + str(ctx.start.line) + ": incompatibilidade de parametros na chamada de " + str(ctx.IDENT()) + "\n")

        return self.visitChildren(ctx)

    def visitParcela_nao_unario(self, ctx:LAParser.Parcela_nao_unarioContext):
        if self.identificadorparcela is not None:
            if "." in self.identificadorparcela:
                identificador = self.identificadorparcela.split('.')
                if ctx.CADEIA() is not None and self.identificadores[identificador[0]][identificador[1]] != 'literal':
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
            elif "[" in self.identificadorparcela:
                identificadorSplit = self.identificadorparcela.split('[')[0]
                indice = int(self.identificadorparcela.split('[')[1].split(']')[0])
                if ctx.CADEIA() is not None and self.identificadores[identificadorSplit][indice] != 'literal':
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
            else:
                if ctx.CADEIA() is not None and self.identificadores[self.identificadorparcela.replace("^", "")] != 'literal':
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
                elif ctx.identificador() is not None and self.identificadores[self.identificadorparcela.replace("^", "")].replace("^", "") not in [self.identificadores[ctx.identificador().getText().replace("&", "")], 'logico']:
                    self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
        if ctx.identificador():
            self.findIdentificador(ctx.identificador().getText(), ctx)
        return self.visitChildren(ctx)

    def visitParcela_logica(self, ctx:LAParser.Parcela_logicaContext):
        if ctx.exp_relacional() is None and self.identificadorparcela is not None:
            self.outfile.write("Linha " + str(ctx.start.line) + ": atribuicao nao compativel para " + self.identificadorparcela + "\n")
        return self.visitChildren(ctx)

    def visitCmdAtribuicao(self, ctx:LAParser.CmdAtribuicaoContext):
        if ctx.identificador():
            if not self.findIdentificador(ctx.identificador().getText(), ctx):
                return
        self.identificadorparcela = ctx.identificador().getText()
        if ctx.POINTER():
            self.identificadorparcela = "^" + ctx.identificador().getText()
        self.visitChildren(ctx.expressao())
        self.identificadorparcela = None
        return self.visitChildren(ctx)

class Generator(LAVisitor):
    def __init__(self, visitor: Visitor):
        self.visitor = visitor

    def handle(self, tree):
        self.visitor.handle(tree)
        self.visit(tree)
    
    def visitPrograma(self, ctx: LAParser.ProgramaContext):
        self.visitor.outfile.write("#include <stdio.h>\n")
        self.visitor.outfile.write("#include <stdlib.h>\n")
        self.visitor.outfile.write("\n\n")
        if ctx.declaracoes():
            self.visitDeclaracoes(ctx.declaracoes())
            self.visitor.outfile.write("\n\n")
        self.visitor.outfile.write("int main() {\n")
        self.visitCorpo(ctx.corpo())
        self.visitor.outfile.write("\treturn 0;\n")
        self.visitor.outfile.write("}\n")
    
    def visitCorpo(self, ctx:LAParser.CorpoContext):
        return self.visitChildren(ctx)

    def visitDeclaracao_local(self, ctx:LAParser.Declaracao_localContext):
        if ctx.tipo() and ctx.tipo().registro():
            return self.visitRegistro(ctx.tipo().registro(), ctx.IDENT().getText(), True)
        if ctx.valor_constante():
            self.visitor.outfile.write("#define " + ctx.IDENT().getText() + " " + ctx.valor_constante().getText())
        return self.visitChildren(ctx)

    def visitDeclaracao_global(self, ctx:LAParser.Declaracao_globalContext):
        if ctx.start.text == "procedimento":
            self.visitor.outfile.write(f"void {ctx.IDENT().getText()} (")
            parametros = self.visitor.funcoes[ctx.IDENT().getText()]["parametros"]
        elif ctx.start.text == "funcao":
            tipo = self.converteTipo(self.visitor.funcoes[ctx.IDENT().getText()]["tipo"])
            self.visitor.outfile.write(f"{tipo} {ctx.IDENT().getText()} (")
            parametros = self.visitor.funcoes[ctx.IDENT().getText()]["parametros"]

        for i, param in enumerate(parametros):
            if i > 0:
                self.outfile.write(" , ")
            if parametros[param] == "literal":
                self.visitor.outfile.write(f"{self.converteTipo(parametros[param])}* {param}")
            else:
                self.visitor.outfile.write(f"{self.converteTipo(parametros[param])} {param}")
        self.visitor.outfile.write(") {\n")
        for declaration in ctx.declaracao_local():
                self.visitDeclaracao_local(declaration)
        for command in ctx.cmd():
                self.visitCmd(command, ctx.IDENT().getText())
        self.visitor.outfile.write("} \n")

    def visitVariavel(self, ctx:LAParser.VariavelContext):
        for identificador in ctx.identificador():
            if ctx.tipo().getText() == "literal":
                self.visitor.outfile.write("    " + self.converteTipo(ctx.tipo().getText()) + " " + identificador.getText() + "[80];\n")
            elif ctx.tipo().registro():
                self.visitor.outfile.write("    struct {\n  ")
                self.visitRegistro(ctx.tipo().registro(), identificador.getText())
            else:
                self.visitor.outfile.write("    " + self.converteTipo(ctx.tipo().getText()) + " " + identificador.getText() + ";\n")
        return self.visitChildren(ctx)
    
    def visitRegistro(self, ctx:LAParser.RegistroContext, identificador = None, tipo = False):
        if identificador and not tipo:
            for variavel in ctx.variavel():
                self.visitVariavel(variavel)
            self.visitor.outfile.write("    } " + identificador + ";\n")
        if tipo:
            self.visitor.outfile.write("    typedef struct {\n  ")
            for variavel in ctx.variavel():
                self.visitVariavel(variavel)
            self.visitor.outfile.write("    } " + identificador + ";\n")

    def visitCmd(self, ctx:LAParser.CmdContext, identFunc = None):
        if ctx.cmdEscreva():
            self.visitCmdEscreva(ctx.cmdEscreva(), identFunc)
        else:
            return self.visitChildren(ctx)
        
    def visitCmdRetorne(self, ctx:LAParser.CmdRetorneContext):
        self.visitor.outfile.write("    return " + self.convertExpressao(ctx.expressao().getText()) + ";\n")
        return self.visitChildren(ctx)
        
    def visitCmdChamada(self, ctx:LAParser.CmdChamadaContext):
        self.visitor.outfile.write("    " + ctx.IDENT().getText() + "(")
        i = 0
        for expressao in ctx.expressao():
            if i > 0:
                self.visitor.outfile.write(",")
            self.visitor.outfile.write(self.convertExpressao(expressao.getText()))
        self.visitor.outfile.write(");\n")
        return self.visitChildren(ctx)

    def visitCmdLeia(self, ctx:LAParser.CmdLeiaContext):
        for identificador in ctx.identificador():
            if self.visitor.identificadores[identificador.getText()] != "literal":
                self.visitor.outfile.write("    scanf(\"")
                tipo = self.converteTipoLeitura(self.visitor.identificadores[identificador.getText()])
                self.visitor.outfile.write(tipo + "\", &" + identificador.getText() + ");\n")
            else:
                self.visitor.outfile.write("    gets(" + identificador.getText() + ");\n")
        return self.visitChildren(ctx)
    
    def visitCmdAtribuicao(self, ctx:LAParser.CmdAtribuicaoContext):
        if ctx.POINTER():
            self.visitor.outfile.write("    *" + ctx.identificador().getText() + " = " + ctx.expressao().getText() + ";\n")
        else:
            if "." in ctx.identificador().getText():
                reg = ctx.identificador().getText().split(".")[0]
                var = ctx.identificador().getText().split(".")[1]
                if reg in self.visitor.identificadores:
                            if var in self.visitor.identificadores[reg]:
                                tipo = self.converteTipo(self.visitor.identificadores[reg][var])
                                if tipo == "char":
                                    self.visitor.outfile.write("    strcpy(" + ctx.identificador().getText() + "," + ctx.expressao().getText() + ");\n")
                                else:
                                    self.visitor.outfile.write("    " + ctx.identificador().getText() + " = " + ctx.expressao().getText() + ";\n")
            else:
                self.visitor.outfile.write("    " + ctx.identificador().getText() + " = " + ctx.expressao().getText() + ";\n")
        return self.visitChildren(ctx)
    
    def visitCmdSe(self, ctx:LAParser.CmdSeContext):
        self.visitor.outfile.write("    if(" + self.convertExpressao(ctx.expressao().getText()) + ") {\n   ")
        for cmd in ctx.cmd1:
            self.visitCmd(cmd)
        self.visitor.outfile.write("    }\n")
        if "senao" in ctx.getText():
            self.visitor.outfile.write("    else {\n    ")
            for cmd in ctx.cmd2:
                self.visitCmd(cmd)
            self.visitor.outfile.write("    }\n")
    
    def visitCmdCaso(self, ctx:LAParser.CmdCasoContext):
        self.visitor.outfile.write("    switch(" + ctx.exp_aritmetica().getText() + ") {\n")
        for selecao in ctx.selecao().item_selecao():
            self.visitConstantes(selecao.constantes())
            for cmd in selecao.cmd():
                self.visitor.outfile.write("        ")
                self.visitCmd(cmd)
            self.visitor.outfile.write("        break;\n")
        if ctx.cmd():
            self.visitor.outfile.write("    default:\n")
            for cmd in ctx.cmd():
                self.visitor.outfile.write("        ")
                self.visitCmd(cmd)
        self.visitor.outfile.write("    }\n")
    
    def visitConstantes(self, ctx: LAParser.ConstantesContext):
        for intervalo in ctx.numero_intervalo():
            comeco = int(intervalo.NUM_INT(0).getText())
            if intervalo.op_unario1:
                comeco = -comeco
            if intervalo.op_unario2:
                fim = -int(intervalo.NUM_INT(1).getText())
            elif intervalo.NUM_INT(1):
                fim = int(intervalo.NUM_INT(1).getText())
            else:
                fim = comeco
            for i in range(comeco, fim + 1):
                self.visitor.outfile.write(f"       case {i}:\n")
        return None

    def convertExpressao(self, expressao):
        if not ("<=" in expressao or ">=" in expressao):
            expressao = expressao.replace("=", "==")
        expressao = expressao.replace(" e ", "&&")
        expressao = expressao.replace(" ou ", "||")
        expressao = expressao.replace("nao", "!")
        expressao = expressao.replace("<>", "!=")
        return expressao

    def evalExpressao(self, expressao, identFunc = None):
        opArit = ['+', '-', '/', '*', '%']
        opRelLog = ['>', '<', '<=', '>=', '<>', '=', 'e', 'ou', 'nao']
        if any(ext in expressao for ext in opRelLog):
            return "%d"
        if any(ext in expressao for ext in opArit):
            expressao = expressao.replace('+', ' ')
            expressao = expressao.replace('-', ' ')
            expressao = expressao.replace('*', ' ')
            expressao = expressao.replace('/', ' ')
            expressao = expressao.replace('%', ' ')
            variaveis = expressao.split(' ')
            for variavel in variaveis:
                if variavel in self.visitor.identificadores:
                    if self.visitor.identificadores[variavel] == "real":
                        return "%f"
                if identFunc:
                    if variavel in self.visitor.funcoes[identFunc]["parametros"]:
                        if self.visitor.funcoes[identFunc]["parametros"][variavel] == "real":
                            return "%f"
            return "%d"
        
    def visitCmdPara(self, ctx:LAParser.CmdParaContext):
        ident = ctx.IDENT().getText()
        self.visitor.outfile.write("    for(" + ident + "=" + self.convertExpressao(ctx.exp_aritmetica1.getText()) + "; " + ident + "<=" + self.convertExpressao(ctx.exp_aritmetica2.getText()) + "; " + ident + "++) {\n   ")
        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        self.visitor.outfile.write("    }\n")

    def visitCmdEnquanto(self, ctx:LAParser.CmdEnquantoContext):
        self.visitor.outfile.write("   while(" + self.convertExpressao(ctx.expressao().getText()) + ") {\n    ")
        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        self.visitor.outfile.write("    }\n")

    def visitCmdFaca(self, ctx:LAParser.CmdFacaContext):
        self.visitor.outfile.write("    do {\n  ")
        for cmd in ctx.cmd():
            self.visitCmd(cmd)
        self.visitor.outfile.write("    } while (" + self.convertExpressao(ctx.expressao().getText()) + ");\n")
    
    def visitCmdEscreva(self, ctx:LAParser.CmdEscrevaContext, identFunc = None):
        self.visitor.outfile.write("    printf(")
        hasStringFirst = False
        notStringFirst = False
        if not ctx.SEPARETOR():
            for expressao in ctx.expressao():
                if expressao.getText() in self.visitor.identificadores:
                    tipo = self.converteTipoLeitura(self.visitor.identificadores[expressao.getText()])
                    self.visitor.outfile.write("\"" + tipo + "\", " + expressao.getText() + ");\n")
                else:
                    if "\"" in expressao.getText():
                        self.visitor.outfile.write(expressao.getText() + ");\n")
                    elif "(" in expressao.getText():
                        nomefunc = expressao.getText().split("(")[0]
                        tipo = self.converteTipoLeitura(self.visitor.funcoes[nomefunc]["tipo"])
                        #self.visitCmdChamada(expressao.termo_logico()[0].fator_logico()[0].parcela_logica().exp_relacional().exp_aritmetica()[0].termo()[0].fator()[0].parcela()[0].parcela_unario())
                        self.visitor.outfile.write("\"" + tipo + "\", " + expressao.getText() + ");\n")
                    else:
                        tipo = self.evalExpressao(expressao.getText(), identFunc)
                        self.visitor.outfile.write("\"" + tipo + "\", " + expressao.getText() + ");\n")
        else:
            for expressao in ctx.expressao():
                if hasStringFirst and notStringFirst:
                    self.visitor.outfile.write("    printf(")
                    hasStringFirst = False
                    notStringFirst = False
                if "\"" in expressao.getText():
                    hasStringFirst = True
                    if not notStringFirst:
                        self.visitor.outfile.write("\"" + expressao.getText().replace("\"", ""))
                    else:
                        self.visitor.outfile.write("    printf(" + expressao.getText() + ");\n") 
                else:
                    notStringFirst = True
                    if expressao.getText() in self.visitor.identificadores:
                        tipo = self.converteTipoLeitura(self.visitor.identificadores[expressao.getText()])
                        if hasStringFirst:
                            self.visitor.outfile.write(tipo + "\", " + expressao.getText() + ");\n")
                        else:
                            self.visitor.outfile.write("\"" + tipo + "\", " + expressao.getText() + ");\n")
                    if identFunc:
                        if expressao.getText() in self.visitor.funcoes[identFunc]["parametros"]:
                            tipo = self.converteTipoLeitura(self.visitor.funcoes[identFunc]["parametros"][expressao.getText()])
                            self.visitor.outfile.write("\"" + tipo + "\", " + expressao.getText() + ");\n")
                    if "." in expressao.getText():
                        reg = expressao.getText().split(".")[0]
                        var = expressao.getText().split(".")[1]
                        if reg in self.visitor.identificadores:
                            if var in self.visitor.identificadores[reg]:
                                tipo = self.converteTipoLeitura(self.visitor.identificadores[reg][var])
                                if hasStringFirst:
                                    self.visitor.outfile.write(tipo + "\", " + expressao.getText() + ");\n")
                                else:
                                    self.visitor.outfile.write("\"" + tipo + "\", " + expressao.getText() + ");\n")
                    if "(" in expressao.getText():
                        nomefunc = expressao.getText().split("(")[0]
                        tipo = self.converteTipoLeitura(self.visitor.funcoes[nomefunc]["tipo"])
                        self.visitor.outfile.write("\"" + tipo + "\", " + expressao.getText() + ");\n")


        return self.visitChildren(ctx)

    def converteTipo(self, tipoLA):
        if tipoLA == "inteiro":
            tipoC = "int"
        elif tipoLA == "real":
            tipoC = "float"
        elif tipoLA == "literal":
            tipoC = "char"
        elif tipoLA == "^inteiro":
            tipoC = "int*"
        elif tipoLA in self.visitor.customTipos:
            tipoC = tipoLA
        return tipoC
    
    def converteTipoLeitura(self, tipoLA):
        if tipoLA == "inteiro":
            tipoC = "%d"
        elif tipoLA == "real":
            tipoC = "%f"
        elif tipoLA == "literal":
            tipoC = "%s"
        return tipoC


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
    generator = Generator(visitor)
    lexer.addErrorListener(LexerErrorListener(output))
    parser.addErrorListener(ParserErrorListener(output))
    generator.handle(val)
    output.close()

    
       

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        logging.error(error)
