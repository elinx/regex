class DFA:

    def __init__(self):
        self.start = []
        self.final = []
        self.trans_tbl = {}

    def add_trans(self, fm, to, inputs):
        self.trans_tbl[(fm, inputs)] = to

    def __repr__(self):
        ret = 'start: {}, final: {}\n'.format(self.start,self.final)
        for k, v in self.trans_tbl.items():
            fm, inputs = k
            ret += 'from: {} to: {}, inputs: {}\n'.format(fm, v, inputs)
        return ret

    def match(self, inputs):
        fm = self.start
        for c in inputs:
            if (fm, c) not in self.trans_tbl:
                return False
            fm = self.trans_tbl[(fm, c)]
        if fm in self.final:
            return True
        else:
            return False
