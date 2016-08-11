class DFA:

    def __init__(self):
        self.start = set()
        self.final = set()
        self.trans_tbl = {}

    def add_trans(self, fm, to, inputs):
        print(fm)
        print(to)
        print(inputs)
        self.trans_tbl[(fm, inputs)] = to

    def match(self, inputs):
        return True