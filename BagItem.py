from SysFuncs import *
from LoadSaves import *
from Currency import ConvertStringToUnits

class BagItem():
    '''An unassigned item that represents all the item-specific data required by the user.
    ----------
    Str name: Name of the item
    Str qty: Quantity of this item within the bag
    Str weight: Weight of the item in analogous units
    Str val: Value of the item in analogous units
    String desc: A brief description of the item
    String icon: File path to the icon image
    List(String) tags: List of tags that describe this item'''


    def __init__(self, **kwargs):
        if 'ID' in kwargs: self.ID = str(kwargs['ID'])
        else: self.ID = self.GetNewItemID()
        if 'name' in kwargs: self.name = str(kwargs['name'])
        if 'qty' in kwargs: self.qty = str(kwargs['qty'])
        if 'weight' in kwargs: self.weight = str(kwargs['weight'])
        if 'val' in kwargs: self.val = str(kwargs['val'])
        if 'desc' in kwargs: self.desc = str(kwargs['desc'])
        if 'icon' in kwargs: self.icon = str(kwargs['icon'])
        if 'tags' in kwargs: self.tags = str(kwargs['tags'])

        if self.ID == None: return

        ITEMS[self.ID] = self

        if 'ID' not in kwargs:
            self._SaveItemInfo_()


    def __lt__(self, other):
        if SORT_ATTR == 'Name':
            return self.name < other.name
        elif SORT_ATTR == 'Quantity':
            return self.qty < other.qty
        elif SORT_ATTR == 'Weight':
            return self.weight < other.weight
        elif SORT_ATTR == 'Value':
            return ConvertStringToUnits(self.val) < ConvertStringToUnits(other.val)

    def __le__(self, other):
        if SORT_ATTR == 'Name':
            return self.name <= other.name
        elif SORT_ATTR == 'Quantity':
            return self.qty <= other.qty
        elif SORT_ATTR == 'Weight':
            return self.weight <= other.weight
        elif SORT_ATTR == 'Value':
            return ConvertStringToUnits(self.val) <= ConvertStringToUnits(other.val)

    def __eq__(self, other):
        if SORT_ATTR == 'Name':
            return self.name == other.name
        elif SORT_ATTR == 'Quantity':
            return self.qty == other.qty
        elif SORT_ATTR == 'Weight':
            return self.weight == other.weight
        elif SORT_ATTR == 'Value':
            return ConvertStringToUnits(self.val) == ConvertStringToUnits(other.val)

    def __ne__(self, other):
        if SORT_ATTR == 'Name':
            return self.name != other.name
        elif SORT_ATTR == 'Quantity':
            return self.qty != other.qty
        elif SORT_ATTR != 'Weight':
            return self.weight != other.weight
        elif SORT_ATTR != 'Value':
            return ConvertStringToUnits(self.val) == ConvertStringToUnits(other.val)

    def __ge__(self, other):
        if SORT_ATTR == 'Name':
            return self.name >= other.name
        elif SORT_ATTR == 'Quantity':
            return self.qty >= other.qty
        elif SORT_ATTR == 'Weight':
            return self.weight >= other.weight
        elif SORT_ATTR == 'Value':
            return ConvertStringToUnits(self.val) >= ConvertStringToUnits(other.val)

    def __gt__(self, other):
        if SORT_ATTR == 'Name':
            return self.name > other.name
        elif SORT_ATTR == 'Quantity':
            return self.qty > other.qty
        elif SORT_ATTR == 'Weight':
            return self.weight > other.weight
        elif SORT_ATTR == 'Value':
            return ConvertStringToUnits(self.val) > ConvertStringToUnits(other.val)


    def HasTag(self, tag):
        try:
            if str(tag).lower() in [str(x).lower() for x in tags]: return True
            else: return False
        except Exception:
            LogExc('BagItem.HasTag(' + str(tag) + ')')


    def UpdateItem(self, **kwargs):
        try:
            if 'name' in kwargs: self.name = str(kwargs['name'])
            if 'qty' in kwargs: self.qty = str(kwargs['qty'])
            if 'weight' in kwargs: self.weight = str(kwargs['weight'])
            if 'val' in kwargs: self.val = str(kwargs['val'])
            if 'desc' in kwargs: self.desc = str(kwargs['desc'])
            if 'icon' in kwargs: self.icon = str(kwargs['icon'])
            if 'tags' in kwargs: self.tags = str(kwargs['tags'])

            self.DeleteItemFromSave()

            self._SaveItemInfo_()
        except Exception:
            LogExc('BagItem.UpdateItem()')


    def GetNewItemID(self):
        '''Gets an unused itemID number.'''
        keys = [int(x) for x in itemStore.keys()]

        for i in range(MAX_ITEMS):
            if not i in keys: return str(i)

        LogMsg("No more items available!")
        return None


    def _SaveItemInfo_(self):
        '''Stores the item by copying a shallow copy of the actual item.'''
        try:
            itemStore.put(str(self.ID), name = self.name, qty = self.qty, weight = self.weight,
                val = self.val, desc = self.desc, icon = self.icon, tags = self.tags)
        except Exception as ex:
            LogExc('BagItem._SaveItemInfo_()')


    def DeleteItemFromSave(self):
        '''Removes the item from itemStore save file. This does not remove the item from bags that it may be saved in.'''
        try:
            itemStore.delete(str(self.ID))
        except Exception as ex:
            LogExc('BagItem.DeleteItemFromSave()')
