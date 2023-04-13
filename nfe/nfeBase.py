class NfeBase:

    __child = {}
    __index = {}

    def __init__(self, child):
        self.__child = child
        for k in child:
            key = str(k.lower()).replace('@', '')
            self.__index[key] = k

    def __getattr__(self, attr_name):
        return self.__child.get(self.__index.get(attr_name.lower()), '')
