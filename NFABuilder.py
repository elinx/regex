from NFA import *

class NFABuilder:

    def basic_nfa(ic):
        nfa = NFA(2, 0, 1)
        nfa.add_trans(0, 1, ic)

    def alter_nfa(nfa1, nfa2):
        """nfa1 | nfa2"""
        return nfa1 | nfa2

    def concat_nfa(nfa1, nfa2):
        """nfa1nfa2"""
        return nfa1 & nfa2

    def repeat_nfa(nfa1):
        """nfa1*"""
        return ~nfa1