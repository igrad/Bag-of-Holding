from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *

def OpenContPane_Items(obj):
    OpenBag(CURRENTBAG)
    contpane_items.pos = CONT_POS
    contpane_new.pos = CONT_POS_R

def OpenBag(openBagID):
    LoadBags()
    
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
    bag = BAGS[bagID]

    # Update the bag title on-screen
    # TODO Update loaded bag's title at the top of screen

    # Update the contents of the contPane GridLayout by creating individual ItemViews
    cont_List.clear_widgets()
    ITEMVIEWS.clear()

    LoadItems(bag.items)

    for itemID in bag.items:
        itemID = int(itemID)

        newItem = ItemView(itemID = itemID)

        # Filters still need to be applied after opening a new bag
        # TODO Apply filters after opening new bag

        # Add the remaining ItemViews to the grid
        # NOTE This will need to be made a function of the filter. IE, if the item
        # NOTE passes through the filter, post it to the grid.

        cont_List.add_widget(newItem)

def UpdateItemList():
    cont_Scroll.clear_widgets()

    cont_List.bind(minimum_height = cont_List.setter('height'))
    cont_Scroll.add_widget(cont_List)

    contpane_items.clear_widgets()
    contpane_items.add_widget(cont_Scroll)
