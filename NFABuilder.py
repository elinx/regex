from NFA import *
from Scanner import *


class NFABuilder:

    def basic_nfa(ic):
        nfa = NFA(2, 0, 1)
        nfa.add_trans(0, 1, ic)
        return nfa

    def alter_nfa(nfa1, nfa2):
        """nfa1 | nfa2"""
        return nfa1 | nfa2

    def concat_nfa(nfa1, nfa2):
        """nfa1nfa2"""
        return nfa1 & nfa2

    def repeat_nfa(nfa1):
        """nfa1*"""
        return ~nfa1

    def ast_to_nfa(ast):
        node_type = ast.value[1]
        node_value = ast.value[0]
        node_left = ast.left
        node_right = ast.right

        if node_type == Scanner.CHAR:
            return NFABuilder.basic_nfa(node_value)
        elif node_type == Scanner.CAT:
            return NFABuilder.concat_nfa(NFABuilder.ast_to_nfa(node_left),
                                         NFABuilder.ast_to_nfa(node_right))
        elif node_type == Scanner.STAR:
            return NFABuilder.repeat_nfa(NFABuilder.ast_to_nfa(node_left))
        elif node_type == Scanner.ALTER:
            return NFABuilder.alter_nfa(NFABuilder.ast_to_nfa(node_left),
                                        NFABuilder.ast_to_nfa(node_right))
        else:
            raise ValueError('unknown ast node type')

