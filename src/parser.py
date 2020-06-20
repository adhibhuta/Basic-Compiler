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
        while not self.check_token(TokenType.EOF):
            self.statement() #Start from here; write the statement fucntion
    def statement(self):
        if self.check_token(TokenType.PRINT):
            print("PRINT-STATEMENT")
            self.next_token()
            if self.check_token(TokenType.STRING):
                self.next_token()
            else:
                self.experssion()
        elif self.check_token(TokenType.IF):
            print("IF-STATEMENT")
            self.next_token()
            self.comparison()
            self.match(TokenType.THEN)
            self.nl()
            while not self.check_token(TokenType.ENDIF): #Iterate till there is an endif
                self.statement()
            self.match(TokenType.ENDIF)#Make sure ended with endif
        self.nl()
    def nl(self):
        if self.check_token(TokenType.NEWLINE):
            print("NEWLINE-STATEMENT")
            self.next_token()
        while self.check_token(TokenType.NEWLINE):
            self.next_token()


