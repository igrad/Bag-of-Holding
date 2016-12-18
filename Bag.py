from SysFuncs import *
from LoadSaves import *
from AppInit import *
from BagItem import *
from Currency import *


class Bag:
    ID = 0
    name = 'Bag'
    items = dict()
    currency = CurrencySet()
    
    def __init__(self, **kwargs):
        if 'ID' in kwargs: self.ID = int(kwargs['ID'])
        else: self.ID = self.GetNewBagID()
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'items' in kwargs: self.items = dict(kwargs['items'])
        if 'currency' in kwargs: self.currency = CurrencySet(cTypes = kwargs['currency'])

        BAGS[self.ID] = self

        if 'ID' not in kwargs:
            self.SaveBagInfo()

    def UpdateBag(self, **kwargs):
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'items' in kwargs: self.items = dict(kwargs['items'])
        if 'currency' in kwargs: self.currency = CurrencySet(kwargs['currency'])

        SaveBagInfo(self)

    def AddItem(self, item):
        items[item.ID] = item

    def RemoveItemFromBag(self, itemID):
        del self.items[itemID]

        ITEMS[itemID].DeleteItemFromSave()

        del ITEMS[itemID]

        self.SaveBagInfo()

    def GetNewBagID(self):
        '''Gets an unused bagID number.'''
        keys = BAGS.keys()

        for i in range(MAX_BAGS):
            if not i in keys: return i

        PostErrorMessage("No more bags available!")
        return None

    def SaveBagInfo(self):
        '''Stores the bag by copying a shallow copy of the actual bag.'''
        bagsStore.put(self.ID, name = self.name, currency = self.currency.cTypes,
            items = self.items)

    def DeleteBagFromSave(self):
        '''Removes the bag from bagsStore save file.'''
        bagsStore.delete(self.ID)
