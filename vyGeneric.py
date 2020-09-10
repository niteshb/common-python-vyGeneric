from importlib import reload
from . import vyGenericObjectRepr

class vyGeneric:
    def __init__(self):
        pass

    def __repr__(self):
        return vyGenericObjectRepr(self)

class vyGenericDict(vyGeneric):
    def __init__(self):
        self.attrDict = {}

    def __getitem__(self, key):
        return self.attrDict[key]

    def __setitem__(self, key, value):
        self.attrDict[key] = value

class vyGenericArray(vyGeneric):
    def __init__(self):
        self.__array = []
    
    def append(self, value):
        self.__array.append(value)

    def __getitem__(self, idx):
        return self.__array[idx]

    def __setitem__(self, idx, value):
        self.__array[idx] = value

