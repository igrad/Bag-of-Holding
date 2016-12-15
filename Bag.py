from SysFuncs import *
from BagItem import *
from SaveStores import *

class Bag():
    ID = 0
    name = 'Bag'
    items = list()

    def __init__(self, **kwargs):
        if 'ID' in kwargs: self.ID = int(kwargs['ID'])
        else: self.ID = GetNewBagID()
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'items' in kwargs: self.items = list(kwargs['items'])

        CreateBag(self)

    def UpdateName(newName):
        self.name = newName
        UpdateBagInfo(self.ID)

    # TODO: def AddItem(item):
    # TODO: def RemoveItem(itemID):
