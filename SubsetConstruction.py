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

    def build_dfa(self):
        pass
