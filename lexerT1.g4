grammar lexerT1;

KEYWORDS: 'algoritmo' | 'fim_algoritmo' | 'declare' | 'literal' | 'inteiro' |
        'leia' | 'escreva' | 'real' | 'logico' | 'enquanto' | 'fim_enquanto' |
        'se' | 'entao' | 'senao' | 'fim_se' | 'caso' |
        'seja' | 'fim_caso' | 'para' | 'ate' | 'faca' | 'fim_para' |
        'registro' | 'fim_registro' | 'tipo' | 'procedimento' | 'var' | 'fim_procedimento' |
        'funcao' | 'retorne' | 'fim_funcao' | 'constante' | 'falso' | 'verdadeiro';

OP_REL: '>'|'>='|'<'| '<='|'<>'|'=';
OP_ARITH: '-'|'+'|'*'|'/'| '%';
OP_LOGIC: 'e'|'ou'|'nao';

NUM_INT: [0-9]+ ;
NUM_REAL: NUM_INT '.' NUM_INT;
IDENT: ([a-zA-Z])([a-zA-Z]|[0-9])*('_')?(([a-zA-Z]|[0-9])*);
CADEIA: '"' ~('"'|'\r'|'\n')* '"';


PARENTHESES: '('|')';
SQUARE_BRACKETS: '[' | ']';
REANGE: '..';
ATTRIBUTE: '.';
DELIMIT: ':';
SEPARETOR: ',';
ATRIBUITION: '<-';
ADDRESS: '&';
POINTER: '^';

COMMENT: '{' ~('}'|'{'|'\r'|'\n')* '}' -> skip;
WHITE_SPACE: ([ \t\r\n]) -> skip;
