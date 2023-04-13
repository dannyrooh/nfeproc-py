from .nfeBase import NfeBase


class InfoProt(NfeBase):

    def __init__(self, child):
        super().__init__(child)

        # # super().__init__(child)
        # l = list(filter(lambda x: (x.lower() == 'infprot'), child))

        # if l:
        #     super().__init__(child[next(iter(l))])

        # # retorna o inforProt
