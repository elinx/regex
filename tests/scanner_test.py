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
