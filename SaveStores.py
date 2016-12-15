from SysFuncs import *
from Bag import *
from BagItem import *

bagsStore = JsonStore('bags_data.json')
itemStore = JsonStore('item_data.json')
optsStore = JsonStore('user_settings.json')

BAGS = dict()
ITEMS = dict()
ITEMVIEWS = list()

MAX_BAGS = 10
MAX_ITEMS = 5000
LAST_BAG_OPENED = 0
NOOBIE_TIPS = True


# Load data
def LoadData():
    LoadItems()
    LoadBags()
    LoadSettings()

def LoadItems():
    '''Create a temp copy of the items store in itemStore, and make them accessible to the user by appending them to the ITEMS dict.'''
    failedItems = list()

    for key in itemStore.keys():
        try:
            sname = str(itemStore.get(key)['name'])
            sqty = int(itemStore.get(key)['qty'])
            smass = float(itemStore.get(key)['mass'])
            sdesc = str(itemStore.get(key)['desc'])
            sicon = str(itemStore.get(key)['icon'])
            stags = list(itemStore.get(key)['tags'])

            item = BagItem(ID = key, name = sname, qty = sqty, mass = smass,
                           desc = sdesc, icon = sicon, tags = stags)

            ITEMS.append(item)

        except:
            failedItems.append(key)

    PostErrorMessage("ERROR: Could not load the following items: " + str(failedItems))

def LoadBags():
    '''Create a temp copy of the bags stored in bagsStore, and make them accessible to the user by appending them to the BAGS dict.'''
    failedBags = list()

    for key in bagsStore.keys():
        try:
            sname = str(bagsStore.get(key)['name'])
            sitems = list(bagsStore.get(key)['items'])

            bag = Bag(ID = key, name = sname, items = sitems)

            BAGS[key] = bag

        except:
            failedBags.append(str(key))

    if len(failedBags) > 0:
        PostErrorMessage("ERROR while loading bags! Could not find/open the following bag(s): " + str(failedBags))

def LoadSettings():
    '''Calls the saved settings file and loads the settings to file.'''
    defaults = {
    'MAX_BAGS': 10,
    'MAX_ITEMS': 5000,
    'LAST_BAG_OPENED': 0,
    'NOOBIE_TIPS': True}

    opts = defaults

    # Settings file existed before this load. Attempt to read settings.
    if optsStore.exists('existed'):
        try:
            opts = dict(optsStore.get('opts')['d'])

            MAX_BAGS = int(opts['MAX_BAGS'])
            MAX_ITEMS = int(opts['MAX_ITEMS'])
            LAST_BAG_OPENED = int(opts['LAST_BAG_OPENED'])
            NOOBIE_TIPS = bool(opts['NOOBIE_TIPS'])
        except:
            PostErrorMessage("ERROR: Saved settings file existed, but is empty. Preferences reset to defaults.")
            optsStore.put('opts', d = defaults)
    else:
        optsStore.put('existed', d = True)
        optsStore.put('opts', d = defaults)


# Fetch and Update data
def GetNewItemID():
    '''Gets an unused itemID number.'''
    for i in range(MAX_ITEMS):
        if not itemStore.exists(i): return i

    PostErrorMessage("No more items available!")
    return None

def GetNewBagID():
    '''Gets an unused bagID number.'''
    for i in range(MAX_BAGS):
        if not bagsStore.exists(i): return i

    PostErrorMessage("No more bags available!")
    return None


# Create new items or bags
def CreateItem(item):
    '''Adds the specified item to the local list (ITEMS), saves the item to memory, and updates the indices for items in the save file.'''
    ITEMS.append(item.ID)

    UpdateItemInfo(item)

def CreateBag(bag):
    '''Adds the specified bag to the local list (BAGS), saves the bag to memory, and updates the indices for bags in the save file.'''
    BAGS[bag.ID] = bag

    SaveBagInfo(bag)


# Remove unwanted items
def RemoveItemFromBag(itemID, bagID):
    '''Removes the specified item from the "items" list owned by the specified bag.'''
    # First, remove it from the instanced ITEMS list
    ITEMS.remove(GetItemIndex(itemID))
    BAGS[bagID].items.remove(itemID)

    SaveBagInfo(BAGS[bagID])


# Read/Write to save files
def SaveBagInfo(scBag):
    '''Stores the bag by copying a shallow copy of the actual bag.'''
    bagsStore.put(scBag.ID, name = scBag.name, items = scBag.items)

def SaveItemInfo(scItem):
    '''Stores the item by copying a shallow copy of the actual item.'''
    itemStore.put(scItem.ID, name = scItem.name, qty = scItem.qty, mass = scItem.mass,
                  desc = scItem.desc, icon = scItem.icon, tags = scItem.tags)

def DeleteItemFromSave(itemID):
    '''Removes the item from itemStore save file. This does not remove the item from bags that it may be saved in.'''
    itemStore.delete(itemID)

def DeleteBagFromSave(bagID):
    '''Removes the bag from bagsStore save file.'''
    bagsStore.delete(bagID)
