from src.lexer import Lexer, TokenType
from src.parser import Parser
import sys

def main():
    #input = "LET foobar = 123"
    #input = '''#This is a comment
    #+- */ >>= "  " 1 1.11  .01= !='''
    #input = "IF+-123 foo*THEN/ NONE"
    if len(sys.argv) != 2:
        sys.exit("Please provide a source file")
    
    with open(sys.argv[1], 'r') as f:
        input = f.read()
    
    lexer = Lexer(input)
    parser = Parser(lexer)
    parser.program() 
    
    
    '''
    print(parser)
    token = lexer.get_token()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.get_token()
    '''
main()
