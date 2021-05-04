from yapl_lexer import *
from yapl_parser import *
import sys

# other global variables

variables={}


def exp_eval(p): # evaluate expression
    operator = p[0]
#    print("it is here")
  
    if p[0]=="var":
#        print("variable return statement")
#        print(variables[p[1]][-1])
#        print("variable return statement",variables[p[1][0]])
        return variables[p[1]][-1] 
    if operator == '+':
#        print("it is here")
        return exp_eval(p[1]) + exp_eval(p[2])
    elif operator == '-':
        return exp_eval(p[1]) - exp_eval(p[2])
    elif operator == '*':
        return exp_eval(p[1]) * exp_eval(p[2])
    elif operator == '/':
        if exp_eval(p[2])==0:
            print( "division by zero")  
            sys.exit()
        else:        
   #        print("here")
            return exp_eval(p[1]) / exp_eval(p[2]) 
    elif operator == '%':
        return exp_eval(p[1]) % exp_eval(p[2])
    elif operator == '^':
        return exp_eval(p[1]) ** exp_eval(p[2])   
    elif p[0] == '<':
        return exp_eval(p[1])< exp_eval(p[2])
    elif p[0] == '<=': 
        return exp_eval(p[1]) <= exp_eval(p[2])
    elif p[0] == '>=':
        return exp_eval(p[1]) >= exp_eval(p[2])
    elif p[0] == '>':
        return exp_eval(p[1])> exp_eval(p[2]) 
    elif p[0] == '&':
        return exp_eval(p[1]) and exp_eval(p[2])
    elif p[0] == '|':
        return exp_eval(p[1]) or exp_eval(p[2])
    elif p[0] == '==':
        return exp_eval(p[1])== exp_eval(p[2])  
    elif p[0] == '!=':
        return exp_eval(p[1]) != exp_eval(p[2])
    elif p[0] == "!":
        return (not exp_eval(p[1]))


    else: # operator was 'NUM' so its just a number
        return p[1]


def stmt_eval(p): # p is the parsed statement subtree / program
    stype = p[0] # node type of parse tree
 
    if stype == '++':
#          print("increment")
#          print(p)
          if p[1] not in variables.keys():
              print("Variable does not exist")
          else:
#              print("increment the variable",variables[p[1]])
#              print(variables[p[1]])    
              if variables[p[1]][0] == 'Int':
#                  print("it is an integer",variables[p[1]][-1])
                  number =variables[p[1]][-1]+1
                  variables[p[1]].append(number)
#                  print(variables[p[1]][-1])
                  return number
                  
              else:
                  print("Cannot be incremented : type error")
    if stype == '--':
#        print("decrement")
#          print(p)
          if p[1] not in variables.keys():
              print("Variable does not exist")
          else:
#              print("increment the variable",variables[p[1]])
#              print(variables[p[1]])    
              if variables[p[1]][0] == 'Int':
#                  print("it is an integer",variables[p[1]][-1])
                  number =variables[p[1]][-1]-1
                  variables[p[1]].append(number)
#                  print(variables[p[1]][-1])
                  return number
                  
              else:
                  print("Cannot be incremented : type error")                 



    if stype == 'variable_dec':
#        print("it will print")
#        print(p[2])
        
        if p[2] not in variables.keys():
#            print("here")
            
            variables[p[2]]= [p[1],None]
            print("variables ",variables)
            # print(p[1],p[2])
            return[p[1],p[2]]        
        else:
            print("variables ",variables)

            print("redeclaration error")
#            print(variables.keys())   


    if stype == 'var_assign':
        # print("it will print")
        if type(p[1]) != tuple:
#            print("this is when the variable is declared and not assigned")
#            print(p)
#            print("asdsdsadfsdfsadf",p[2][1])
#            print(variables.keys())
            if p[1] not in variables.keys():
                print("variable has not been declared ")
            else:
                # print("assigned")
                # print(p[1])
                # print(p[2][1])
                variables[p[1]].append(p[2][1]) 
#                print(variables)

        elif type(p[1]) == tuple:
            if p[1][2] not in variables.keys():
#                print("here2 declare ")
#                print(p)
                variables[p[1][2]]= [p[1][1],None]
#                print(variables)
#                print("it comes here")
                variables[p[1][2]].append(p[2][1]) 
#                print("it comes here")
#            print(variables[p[2][1]])
#            print(variables[p[1][2]])
            
#            print("it comes here")  
            else:
                print("redeclaration error")
#            print(p)
            
            
  
    if stype == 'PRINT': 

#        print("it is here")
        # print(p[1])
        exp = p[1]
#      print("it is here")
#        print(p)   
 #       print("p1is",p[1])   
        # print("it is here2")  
 #       print(p)
        result = ""
 #       print("it is here")
        for args in p[1]:
#            print(exp_eval(args))
            result= result +str(exp_eval(args)) + " "

#        print("the print function is",result)
        # print("it is here3")
        print(result)
   
            # print("this is when the variable is declared and assigned")




def run_program(p): # p[0] == 'Program': a bunch of statements
    for stmt in p: # statements in proglist
        if stmt != None:
            stmt_eval(stmt) # statement subtree as tuple
#    print(p)

if len(sys.argv) == 1:
    print('File name/path not provided as cmd arg.')
    exit(1)

while True:
    fileHandler = open(sys.argv[1],"r")
    userin = fileHandler.read()
    fileHandler.close()

    print("Welcome to your YAPL's Interpreter!")
    parsed = parser.parse(userin)
    if not parsed:
        continue
    
    for line in userin.split('\n'):
        print(line)
    print("=========================================\n{OUTPUT}")
    try:
        run_program(parsed)
    except Exception as e:
        print(e)
    
    input("Press any key to run code again.")


exit()