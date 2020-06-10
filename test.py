from src.lexer import Lexer

def main():
	input = "LET foobar = 123"
	lexer = Lexer(input)

	while lexer.peek() != '\0':
		print(lexer.cur_char)
		lexer.next_char()

main()
