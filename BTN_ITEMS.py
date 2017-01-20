from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *

def OpenContPane_Items(obj):
    PopulateItemViews(CURRENTBAG)

    time = T_SCREENSHIFT
    if list(contpane.pos) == list(CONT_POS_NEW):
        time = time * 3

    anim = Animation(pos = CONT_POS_ITEMS, duration = time, t = ANIMTYPE)
    anim.start(contpane)

def UpdateItemList():
    cont_Scroll.clear_widgets()

    cont_List.bind(minimum_height = cont_List.setter('height'))
    cont_Scroll.add_widget(cont_List)

    contpane_items.clear_widgets()
    contpane_items.add_widget(cont_Scroll)

def PopulateItemViews(openBagID):
    bag = BAGS[openBagID]

    # Update the contents of the contPane GridLayout by creating individual ItemViews
    cont_List.clear_widgets()
    ITEMVIEWS.clear()

    print('number of items in bag ' + str(len(bag.items)))

    for itemID in bag.items:
        itemID = int(itemID)

        newItem = ItemView(itemID = itemID)

        # Filters still need to be applied after opening a new bag
        # TODO Apply filters after opening new bag

        # Add the remaining ItemViews to the grid
        # NOTE This will need to be made a function of the filter. IE, if the item
        # NOTE passes through the filter, post it to the grid.

        print('ITEMVIEWS keys ' + str(ITEMVIEWS.keys()))

        cont_List.add_widget(ITEMVIEWS[int(itemID)])

    UpdateItemList()

def OpenBag(openBagID):
    print('opening bag ' + str(openBagID))
    LoadBags(openBagID)

    bagIDs = BAGS.keys()
    bagID = 0

    if len(bagIDs) < 1:
        print('no bags found, creating new bag')
        newBag = Bag()
        bagID = newBag.ID
    else:
        if openBagID in bagIDs:
            bagID = openBagID
            print('found bag')
        else:
            # TODO Notify user that the bag they've selected could not be found
            bagID = BAGS[bagIDs[0]]
            print('could not find bag, opening different bag instead')

    CURRENTBAG = bagID

    LoadItems(BAGS[bagID].items)

    # Update the bag title on-screen
    # TODO Update loaded bag's title at the top of screen

    PopulateItemViews(openBagID)
