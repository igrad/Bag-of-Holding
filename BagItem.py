from SysFuncs import *
from LoadSaves import *

class BagItem():
    '''An unassigned item that represents all the item-specific data required by the user.
    ----------
    String name: Name of the item
    Int qty: Quantity of this item within the bag
    Float weight: Weight of the item in analogous units
    Int val: Value of the item in analogous units
    String desc: A brief description of the item
    String icon: File path to the icon image
    List(String) tags: List of tags that describe this item'''
    ID = 0
    name = 'item'
    qty = 1
    weight = 1.00
    val = 1
    desc = 'description'
    icon = 'images/none.png'
    tags = []

    def __init__(self, **kwargs):
        if 'ID' in kwargs: self.ID = int(kwargs['ID'])
        else: self.ID = self.GetNewItemID()
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'qty' in kwargs: self.qty = int(kwargs['qty'])
        if 'weight' in kwargs: self.weight = float(kwargs['qty'])
        if 'val' in kwargs: self.val = float(kwargs['val'])
        if 'desc' in kwargs: self.desc = str(kwargs['desc'])
        if 'icon' in kwargs: self.icon = str(kwargs['icon'])
        if 'tags' in kwargs: self.icon = list(kwargs['tags'])

        ITEMS[self.ID] = self

        if 'ID' not in kwargs:
            SaveItemInfo(self)

    def AddQty(self):
        self.qty += 1

    def SubQty(self):
        self.qty -= 1

    def HasTag(self, tag):
        if tag in tags: return True
        else: return False

    def UpdateItem(self, **kwargs):
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'qty' in kwargs: self.qty = int(kwargs['qty'])
        if 'weight' in kwargs: self.weight = float(kwargs['qty'])
        if 'val' in kwargs: self.val = float(kwargs['val'])
        if 'desc' in kwargs: self.desc = str(kwargs['desc'])
        if 'icon' in kwargs: self.icon = str(kwargs['icon'])
        if 'tags' in kwargs: self.icon = list(kwargs['tags'])

        SaveItemInfo(self)

    def GetNewItemID(self):
        '''Gets an unused itemID number.'''
        keys = ITEMS.keys()
        for i in range(MAX_ITEMS):
            if not i in keys: return i

        PostErrorMessage("No more items available!")
        return None

    def SaveItemInfo(self):
        '''Stores the item by copying a shallow copy of the actual item.'''
        itemStore.put(self.ID, name = self.name, qty = self.qty, weight = self.weight,
            desc = self.desc, icon = self.icon, tags = self.tags)

    def DeleteItemFromSave(self):
        '''Removes the item from itemStore save file. This does not remove the item from bags that it may be saved in.'''
        itemStore.delete(self.ID)
