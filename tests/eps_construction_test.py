import unittest
from Parser import *
from NFABuilder import *
from SubsetConstruction import *


class EPSConTest(unittest.TestCase):
    def setUp(self):
        scanner = Scanner('(a|b)*abb')
        scanner.lex()

        parser = Parser(scanner.tokens)
        parser.parse()

        nfa = NFABuilder.ast_to_nfa(parser.ast)

        self.sc = SubsetConstruction(nfa)

    def common(self, states, target):
        res = self.sc.eps_closure_of(states)
        self.assertEqual(sorted(res), sorted(target))

    def test_eps_closure_of_0(self):
        self.common([0], [0, 1, 2, 4, 7])

    def test_eps_closure_of_1(self):
        self.common([1], [1, 2, 4])

    def test_eps_closure_of_2(self):
        self.common([2], [2])

    def test_eps_closure_of_3(self):
        self.common([3], [3, 6, 7, 1, 2, 4])

    def test_eps_closure_of_4(self):
        self.common([4], [4])

    def test_eps_closure_of_89(self):
        self.common([8, 9], [8, 9])
