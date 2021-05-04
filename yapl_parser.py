import ply.yacc as yacc
from yapl_lexer import *

#sys.tracebacklimit = 0 # to prevent traceback debug output since it is not needed

# to resolve ambiguity, individual tokens assigned a precedence level and associativity. 
# tokens ordered from lowest to highest precedence, rightmost terminal judged
precedence = (
    ('left', 'PLUS', 'MINUS'),  # +, - same precedence, left associative
    ('left', 'MULT', 'DIV'),
    ('left','OR','AND'),
    ('left', 'EQUAL', 'NEQUAL'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('right', 'NOT'),
    
)

start = 'S'
# multiple variables, assigning data from one variable to another

# after the lexing, start parsing

def p_start(p): # non-terminal, starting
    """
    S : stmt S
    """
    p[0] = [p[1]] + p[2] # list comprehension used to solve recursive grammar, added/appending as well
    

def p_start_empty(p):
    """
    S :
    """
    p[0] = []



def p_exp_not(p):
    """ 
    exp : NOT exp 

    """
    p[0]=('not',p[2])




def p_stmt(p):
    '''
             stmt   :     var_assign
                    |     variable_dec
    ''' 
   
    p[0] = p[1]

def p_variable_dec(p):
    '''
    variable_dec    : TYP_INT IDENTIFIER  
                    | TYP_FLOAT IDENTIFIER 
                    | TYP_STRING IDENTIFIER 
                    | TYP_BOOL IDENTIFIER 
                    | TYP_CHAR IDENTIFIER
    '''
    p[0] = ("variable_dec", p[1], p[2])


def p_var_assign(p):
    '''
    var_assign      : variable_dec EQUAL exp
                    | IDENTIFIER EQUAL exp 
                  
            
    '''
    p[0] = ('var_assign', p[1], p[3])
    #p[0] = ("var_assign",p[1][1], p[1][2], p[3])



# def p_print_stmt(p):
#     """
#     stmt : PRINT exp SEMICOL


#     """
# #    print("printhing rhis ",p)
#     p[0] = ('PRINT', p[2])

def p_print(p):
    '''
        stmt  : PRINT arg SEMICOL
    '''
    p[0] = ('PRINT', p[2])

def p_arg_second(p):
    '''
       arg  : arg COMMA exp
    '''

    p[1].append(p[3])
    p[0] = p[1]

def p_arg_first(p):
    '''
        arg  : exp
    '''
    p[0] = [p[1]] 









def p_parenthesis(p):
    '''
        exp   :   LP exp RP
    '''
#    print(p)
    p[0] = p[2]


def p_increment_decrement(p):
    '''
    stmt : IDENTIFIER INCREMENT 
         | IDENTIFIER  DECREMENT 
    '''
    
    p[0] = (p[2], p[1])




# def p_if_statement(p):
#     '''
#         if   :   IF 
#     '''
#     p[0] = ('if',p[3],p[6],p[8],p[9])


def p_exp_bin(p):
    """ 
    exp : exp PLUS exp
        | exp MINUS exp
        | exp MULT exp
        | exp DIV exp
        | exp LT exp
        | exp GT exp
        | exp LTE exp
        | exp GTE exp
        | exp NEQUAL exp
        | exp OR exp
        | exp EEQUAL exp
        | exp MODULO exp
        | exp POWER exp

    """
    p[0] = (p[2], p[1], p[3]) # '1+2' -> ('+', '1', '2')



def p_exp_num(p):
    """
    exp : INT
        | FLOAT 
        | CHAR
        | STRING 
        | BOOL
    """
    p[0] = ('NUM', p[1])


def p_IDENTIFIER(p):
    """
    exp :  IDENTIFIER
    """
#    print("this is identifier",p)
    p[0] = ('var', p[1])



def p_error(p):
    print("Syntax error at token", p.value, p.type, p.lexpos)
    exit(1)

parser = yacc.yacc() # start parsing, yacc object created
