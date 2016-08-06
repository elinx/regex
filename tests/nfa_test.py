import unittest
from NFA import *


class TestNFAMethod(unittest.TestCase):

    def test_ctor(self):
        nfa = NFA(2, 0, 1)

        res = [[0, 0], [0, 0]]

        self.assertEqual(nfa.size, len(res))
        self.assertEqual(nfa.trans_tbl, res)

    def test_empty_ctor(self):
        nfa = NFA(1, 0, 0)

        self.assertEqual(nfa.size, 1)
        self.assertEqual(nfa.trans_tbl, None)

    def test_trans(self):
        nfa = NFA(2, 0, 1)
        nfa.add_trans(0, 1, 'a')

        res = [[0, 'a'], [0, 0]]

        self.assertEqual(nfa.trans_tbl, res)

    def test_1_shift(self):
        nfa = NFA(2, 0, 1)
        nfa.add_trans(0, 1, 'a')
        nfa >>= 1

        res = [[0, 0, 0], [0, 0, 'a'], [0, 0, 0]]

        self.assertEqual(nfa.size, len(res))
        self.assertEqual(nfa.start, 1)
        self.assertEqual(nfa.final, 2)
        self.assertEqual(nfa.trans_tbl, res)

    def test_3_shift(self):
        nfa = NFA(2, 0, 1)
        nfa.add_trans(0, 1, 'a')
        nfa >>= 3
        self.assertEqual(nfa.size, 5)
        self.assertEqual(nfa.start, 3)
        self.assertEqual(nfa.final, 4)

        res = [[0,  0,  0,  0,  0],
               [0,  0,  0,  0,  0],
               [0,  0,  0,  0,  0],
               [0,  0,  0,  0, 'a'],
               [0,  0,  0,  0,  0]]

        self.assertEqual(nfa.trans_tbl, res)

    def test_0_shift(self):
        nfa = NFA(2, 0, 1)
        nfa.add_trans(0, 1, 'a')
        nfa >>= 0
        res = [[0, 'a'], [0, 0]]
        self.assertEqual(nfa.trans_tbl, res)

    def test_or_op1(self):
        nfa1 = NFA(2, 0, 1)
        nfa1.add_trans(0, 1, 'a')
        nfa2 = NFA(2, 0, 1)
        nfa2.add_trans(0, 1, 'b')

        new_nfa = nfa1 | nfa2
        self.assertEqual(nfa2.size, 5)
        self.assertEqual(nfa1.size, 3)
        self.assertEqual(new_nfa.start, 0)
        self.assertEqual(new_nfa.final, 5)
        self.assertEqual(new_nfa.size, 6)

        res = [[0,  -1,   0,  -1,   0,   0],
               [0,   0, 'a',   0,   0,   0],
               [0,   0,   0,   0,   0,  -1],
               [0,   0,   0,   0, 'b',   0],
               [0,   0,   0,   0,   0,  -1],
               [0,   0,   0,   0,   0,   0]]
        self.assertEqual(new_nfa.trans_tbl, res)

    def test_and_op1(self):
        nfa1 = NFA(2, 0, 1)
        nfa1.add_trans(0, 1, 'a')
        nfa2 = NFA(2, 0, 1)
        nfa2.add_trans(0, 1, 'b')

        new_nfa = nfa1 & nfa2

        self.assertEqual(new_nfa.start, 0)
        self.assertEqual(new_nfa.final, 4)
        self.assertEqual(new_nfa.size, 5)

        res = [[0, -1,   0,   0,   0],
               [0,  0, 'a',   0,   0],
               [0,  0,   0, 'b',   0],
               [0,  0,   0,   0,  -1],
               [0,  0,   0,   0,   0]]
        self.assertEqual(new_nfa.trans_tbl, res)

    def test_rep_op1(self):
        nfa1 = NFA(2, 0, 1)
        nfa1.add_trans(0, 1, 'a')

        new_nfa = ~nfa1  # create a repeat pattern

        self.assertEqual(new_nfa.size, 4)
        self.assertEqual(new_nfa.start, 0)
        self.assertEqual(new_nfa.final, 3)

        res = [[0, -1, 0, -1], [0, 0, 'a', 0], [0, -1, 0, -1], [0, 0, 0, 0]]
        self.assertEqual(new_nfa.trans_tbl, res)

if __name__ == '__main__':
    unittest.main()
