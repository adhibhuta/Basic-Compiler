from src.lexer import Lexer, TokenType

def main():
    #input = "LET foobar = 123"
    input = '''#This is a comment
    +- */ >>= = !='''
    lexer = Lexer(input)
    token = lexer.get_token()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.get_token()

main()
