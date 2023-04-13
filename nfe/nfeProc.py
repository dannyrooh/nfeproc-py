import os.path
import xmltodict
from .protNfe import ProtNfe
from .nfe import Nfe


class NfeProc:

    # private
    __myfile: str = ''

    # public
    versao: str
    xmlns: str
    nfe: Nfe
    protNfe: ProtNfe

    # methods
    def __init__(self, myFile: str = ""):
        self.__myfile = myFile
        self.__bootstrapNfeProc()

    def isValid(self):
        return not self.__myfile.strip() == ""

    def loadFromFile(self, filePath: str):
        if not os.path.isfile(filePath):
            raise Exception("FILE NOT FOUND")
        self.__myfile = open(filePath).read()
        self.__bootstrapNfeProc()

    def __bootstrapNfeProc(self):

        if not self.isValid():
            return

        xmlDict = xmltodict.parse(self.__myfile)  # Parse XML
        # retorna o primeiro item
        root = next(iter(xmlDict))

        if (root == ''):
            quit()

        cols = {}

        for k in xmlDict[root].keys():
            cols[str(k).lower()] = k

        for i in cols:
            # if (str(i).lower() == 'protnfe'):
            # print(i)
            if (i == 'protnfe'):
                self.protNfe = ProtNfe(xmlDict[root][cols.get(i)])
                # print('-> PROTNFE')
            elif (i == 'nfe'):
                self.nfe = Nfe(xmlDict[root][cols.get(i)])

                # colsInfNfe = []
                # for x in infNfe:
                #     for y in infNfe[x]:
                #     print(x, y)

                # print(colsInfNfe)
            elif (i == '@versao') or (i == '@xmlns'):
                setattr(self, i[1:], xmlDict[root][i])
