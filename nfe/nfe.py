from .signature import Signature


class Nfe():
    xmlns: str = ''
    infNfe = {}
    signature: Signature

    def __init__(self, child):
        # print(child)

        x = filter(lambda x: (x.lower() == '@xmlns'), child)
        if x:
            self.xmlns = child[next(iter(x))]

        # signature
        s = filter(lambda x: (x.lower() == 'signature'), child)
        if s:
            self.signature = Signature(child[next(iter(s))])
