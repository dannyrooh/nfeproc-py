from .infProf import InfoProt


class ProtNfe:

    versao: str = ''
    infoProt: InfoProt

    def __init__(self, child):

        # print(child)

        v = filter(lambda x: (x.lower() == '@versao'), child)
        if v:
            self.versao = child[next(iter(v))]

        l = list(filter(lambda x: (x.lower() == 'infprot'), child))

        if l:
            self.infoProt = InfoProt(child[next(iter(l))])
