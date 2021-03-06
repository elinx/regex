from SubsetConstruction import *
from NFABuilder import *


class Parser:
    """Grammar(EBNF):

    <regex>  ::= <term> '|' <regex>
              | <term>

    <term>   ::= { <factor> }
    <factor> ::= <base> { '*' }
    <base>   ::= <char>
              | '\' <char>
              | '(' <regex> ')'

    reference: http://matt.might.net/articles/parsing-regex-with-recursive-descent/
    """
    class AST:
        def __init__(self, value, left, right):
            self.value = value
            self.left = left
            self.right = right

        def __repr__(self, level=0):
            ret = '\t' * level + str(self.value[0]) + '\n'
            if self.left is not None:
                ret += self.left.__repr__(level + 1)
            if self.right is not None:
                ret += self.right.__repr__(level + 1)
            return ret

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.ast = None

    def consume(self):
        token = None
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1
        return token

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def base(self):
        """
        <base> ::= <char>
                |  '\' <char>
                |  '(' <regex> ')'

        """
        token = self.peek()
        if token is not None:
            if token[1] == Scanner.LP:
                self.consume()
                r = self.regex()
                self.consume()
                return r
            elif token[1] == Scanner.BS:
                op = self.consume()
                return self.AST(op, self.consume(), None)
            else:
                return self.AST(self.consume(), None, None)

    def factor(self):
        """<factor> ::= <base> { '*' }"""
        factor_ast = self.base()
        token = self.peek()

        while token is not None and token[0] == '*':
            factor_ast = self.AST((Scanner.STAR, Scanner.STAR), factor_ast, None)
            self.consume()
            token = self.peek()
        return factor_ast

    def term(self):
        """<term> ::= { <factor> }"""
        term_ast = None
        token = self.peek()

        while token is not None and \
                token[0] != ')' and token[0] != '|':
            factor_ast = self.factor()
            if term_ast is None:
                term_ast = factor_ast
            else:
                term_ast = self.AST((Scanner.CAT, Scanner.CAT), term_ast, factor_ast)
            token = self.peek()

        return term_ast

    def regex(self):
        """<regex> ::= <term> '|' <regex>
                    |  <term>
        """
        expr_ast = self.term()

        token = self.peek()
        if token is not None and token[1] == Scanner.ALTER:
            op = self.consume()
            right = self.regex()
            expr_ast = self.AST(op, expr_ast, right)

        return expr_ast

    def parse(self):
        self.ast = self.regex()

if __name__ == '__main__':
    scanner = Scanner('(a|b)*abb')
    scanner.lex()

    parser = Parser(scanner.tokens)
    parser.parse()
    # print(parser.ast)

    nfa = NFABuilder.ast_to_nfa(parser.ast)
    # print(nfa)

    sctor = SubsetConstruction(nfa)
    dfa = sctor.build_dfa(scanner.syms())
    # print(dfa)

    res = dfa.match('abb')

    print(res)
