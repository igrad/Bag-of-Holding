from SysFuncs import *
from SaveStores import *

ITEMIDCTR = 0

class BagItem():
    '''An unassigned item that represents all the item-specific data required by the user.
    ----------
    String name: Name of the item
    Int qty: Quantity of this item
    String desc: A brief description of the item
    String icon: File path to the icon image
    List(String) tags: List of tags that describe this item'''

    def __init__(self, **kwargs):
        if 'ID' in kwargs: self.ID = int(kwargs['ID'])
        else: self.ID = GetItemIndex()
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'qty' in kwargs: self.qty = int(kwargs['qty'])
        if 'mass' in kwargs: self.mass = float(kwargs['qty'])
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
        if 'mass' in kwargs: self.mass = float(kwargs['qty'])
        if 'desc' in kwargs: self.desc = str(kwargs['desc'])
        if 'icon' in kwargs: self.icon = str(kwargs['icon'])
        if 'tags' in kwargs: self.icon = list(kwargs['tags'])

        UpdateItemInfo(self.ID)
