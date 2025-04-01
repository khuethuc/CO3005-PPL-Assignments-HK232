grammar ZCode;

@lexer::header {
# 2252385
from lexererr import *
}

options {
	language=Python3;
}
/* = = = = = SYNTAX ANALYSIS = = = = = */
/* PROGRAM */
program: declare_list EOF;
declare_list: declaration declare_list | declaration;
declaration: variable_decl | function_decl | NEWLINE;

/* VARIABLES DECLARATION */
variable_decl: (var | dynamic | normal_type | array_type) atleast_newline;

var: VAR IDENTIFIER ASSIGN expression;

dynamic: DYNAMIC IDENTIFIER nullable_vardecl_expr;

normal_type: type_list IDENTIFIER nullable_vardecl_expr;
type_list: NUMBER | BOOLEAN | STRING;

array_type: type_list IDENTIFIER OPEN_SQUARE_BRACKET size CLOSE_SQUARE_BRACKET array_rhs;
size: NUMBER_LITERAL COMMA size | NUMBER_LITERAL;
array_rhs: ASSIGN array_literal | ASSIGN expression | ;
array_literal: OPEN_SQUARE_BRACKET array_elements CLOSE_SQUARE_BRACKET;
array_elements: one_element | multiple_elements;
one_element: expression COMMA one_element | expression;
multiple_elements: OPEN_SQUARE_BRACKET one_element CLOSE_SQUARE_BRACKET COMMA multiple_elements | OPEN_SQUARE_BRACKET one_element CLOSE_SQUARE_BRACKET;

parameter_list: parameter_prime | ;
parameter_prime: parameter COMMA parameter_prime| parameter;
parameter: type_list (IDENTIFIER | IDENTIFIER OPEN_SQUARE_BRACKET size CLOSE_SQUARE_BRACKET);

nullable_vardecl_expr: ASSIGN expression | ;

/* NEWLINE DECLARATION */
atleast_newline: NEWLINE atleast_newline | NEWLINE;
nullable_newline: atleast_newline | ;

/* FUNCTION DECLARATION */
function_decl: FUNC IDENTIFIER OPEN_ROUND_BRACKET parameter_list CLOSE_ROUND_BRACKET function_body;
function_body: atleast_newline | nullable_newline return_stmt | nullable_newline block_stmt;

/* STATEMENT */
statement: variable_decl_stmt | assignment_stmt | break_stmt | if_stmt | for_stmt | continue_stmt | return_stmt | function_call_stmt | block_stmt;

variable_decl_stmt: var | dynamic | normal_type | array_type;

assignment_stmt: assignment_type ASSIGN expression;
assignment_type: IDENTIFIER | index_operators_expr;

if_stmt: IF OPEN_ROUND_BRACKET expression CLOSE_ROUND_BRACKET nullable_newline statement elif_list else_list;
elif_list: atleast_newline elif_part elif_list | ;
elif_part: ELIF OPEN_ROUND_BRACKET expression CLOSE_ROUND_BRACKET nullable_newline statement; 
else_list: atleast_newline else_part | ;
else_part: ELSE nullable_newline statement;

for_stmt: FOR IDENTIFIER UNTIL expression BY expression nullable_newline statement;

break_stmt: BREAK;

continue_stmt: CONTINUE;

return_stmt: RETURN | RETURN expression;

function_call_stmt: IDENTIFIER OPEN_ROUND_BRACKET expression_list CLOSE_ROUND_BRACKET;

block_stmt: BEGIN atleast_newline block_body END;
block_body: statement atleast_newline block_body | ;

/* EXPRESSION */
expression_list: expression_prime COMMA expression_list | expression_prime;
expression_prime: expression | ;

expression: expression2 CONCAT expression2 | expression2;
expression2: expression3 relational_sign expression3 | expression3;
expression3: expression3 (AND | OR) expression4 | expression4;
expression4: expression4 (PLUS | MINUS) expression5 | expression5;
expression5: expression5 (MUL | DIV | MOD) expression6 | expression6;
expression6: NOT expression6 | expression7;
expression7: (MINUS | PLUS) expression7 | expression8;
expression8: expression8 index_operators_expr | expression9;
expression9: IDENTIFIER | NUMBER_LITERAL | TRUE | FALSE | STRING_LITERAL | array_literal | index_operators_expr | function_call_expr | sub_expr;

relational_sign: EQUAL | EQUAL_STRING | NEQ | LESS | GREATER | LEQ | GEQ;

index_operators_expr: (IDENTIFIER | function_call_expr) OPEN_SQUARE_BRACKET index_operators CLOSE_SQUARE_BRACKET;
index_operators: expression COMMA index_operators | expression;

function_call_expr: IDENTIFIER OPEN_ROUND_BRACKET expression_list CLOSE_ROUND_BRACKET;

sub_expr: OPEN_ROUND_BRACKET expression CLOSE_ROUND_BRACKET;

/* = = = = = LEXICAL ANALYSIS = = = = = */
/* * * KEYWORDS, OPERATORS, SEPARATORS * * */
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOLEAN: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
WHILE: 'while';
NOT: 'not';
AND: 'and';
OR: 'or';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '=';
NEQ: '!=';
LESS: '<';
GREATER: '>';
LEQ: '<=';
GEQ: '>=';
ASSIGN: '<-';
CONCAT: '...';
EQUAL_STRING: '==';
OPEN_ROUND_BRACKET: '(';
CLOSE_ROUND_BRACKET: ')';
OPEN_SQUARE_BRACKET: '[';
CLOSE_SQUARE_BRACKET: ']';
COMMA: ',';

/* * * IDENTIFIER * * */
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

/* * * LITERALS * * */
NUMBER_LITERAL: INTEGER DECIMAL? EXPONENT?;
fragment INTEGER: [0-9]+;
fragment DECIMAL: '.'[0-9]*;
fragment EXPONENT: [eE][+-]?[0-9]+;
// BOOLEAN_LITERAL: TRUE | FALSE;
STRING_LITERAL: '"' LEGAL_CHARACTER* '"' {self.text = self.text[1:-1];};
fragment DOUBLE_QUOTE: '\'"';
fragment LEGAL_CHARACTER: ~["\r\n\\] | '\\'[bfrnt\\'] | DOUBLE_QUOTE;

/* * * COMMENT AND SPECIAL CHARACTERS * * */
NEWLINE: '\n';
COMMENT: '##' ~[\n\r\f]* -> skip;
WHITE_SPACE : [ \t\b\f\r]+ -> skip ;

/* * * ERRORS * * */
UNCLOSE_STRING: '"' LEGAL_CHARACTER* ('\r\n' | '\n' | EOF) '"'
{
	index = self.text.find('\n')
	if self.text.find('\r') == index - 1:
	    raise UncloseString(self.text[1:index - 1])
	else:
		raise UncloseString(self.text[1:index])
};
ILLEGAL_ESCAPE: '"' LEGAL_CHARACTER* ('\r' | '\\' ~[bfrnt\\'] | '\\') '"'
{
    raise IllegalEscape(self.text[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};