class X509Data:
    x509certificate: str

    def __init__(self, child):
        self.x509certificate = child.get('X509Certificate')


class KeyInfo:
    x509data: X509Data

    def __init__(self, child):
        tag = ''
        for x in child:
            if x.lower() == 'x509data':
                tag = x
                break

        if tag:
            self.x509data = X509Data(child[tag])


class Signature:
    xmlns: str
    signaturevalue: str
    keyinfo: KeyInfo

    def __init__(self, child):
        # print(child)
        for tag in child:
            t = tag.lower()
            if t == '@xmlns':
                self.xmlns = child[tag]
            elif t == 'signaturevalue':
                self.signaturevalue = child[tag]
            elif t == 'keyinfo':
                self.keyinfo = KeyInfo(child[tag])
