from SysFuncs import *
from Bag import *
from BagItem import *

# Load data
def LoadData():
    LoadBags()
    LoadSettings()

def LoadItems(keys):
    '''Create a temp copy of the items store in itemStore, and make them accessible to the user by appending them to the ITEMS dict.'''
    failedItems = list()

    ITEMS.clear()

    itemStore = JsonStore('item_data.json')

    for key in keys:
        key = str(key)
        try:
            sname = str(itemStore.get(key)['name'])
            sqty = str(itemStore.get(key)['qty'])
            sweight = str(itemStore.get(key)['weight'])
            sval = str(itemStore.get(key)['val'])
            sdesc = str(itemStore.get(key)['desc'])
            sicon = str(itemStore.get(key)['icon'])
            stags = list(itemStore.get(key)['tags'])

            item = BagItem(ID = key, name = sname, qty = sqty, weight = sweight,
                val = sval, desc = sdesc, icon = sicon, tags = stags)

            ITEMS[item.ID] = item

        except Exception as ex:
            LogMsg("ERROR: LoadItems() error on itemID " + str(key) + ": " + str(ex))
            failedItems.append(key)

    if len(failedItems) > 0:
        LogMsg("ERROR: Could not load the following items: " + str(failedItems))

def LoadBags(bagKey = None):
    '''Create a temp copy of the bags stored in bagsStore, and make them accessible to the user by appending them to the BAGS dict.'''
    failedBags = list()

    bagsStore = JsonStore('bags_data.json')
    bagRange = list(bagsStore.keys())

    # A bag ID has been specified. Only load that bag
    if bagKey != None:
        bagRange = [bagKey]

    for key in bagRange:
        key = str(key)
        try:
            sname = str(bagsStore.get(key)['name'])
            sitems = list(bagsStore.get(key)['items'])
            scurrency = list(bagsStore.get(key)['currency'])
            sview = str(bagsStore.get(key)['view'])

            newBag = Bag(ID = key, name = sname, items = sitems,
                currency = scurrency, view = sview)

            BAGS[key] = newBag

        except Exception as ex:
            LogMsg('ERROR || Bag exception raised, could not load bag ' + str(key) + '. Returned error: ' + str(ex))
            failedBags.append(str(key))

    if len(failedBags) > 0:
        LogMsg("ERROR while loading bags! Could not find/open the following bag(s): " + str(failedBags))

def LoadSettings():
    '''Calls the saved settings file and loads the settings to file.'''
    defaults = {
    'MAX_BAGS': 10,
    'MAX_ITEMS': 5000,
    'LAST_BAG_OPENED': 0}

    opts = defaults

    optsStore = JsonStore('user_settings.json')

    # Settings file existed before this load. Attempt to read settings.
    if optsStore.exists('existed'):
        try:
            opts = dict(optsStore.get('opts')['d'])

            MAX_BAGS = int(opts['MAX_BAGS'])
            MAX_ITEMS = int(opts['MAX_ITEMS'])
            LAST_BAG_OPENED = int(opts['LAST_BAG_OPENED'])
        except:
            LogMsg("ERROR: Saved settings file existed, but is empty. Preferences reset to defaults.")
            optsStore.put('opts', d = defaults)
    else:
        optsStore.put('existed', d = True)
        optsStore.put('opts', d = defaults)
