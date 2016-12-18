from SysFuncs import *
from SaveStores import *

class BagItem():
    '''An unassigned item that represents all the item-specific data required by the user.
    ----------
    String name: Name of the item
    Int qty: Quantity of this item
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
        else: self.ID = GetItemIndex()
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'qty' in kwargs: self.qty = int(kwargs['qty'])
        if 'weight' in kwargs: self.weight = float(kwargs['qty'])
        if 'val' in kwargs: self.val = float(kwargs['val'])
        if 'desc' in kwargs: self.desc = str(kwargs['desc'])
        if 'icon' in kwargs: self.icon = str(kwargs['icon'])
        if 'tags' in kwargs: self.icon = list(kwargs['tags'])

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

        UpdateItemInfo(self.ID, self.qty, self.weight, self.val, self.desc, self.icon,
            self.tags)
