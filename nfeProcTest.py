import os.path
from nfe.nfeProc import NfeProc


filePath = os.getcwd() + os.path.sep + \
    'files\\NFe35220211111111111111550010000017501070050070.xml'

if not os.path.isfile(filePath):
    raise Exception("ARQUIVO NOT FOUND")
else:

    # fileBody = open(filePath).read()

    nfeProc = NfeProc()
    nfeProc.loadFromFile(filePath)

    if not nfeProc.isValid():
        raise Exception("NFE INVALIDA")

    def title(text):
        print("-" * 80)
        print(text)
        print("-" * 80)

    # nfeProc

    title('nfeProc')
    print(f'@xmlns= {nfeProc.xmlns}')
    print(f'@versao= {nfeProc.versao}')
    print()

    # nfe

    title('Nfe')
    print(f'xmlns={nfeProc.nfe.xmlns}')
    print('infNfe')

    # Signature
    title('Signature')
    signature = nfeProc.nfe.signature
    print(f'  xmlns={signature.xmlns}')
    print(f'  signaturevalue={signature.signaturevalue}')
    print(f'  KeyInfo')
    print(f'          X509Data')
    print(
        f'                   X509Certificate={signature.keyinfo.x509data.x509certificate}')
    # protNfe
    title('protNfe')
    print(f'versao={nfeProc.protNfe.versao}')
    print('InfProt')

    for a in ['id', 'tpAmb', 'verAplic', 'chNfe', 'dhRecbto', 'nProt', 'digVal', 'cStat', 'xMotivo']:
        print(f'  {a} = {getattr(nfeProc.protNfe.infoProt,a)}')

    title('FIM')
