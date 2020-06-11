from src.lexer import Lexer, TokenType
from src.parser import Parser
def main():
    #input = "LET foobar = 123"
    #input = '''#This is a comment
    #+- */ >>= "  " 1 1.11  .01= !='''
    input = "IF+-123 foo*THEN/ NONE"
    lexer = Lexer(input)
    parser = Parser(lexer)
    print(parser)
    token = lexer.get_token()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.get_token()

main()
