from SysFuncs import *
from LoadSaves import *
from AppInit import *
from BagItem import *
from Currency import *


class Bag:
    '''An instance of a user's bag. This contains all of the meta data about the
    bag as well as lists the contents of the bag as ID references. Information
    about the items themselves are not stored here, just the IDs of the items
    assigned to this bag.'''

    def __init__(self, **kwargs):
        if 'ID' in kwargs: self.ID = str(kwargs['ID'])
        else: self.ID = self.GetNewBagID()
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'items' in kwargs: self.items = list(kwargs['items'])
        if 'currency' in kwargs: self.currency = CurrencySet(cTypes = kwargs['currency'])
        if 'view' in kwargs: self.view = str(kwargs['view'])

        self.tot_items = len(self.items)
        self.tot_weight = 0
        self.tot_val = 0

        BAGS[self.ID] = self

        if 'ID' not in kwargs:
            self.SaveBagInfo()


    def UpdateBag(self, **kwargs):
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'items' in kwargs: self.items = list(kwargs['items'])
        if 'currency' in kwargs: self.currency = CurrencySet(kwargs['currency'])
        if 'view' in kwargs: self.view = str(kwargs['view'])

        self.SaveBagInfo()
        self.SetTotals()


    def AddItem(self, itemID):
        self.items.append(itemID)
        self.items.sort()

        self.SaveBagInfo()


    def RemoveItemFromBag(self, itemID):
        del self.items[itemID]

        ITEMS[itemID].DeleteItemFromSave()

        del ITEMS[itemID]

        self.SaveBagInfo()


    def GetNewBagID(self):
        '''Gets an unused bagID number.'''
        keys = BAGS.keys()

        for i in range(MAX_BAGS):
            if not i in keys: return str(i)

        LogMsg("No more bags available!")
        return None


    def SaveBagInfo(self):
        '''Stores the bag by copying a shallow copy of the actual bag.'''
        bagsStore.put(str(self.ID), name = self.name, currency = self.currency.cTypes,
            view = self.view, items = self.items)


    def SetTotals(self):
        '''Set the tot_items, tot_weight, and tot_val properties.'''
        self.tot_items = len(self.items)
        self.tot_weight = sum([int(ExtractNumber(ITEMS[str(x)].weight)) for x in self.items])
        self.tot_val = sum([ExtractNumber(ITEMS[str(x)].val) for x in self.items])


    def DeleteBagFromSave(self):
        '''Removes the bag from bagsStore save file.'''
        bagsStore.delete(str(self.ID))
