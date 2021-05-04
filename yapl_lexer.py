import ply.lex as lex
import re

# TOKEN IDENTIFIERS, have to match name of our token

# list of all possible tokens
tokens = [
    'INT',
    'FLOAT',
    'CHAR',
    'EQUAL',
    'STRING',
    'BOOL',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'MODULO',
    'TYP_INT',
    'TYP_STRING',
    'TYP_BOOL',
    'TYP_CHAR',
    'TYP_FLOAT',
    'True',
    'False',
    'POWER',
    'INCREMENT',
	'DECREMENT',
    'AND',
    'NOT',
    'OR',
    'EEQUAL',
    'LT',
    'GT',
    'LTE',
    'GTE',
    'NEQUAL',
    'IDENTIFIER',
    'IF',
    'ELSEIF',
    'ELSE',
    'LP',
    'RP',
    'SEMICOL',
    'COMMA',
    'PRINT'
   
]

t_PLUS = r'\+' # recognise regular expression symbol
t_MINUS = r'\-'
t_MULT= r'\*'
t_DIV=r'\/'
t_SEMICOL = r'\;'
t_EQUAL= r'\='
t_AND=r'\&'
t_LP=r'\('
t_RP=r'\)'  
t_NOT= r'\!'
t_POWER=r'\^'
t_INCREMENT=r'\+\+'
t_DECREMENT=r'\-\-'
t_MODULO=r'\%'
t_OR= r'\|'
t_EEQUAL = r'\=\='
t_NEQUAL = r'\!\='
t_LT = r'\<'
t_GT = r'\>'
t_LTE = r'\<\='
t_GTE = r'\>\='

t_COMMA=r'\,'

t_ignore = ' \t\r\n\f\v' # ignore spaces, better lexing performance, special case

# variable or function names (including predefined functions like print)


def t_TYP_INT(t):
    r'Int'
    return t


def t_TYP_STRING(t):
    r'String'
    return t


def t_TYP_CHAR(t):
    r'Char'
    return t


def t_TYP_FLOAT(t):
    r'Float'
    return t


def t_TYP_BOOL(t):
    r'Bool'
    t.type = 'TYP_BOOL'
    return t


def t_BOOL(t):
	r'False|True'
	
	if t.value == 'False':
		t.value = False
	else:
		t.value = True
	return t
def t_ELSEIF(t):
    r'ELSEIF'
    return t


def t_IF(t):
    r'IF'
    return t

def t_ELSE(t):
    r'ELSE'
    return t


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value == 'print':
        t.type = 'PRINT'
   
    else:
        t.type = 'IDENTIFIER'
        
    return t

# def t_IDENTIFIER(t):
#     r'[a-zA-z_][a-zA-Z_0-9]*'
#     return t
def t_FLOAT(t): # parameter t is the token
    r'\d*\.\d+' # decimal nums    
    t.value = float(t.value) # convert to float
    return t



def t_INT(t): # parameter t is the token
    r'\d+' # atleast one digit
    t.value = int(t.value) # convert to int
    return t


def t_CHAR(t): 
    r'\'[A-Za-z]\''
    return t

def t_STRING(t):
    r'\"(.*?)\"'
    t.value = t.value[1:-1]
    return t


def t_lineno(t):
    r'\n'
    t.lexer.lineno += len(t.value) 


def t_error(t): # error while lexing
    print("[Lexer Error] Line",t.lineno)
    print(f"Illegal character: {t.value}")
    t.lexer.skip(1) # skips illegal character

# create lexer
lexer = lex.lex()

# ENABLE THIS TO TEST YOUR LEXER DIRECTLY
# while True:
#     print("YAPL_LEXER>>",end='')
#     lexer.input(input()) # reset lexer, store new input
        
#     while True: # necessary to lex all tokens
#         tokenEntered = lexer.token() # return next token from lexer
#         if not tokenEntered: # lexer error also given
#             break
#         print(tokenEntered)
