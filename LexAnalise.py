import re 
import ply.lex as lex
# defining our tokens using regular expression

tokens=['KEYWORD','IDENTIFIER', 'OPERATOR','LITERAL','PUNCTUATION','WHITESPACE']

# these are the components of the regular expression 
t_KEYWORD= r'int'
t_IDENTIFIER= r'[a-zA-Z_][a-zA-Z]*' #first can be a underscore or smal or acpital leter and second 0 or more small or capital letters 
t_OPERATOR= r'='
t_LITERAL= r'[1-9]\d*'
t_PUNCTUATION= r';'


t_ignore =' \t\n' # this one ignores creating a token for white space

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)  # Skip the illegal character and continue


lexer = lex.lex() # i have created  a lexer 

mystring ="int y = 10;" # the string to be analysed 

lexer.input(mystring)
for token in lexer:
    print(f"type {token.type}, value: {token.value}")

    print( "\n " )
   

mystring2 ="int xy1 = 9;" # wrong  string to be analysed 
   

lexer.input(mystring2)
for token in lexer:
    print( f" type {token.type}, value: {token.value}" )

    
