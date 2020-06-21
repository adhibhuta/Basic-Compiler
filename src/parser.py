#The language requires grammer; this is the place where it is maintained
#When any compiler throws syntax error it basically means you didnt follow grammer
'''
TODO :
    - [ ] Instead of returning the whole list of tokenised code
    can we do like a generator
'''
from .lexer import *
import sys

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.cur_token = None
        self.peek_token = None
        self.next_token()
        self.next_token()
    def abort(self, message):
        sys.exit(f"Parser Aborting Reason: {message}")
    #Returns True if current token matches
    def check_token(self, kind):
        return self.cur_token.kind == kind
    #Returns True if next token matches
    def check_peek(self, kind):
        return self.peek_token.kind == kind
    #Gives the next token
    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.lexer.get_token()
    #Tries to match return True if does and moves to next token else aborts
    def match(self, kind):
        if not self.check_token(kind):
            self.abort(f"Expected {kind.name} got {self.cur_token.kind.name}")
        self.next_token()
        return True
    def program(self):
        print("PROGRAM")
        while self.check_token(TokenType.NEWLINE):
            self.next_token()
        while not self.check_token(TokenType.EOF):
            self.statement() #Start from here; write the statement fucntion
    def statement(self):
        if self.check_token(TokenType.PRINT):
            print("PRINT-STATEMENT")
            self.next_token()
            if self.check_token(TokenType.STRING):
                self.next_token()
            else:
                self.expression()
        elif self.check_token(TokenType.IF):
            print("IF-STATEMENT")
            self.next_token()
            self.comparison()
            self.match(TokenType.THEN)
            self.nl()
            while not self.check_token(TokenType.ENDIF): #Iterate till there is an endif
                self.statement()
            self.match(TokenType.ENDIF)#Make sure ended with endif
        elif self.check_token(TokenType.WHILE):
            print("WHILE-STATEMENT")
            self.next_token()
            self.comparison()
            self.match(TokenType.THEN)
            self.nl()
            while not self.check_token(TokenType.ENDWHILE):
                self.statement()
            self.match(TokenType.ENDWHILE)
        elif self.check_token(TokenType.LABEL):
            print("LABEL-STATEMENT")
            self.next_token()
            self.match(TokenType.IDENT)
        elif self.check_token(TokenType.GOTO):
            print("GOT-STATEMENT")
            self.next_token()
            self.match(TokenType.IDENT)
        elif self.check_token(TokenType.LET):
            print("LET-STATEMENT")
            self.next_token()
            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)
            self.expression()
        elif self.check_token(TokenType.INPUT):
            print("INPUT-STATEMENT")
            self.next_token()
            self.match(TokenType.IDENT)
        else:
            self.abort("Invalid statement " + self.cur_token.text + " (" + self.cur_token.kind.name + ")")
        self.nl()
    def nl(self):
        print("NEWLINE-STATEMENT")
        self.match(TokenType.NEWLINE)
        while self.check_token(TokenType.NEWLINE):
            self.next_token()
    def is_comparison_operator(self):
        return self.check_token(TokenType.GT) or self.check_token(TokenType.GTEQ) or self.check_token(TokenType.LT) or self.check_token(TokenType.LTEQ) or self.check_token(TokenType.EQEQ) or self.check_token(TokenType.NOTEQ)

    def comparison(self):
        print("COMPARISON-STATEMENT")
        self.expression()

        if self.is_comparison_operator():
            self.next_token()
            self.expression()
        while self.is_comparison_operator():
            self.next_token()
            self.expression()
    def expression(self):
        print("EXPRESSION-STATEMENT")
        self.term()
        while self.check_token(TokenType.PLUS) or self.check_token(TokenType.MINUS):
            self.next_token()
            self.term()
    def term(self):
        print("TERM-STATEMENT")
        self.unary()
        while self.check_token(TokenType.ASTERISK) or self.check_token(TokenType.SLASH):
            self.next_token()
            self.unary()
    def unary(self):
        print("UNARY-STATEMENT")
        if self.check_token(TokenType.PLUS) or self.check_token(TokenType.MINUS):
            self.next_token()
        self.primary()
    def primary(self):
        print("PRIMARY (" + self.cur_token.text + ")")

        if self.check_token(TokenType.NUMBER):
            self.next_token()
        elif self.check_token(TokenType.IDENT):
            self.next_token()
        else:
            self.abort("Unexpected token at " + self.cur_token.text)
