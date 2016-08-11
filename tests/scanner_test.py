import unittest
from Scanner import *


class TestScanner(unittest.TestCase):

    def common_lex(self, inputs, expect):
        s = Scanner(inputs)
        s.lex()
        self.assertEqual(s.tokens, expect)

    def test_regex1(self):
        self.common_lex('a', [('a', Scanner.CHAR)])

    def test_regex2(self):
        self.common_lex('ab', [('a', Scanner.CHAR),
                               ('b', Scanner.CHAR)])

    def test_regex3(self):
        self.common_lex('a|b', [('a', Scanner.CHAR),
                                ('|', Scanner.ALTER),
                                ('b', Scanner.CHAR)])

    def test_regex4(self):
        self.common_lex('a.b', [('a', Scanner.CHAR),
                                ('.', Scanner.DOT),
                                ('b', Scanner.CHAR)])

    def test_regex5(self):
        self.common_lex('(a)', [('(', Scanner.LP),
                                ('a', Scanner.CHAR),
                                (')', Scanner.RP)])

    def test_regex6(self):
        self.common_lex('a*', [('a', Scanner.CHAR),
                               ('*', Scanner.STAR)])

    def test_regex7(self):
        self.common_lex('\w', [('\\', Scanner.BS),
                               ('w', Scanner.CHAR)])

    def common_syms(self, inputs, expect):
        s = Scanner(inputs)
        s.lex()
        res = s.syms()
        self.assertEqual(res, expect)

    def test_regex8(self):
        self.common_syms('a', {'a'})

    def test_regex9(self):
        self.common_syms('ab', {'a', 'b'})

    def test_regex10(self):
        self.common_syms('a|b', {'a', 'b'})

    def test_regex11(self):
        self.common_syms('(a|b)*', {'a', 'b'})

    def test_regex12(self):
        self.common_syms('(a|b)*abb', {'a', 'b'})
