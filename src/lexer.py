from enum import Enum

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
    def abort(self):
        pass
    def remove_whitespaces(self):
        pass
    def remove_comments(self):
        pass
    def get_token(self):
        pass #Start fron here

class Token:
    def __init__(self, _text, _kind):
        self,text = _text
        self.kind = _kind

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
    GTEQ = 2
