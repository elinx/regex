class Scanner:

    LP = 'LeftP'
    RP = 'RightP'
    STAR = 'Star'
    ALTER = 'Alter'
    WS = 'WhiteSpace'
    TAB = 'Tab'
    NL = 'Newline'
    CHAR = 'Char'
    DOT = 'Dot'
    CAT = 'Cat'
    BS = 'BackSlash'

    token_exprs = [
        ('(', LP),
        (')', RP),
        ('*', STAR),
        ('|', ALTER),
        ('.', DOT),
        (' ', WS),
        ('\\', BS),
        ('\t', CHAR),
        ('\n', CHAR),
        # ('\d', CHAR),
        # ('\D', CHAR),
        # ('\w', CHAR),
        # ('\W', CHAR),
        ('abcdefghijklmnopqrstuvwxyz'
         'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
         '0123456789', CHAR)
    ]

    def __init__(self, inputs):
        self.inputs = inputs
        self.tokens = []

    def lex(self):
        for w in self.inputs:
            for t in self.token_exprs:
                if w in t[0]:
                    self.tokens.append((w, t[1]))

    def syms(self):
        res = set()
        for val, tag in self.tokens:
            if tag == self.CHAR:
                res.add(val)
        return res
