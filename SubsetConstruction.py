from DFA import *


class SubsetConstruction:

    def __init__(self, nfa):
        self.nfa = nfa

    def eps_closure_of(self, states):
        """
        Fetch a eps-closure set for all states in nfa
        :param states: states list
        :return: eps closure of this stats list
        """
        stack = [] + states
        eps = [] + states
        # DFS search
        while stack:
            v = stack.pop()
            for i in range(self.nfa.size):
                if self.nfa.trans_tbl[v][i] == -1 and \
                                i not in eps:
                    eps.append(i)
                    stack.append(i)
        return eps

    def build_dfa(self, syms):
        dfa = DFA()
        start_set = self.eps_closure_of([self.nfa.start])
        dfa.start = start_set
        queue = list()
        queue.append(start_set)

        while queue:
            cur_set = queue[0]
            queue = queue[1:]  # de-queue
            for c in syms:
                next_set = self.eps_closure_of(list(self.nfa.move(cur_set, c)))
                queue.append(next_set)  # enqueue
                dfa.add_trans(cur_set, next_set, c)
