#The language requires grammer; this is the place where it is maintained
#When any compiler throws syntax error it basically means you didnt follow grammer
'''
TODO :
    - [ ] Instead of returning the whole list of tokenised code
    can we do like a generator
'''
from .lexer import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.cur_token = None
        self.peek_token = None
        self.next_token()
        self.next_token()
    def abort(self, message):
        pass
    #Returns True if current token matches
    def check_token(self, kind):
        return self.cur_token.kind == kind
    #Returns True if next token matches
    def check_peek(self, kind):
        return self.peek_token.kind == kind
    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.lexer.get_token()
    def match(self):
        pass
