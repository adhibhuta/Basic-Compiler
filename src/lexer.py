from enum import Enum
import sys

class Lexer:
    def __init__(self, source):
        self.source = source + '\n'
        self.cur_pos = -1
        self.cur_char = '\0'
        self.next_char()
    def peek(self):
        if self.cur_pos+1 >= len(self.source):
            return '\0'
        return self.source[self.cur_pos+1]
    def next_char(self):
        self.cur_pos += 1
        if self.cur_pos >= len(self.source):
            self.cur_char = '\0'
        else:
            self.cur_char = self.source[self.cur_pos]
    def abort(self, message):
        sys.exit(f"Lexer exiting with message:{message}")
    def remove_whitespaces(self):
        while self.cur_char == ' 'or self.cur_char == '\t' or self.cur_char == '\r':
            self.next_char()
    def remove_comments(self):
        if self.cur_char == '#':
            while self.cur_char != '\n':
                self.next_char()
    def get_token(self):
        self.remove_whitespaces()
        self.remove_comments()
        token = None
        if self.cur_char == '+':
            token = Token(self.cur_char, TokenType.PLUS)
        elif self.cur_char == '-':
            token = Token(self.cur_char, TokenType.MINUS)
        elif self.cur_char == '*':
            token = Token(self.cur_char, TokenType.ASTERISK)
        elif self.cur_char == '/':
            token = Token(self.cur_char, TokenType.SLASH)
        elif self.cur_char == '\n':
            token = Token(self.cur_char, TokenType.NEWLINE)
        elif self.cur_char == '\0':
            token = Token(self.cur_char, TokenType.EOF)
        elif self.cur_char == '=':
            # We need to check weather the token is a = or ==
            if self.peek() == '=':
                last_char = self.cur_char
                self.next_char()
                token = Token(last_char+self.cur_char, TokenType.EQEQ)
            else:
                token = Token(self.cur_char, TokenType.EQ)
        elif self.cur_char == '>':
            # We need to check weather the token is a > or >=
            if self.peek() == '=':
                last_char = self.cur_char
                self.next_char()
                token = Token(last_char+self.cur_char, TokenType.GTEQ)
            else:
                token = Token(self.cur_char, TokenType.GT)
        elif self.cur_char == '<':
            # We need to check weather the token is a < or <=
            if self.peek() == '=':
                last_char = self.cur_char
                self.next_char()
                token = Token(last_char+self.cur_char, TokenType.LTEQ)
            else:
                token = Token(self.cur_char, TokenType.LT)
        elif self.cur_char == '!':
            # We need to check weather the token is != and ! alone is not allowed
            if self.peek() == '=':
                last_char = self.cur_char
                self.next_char()
                token = Token(last_char+self.cur_char, TokenType.NOTEQ)
            else:
                self.abort("Found ! instead of !=")
        else:
            self.abort(f"Unknown token {self.cur_char}")
        self.next_char()
        return token

class Token:
    def __init__(self, text, kind):
        self.text = text
        self.kind = kind

class TokenType(Enum):
    '''
    '''
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    # Keywords.
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    # Operators.
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
