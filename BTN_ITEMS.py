from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *

def OpenContPane_Items(obj):
    contpane_items.pos = CONT_POS
    contpane_new.pos = CONT_POS_R

def OpenBag(openBagID):
    b = 0
    found = False
    bag = 0

    bagIDs = BAGS.keys()

    for ID in bagIDs:
        if ID == openBagID:
            b = ID
            found = True

    # Specified bag could not be found. Open the first bag listed instead and send a
    # notification to the user.
    if found:
        bag = BAGS[b]
    elif not found and len(bagIDs) > 0:
        # TODO Notify user that the bag they've selected could not be found
        bag = BAGS[0]
        print('BAG NOT FOUND, BAGS AVAILABLE')
    # User does not have any bags created
    elif not found and len(bagIDs) == 0:
        print('BAG NOT FOUND, NONE')
        bag = Bag()

    # Update the bag title on-screen
    # TODO Update loaded bag's title at the top of screen

    # Update the contents of the contPane GridLayout by creating individual ItemViews
    ITEMVIEWS.clear()
    cont_List.clear_widgets()
    i = 0

    print('INFO || Number of items to load: ' + str(len(bag.items)))

    LoadItems(bag.items)

    for itemID in bag.items:
        ITEMVIEWS.append(ItemView(itemID = itemID))

        # Filters still need to be applied after opening a new bag
        # TODO Apply filters after opening new bag

        # Add the remaining ItemViews to the grid
        # NOTE This will need to be made a function of the filter. IE, if the item
        # NOTE passes through the filter, post it to the grid.
        print("TROUBLESHOOTING || ITEMVIEWS entries: " + str([x.itemID for x in ITEMVIEWS]))
        print("TROUBLESHOOTING || ITEMVIEWS[0]: " + str(ITEMVIEWS[0]))

        cont_List.add_widget(ITEMVIEWS[i])

        i += 1

    # After all items have been posted to the grid for display, update the scroller's
    # height to reflect the size of the new grid.
    UpdateItemList()

def UpdateItemList():
    cont_Scroll.clear_widgets()

    cont_List.bind(minimum_height = cont_List.setter('height'))
    cont_Scroll.add_widget(cont_List)

    contpane_items.clear_widgets()
    contpane_items.add_widget(cont_Scroll)
