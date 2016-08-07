class Scanner:
    NUM = 'NUM'
    OP = 'OP'

    ops = '+-*/'

    def __init__(self, inputs):
        self.inputs = inputs
        self.tokens = []

    def lex(self):
        ss = self.inputs.split()
        for w in ss:
            if w is not None and w.isdigit():
                self.tokens.append((int(w), self.NUM))
            elif len(w) == 1 and w in self.ops:
                self.tokens.append((w, self.OP))
            else:
                raise ValueError('input {0} is not valid'.format(w))
