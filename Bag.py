from SysFuncs import *
from BagItem import *
from SaveStores import *
from Currency import *

class Bag():
    ID = 0
    name = 'Bag'
    items = dict()
    currency = CurrencySet()

    def __init__(self, **kwargs):
        if 'ID' in kwargs: self.ID = int(kwargs['ID'])
        else: self.ID = GetNewBagID()
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'items' in kwargs: self.items = dict(kwargs['items'])
        if 'currency' in kwargs: self.currency = CurrencySet(kwargs['currency'])

        StoreNewBag(self)

    def UpdateBag(**kwargs):
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'items' in kwargs: self.items = dict(kwargs['items'])
        if 'currency' in kwargs: self.currency = CurrencySet(kwargs['currency'])

        UpdateBagInfo(self.ID, self.name, self.items, self.currency)

    def AddItem(item):
        items[item.ID] = item

    def RemoveItem(itemID):
        del items[itemID]
