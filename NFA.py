class NFA:
    EPS = -1
    NONE = 0

    def create_tbl(self, sz):
        if sz <= 1:
            return None
        tbl = []
        for r in range(sz):
            tbl.append([self.NONE for c in range(sz)])
        return tbl

    def __init__(self, sz, start, final):
        self.size = sz
        self.start = start
        self.final = final
        self.trans_tbl = self.create_tbl(self.size)

    def add_trans(self, fm, to, ic):
        self.trans_tbl[fm][to] = ic

    def display_trans(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.trans_tbl[r][c] != self.NONE:
                    ic = self.trans_tbl[r][c]
                    ic = ic if ic != self.EPS else "EPS"
                    print("from {0} to {1} when input is {2}".format(r, c, ic))

    def __rshift__(self, delta):
        if delta <= 0:
            return self
        new_tbl = self.create_tbl(self.size + delta)

        for r in range(self.size):
            for c in range(self.size):
                new_tbl[r+delta][c+delta] = self.trans_tbl[r][c]

        self.trans_tbl = new_tbl
        self.size += delta
        self.start += delta
        self.final += delta

        # self.add_trans(0, self.start, self.EPS)
        return self

    def fill(self, sub):
        """Copy the sub NFA transactions to this NFA

        We assume that this NFA is larger than sub NFA
        """
        for r in range(sub.size):
            for c in range(sub.size):
                self.trans_tbl[r][c] = sub.trans_tbl[r][c]

    def append_final(self):
        new_tbl = self.create_tbl(self.size + 1)
        for r in range(self.size):
            for c in range(self.size):
                new_tbl[r][c] = self.trans_tbl[r][c]
        self.trans_tbl = new_tbl
        self.size += 1
        self.final += 1

    def __or__(self, other):
        """Create a (this | other) transaction table"""
        self >>= 1
        other >>= self.size

        new_nfa = NFA(other.size + 1, 0, other.size)
        new_nfa.fill(other)
        new_nfa.fill(self)  # note: the copy order matters, copy the large one firstly.

        new_nfa.add_trans(new_nfa.start, self.start, self.EPS)
        new_nfa.add_trans(new_nfa.start, other.start, self.EPS)
        new_nfa.add_trans(self.final, new_nfa.final, self.EPS)
        new_nfa.add_trans(other.final, new_nfa.final, self.EPS)

        return new_nfa

    def __and__(self, other):
        """Create a (this other) concat transaction table"""
        self >>= 1
        other >>= self.size - 1

        new_nfa = NFA(other.size + 1, 0, other.size)
        new_nfa.fill(other)
        new_nfa.fill(self)

        new_nfa.add_trans(0, self.start, self.EPS)
        new_nfa.add_trans(other.final, new_nfa.final, self.EPS)

        return new_nfa

    def __invert__(self):
        """Create a repeat(eps-closure) pattern"""
        self >>= 1

        new_nfa = NFA(self.size + 1, 0, self.size)
        new_nfa.fill(self)

        new_nfa.add_trans(0, self.start, self.EPS)
        new_nfa.add_trans(self.final, new_nfa.final, self.EPS)
        new_nfa.add_trans(new_nfa.start, new_nfa.final, self.EPS)
        new_nfa.add_trans(self.final, self.start, self.EPS)

        return new_nfa
