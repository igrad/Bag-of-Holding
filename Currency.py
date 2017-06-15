from SysFuncs import *


CurrencyUnit = namedtuple('CurrencyUnit', 'name unitval')

class CurrencySet:
    cTypes = list()
    def __init__(self, **kwargs):
        if 'cTypes' in kwargs:
            self.cTypes = sorted([CurrencyUnit(x[0], x[1]) for x in kwargs['cTypes']],
                key = lambda x:x[1])

    def GetCNames(self):
        return self.cTypes.keys()

    def GetCVals(self):
        return self.cTypes.values()

    def AddNewCType(self, name, unitval):
        newCType = CurrencyUnit(name, unitval)

        self.cTypes.append(newCType)
        self.cTypes = sorted(cTypes, key = lambda x:x[1])

    def RemoveCType(self, name):
        for cType in self.cTypes:
            if cType.name == name:
                del self.cTypes[cType]

def ConvertStringToUnits(str):
    '''Interpret the intended value of the string by converting the labeled units in the
    string to the intended unit-value.'''
    pass
