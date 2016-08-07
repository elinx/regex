from Scanner import *


class Parser:
    """Grammar:

    expr ::= term ((PLUS | MINUS) term)*
    term ::= factor ((MUL | DIV) factor)*
    factor ::= NUM
    """
    class AST:
        def __init__(self, value, left, right):
            self.value = value
            self.left = left
            self.right = right

        def __repr__(self, level=0):
            ret = '\t' * level + str(self.value) + '\n'
            if self.left is not None:
                ret += self.left.__repr__(level + 1)
            if self.right is not None:
                ret += self.right.__repr__(level + 1)
            return ret

        def show(self, level=0):
            print('\t' * level + str(self.value))
            if isinstance(self.left, Parser.AST):
                self.left.show(level + 1)
            else:
                print('\t' * level + str(self.left))

            if isinstance(self.right, Parser.AST):
                self.right.show(level + 1)
            else:
                print('\t' * level + str(self.right))

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.ast = None

    def __repr__(self):
        pass

    def consume(self):
        token = None
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1
        return token

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def factor(self):
        """factor ::= [0-9]*"""
        val = self.peek()[1]
        if val == Scanner.NUM:
            return self.AST(self.consume()[0], None, None)
        return None

    def term(self):
        """term ::= factor ((MUL | DIV) factor)*"""
        term_ast = self.factor()

        token = self.peek()
        while token is not None and token[1] == Scanner.OP and \
                (token[0] == '*' or token[0] == '/'):
            op = self.consume()
            right = self.factor()
            new_ast = self.AST(op[0], term_ast, right)
            term_ast = new_ast
            token = self.peek()

        return term_ast

    def expr(self):
        """expr ::= term ((PLUS | MINUS) term)*"""
        expr_ast = self.term()

        token = self.peek()
        while token is not None and token[1] == Scanner.OP and \
                (token[0] == '+' or token[0] == '-'):
            op = self.consume()
            right = self.term()
            new_ast = self.AST(op[0], expr_ast, right)
            expr_ast = new_ast
            token = self.peek()

        return expr_ast

    def parse(self):
        return self.expr()

    def exec(self, ast):
        if str(ast.value) not in '+-*/':
            return ast.value
        left = self.exec(ast.left)
        right = self.exec(ast.right)
        return {
            '+': left + right,
            '-': left - right,
            '*': left * right,
            '/': left / right
        }[ast.value]

if __name__ == '__main__':
    scanner = Scanner('1 - 2 * 3 + 6')
    scanner.lex()

    parser = Parser(scanner.tokens)
    print(parser.exec(parser.parse()))
