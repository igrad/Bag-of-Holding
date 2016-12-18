from SysFuncs import *
from Bag import *
from BagItem import *

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

    if len(failedItems) > 0:
        PostErrorMessage("ERROR: Could not load the following items: " + str(failedItems))

def LoadBags():
    '''Create a temp copy of the bags stored in bagsStore, and make them accessible to the user by appending them to the BAGS dict.'''
    failedBags = list()

    for key in bagsStore.keys():
        try:
            sname = str(bagsStore.get(str(key))['name'])
            sitems = dict(bagsStore.get(str(key))['items'])
            scurrency = list(bagsStore.get(str(key))['currency'])

            print('creating bag')
            newBag = Bag(ID = key, name = sname, items = sitems,
                currency = scurrency)
            print('created new bag')

            BAGS[int(key)] = newBag
            print('stored bag')

        except:
            print('bag exception raised')
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
