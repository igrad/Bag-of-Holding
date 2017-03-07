from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *

def OpenContPane_Items(obj):
    PopulateItemViews(CURRENTBAG)

def UpdateItemList():
    contScroll.clear_widgets()

    contList.bind(minimum_height = contList.setter('height'))
    contScroll.add_widget(contList)

    cont.clear_widgets()
    cont.add_widget(contScroll)

def PopulateItemViews(openBagID):
    bag = BAGS[openBagID]

    # Update the contents of the contPane GridLayout by creating individual ItemViews
    contList.clear_widgets()
    ITEMVIEWS.clear()

    for itemID in bag.items:
        itemID = int(itemID)

        newItem = ItemView(itemID = itemID)

        # Filters still need to be applied after opening a new bag
        # TODO Apply filters after opening new bag

        # Add the remaining ItemViews to the grid
        # NOTE This will need to be made a function of the filter. IE, if the item
        # NOTE passes through the filter, post it to the grid.

        contList.add_widget(ITEMVIEWS[int(itemID)])

    UpdateItemList()

def OpenBag(openBagID):
    LoadBags(openBagID)

    bagIDs = BAGS.keys()
    bagID = 0

    if len(bagIDs) < 1:
        newBag = Bag()
        bagID = newBag.ID
    else:
        if openBagID in bagIDs:
            bagID = openBagID
        else:
            # TODO Notify user that the bag they've selected could not be found
            bagID = BAGS[bagIDs[0]]

    CURRENTBAG = bagID

    LoadItems(BAGS[bagID].items)

    # Update the bag title on-screen
    # TODO Update loaded bag's title at the top of screen

    PopulateItemViews(openBagID)
