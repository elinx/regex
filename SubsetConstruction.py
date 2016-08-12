from DFA import *


class SubsetConstruction:

    @staticmethod
    def generate_state():
        state = 0
        while True:
            yield state
            state += 1

    def __init__(self, nfa):
        self.nfa = nfa
        self.generator = SubsetConstruction.generate_state()

    def gen_state(self):
        return next(self.generator)

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

        queue = list()  # this is actually a BFS graph traverse algorithm
        queue.append(start_set)  # except that the vertex is a set

        visited_set = []
        dfa_states_map = dict()
        dfa_states_map[repr(start_set)] = self.gen_state()
        dfa.start = dfa_states_map[repr(start_set)]

        while queue:
            cur_set = queue[0]
            queue = queue[1:]  # de-queue
            visited_set.append(cur_set)
            # print('cur: {}'.format(cur_set))

            if self.nfa.final in cur_set:
                if dfa_states_map[repr(cur_set)] not in dfa.final:
                    dfa.final.append(dfa_states_map[(repr(cur_set))])

            for c in syms:
                next_set = self.eps_closure_of(list(self.nfa.move(cur_set, c)))
                # print('next: {}'.format(next_set))
                if next_set not in visited_set:
                    queue.append(next_set)  # enqueue
                    if repr(next_set) not in dfa_states_map:
                        dfa_states_map[repr(next_set)] = self.gen_state()
                dfa.add_trans(dfa_states_map[repr(cur_set)], dfa_states_map[repr(next_set)], c)
        return dfa
