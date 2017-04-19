from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *
from Tabs import *


def PopulateItemViews(openBagID):
    bag = BAGS[openBagID]

    # Update the contents of the contPane GridLayout by creating individual ItemViews
    contList.clear_widgets()
    ITEMVIEWS.clear()

    if bag.view == 'cozy':
        ItemView = CozyView
        contList.row_default_height = ITEMVIEW_COZY.h
    elif bag.view == 'norm':
        ItemView = NormView
        contList.row_default_height = ITEMVIEW_NORM.h
    elif bag.view == 'card':
        ItemView = CardView
        contList.row_default_height = ITEMVIEW_CARD.h

    for itemID in bag.items:
        itemID = int(itemID)

        newItem = ItemView(itemID = itemID)

        # Filters still need to be applied after opening a new bag
        # TODO Apply filters after opening new bag

        # Add the remaining ItemViews to the grid
        # NOTE This will need to be made a function of the filter. IE, if the item
        # NOTE passes through the filter, post it to the grid.

        contList.add_widget(ITEMVIEWS[int(itemID)])


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
    VIEW_TYPE = BAGS[bagID].view

    LoadItems(BAGS[bagID].items)

    # Update the bag title on-screen
    menuTitle.text = BAGS[CURRENTBAG].name

    PopulateItemViews(openBagID)

    HighlightView(VIEW_TYPE)

def HighlightView(viewType):
    if viewType == 'norm':
        viewNorm_Check.source = VIEW_CHECK_ACTIVE
        viewCozy_Check.source = VIEW_CHECK_INACTIVE
        viewCard_Check.source = VIEW_CHECK_INACTIVE
    if viewType == 'cozy':
        viewNorm_Check.source = VIEW_CHECK_INACTIVE
        viewCozy_Check.source = VIEW_CHECK_ACTIVE
        viewCard_Check.source = VIEW_CHECK_INACTIVE
    if viewType == 'card':
        viewNorm_Check.source = VIEW_CHECK_INACTIVE
        viewCozy_Check.source = VIEW_CHECK_INACTIVE
        viewCard_Check.source = VIEW_CHECK_ACTIVE

def SelectItem(btn):

    if pick.pos != list(PICK.pos):
        LogMsg('Item selected: ' + str(btn.dname.text))
        itemID = btn.itemID

        pickName.text = ITEMS[itemID].name
        pickIcon.source = ITEMS[itemID].icon
        pickQty.text = 'Quantity: ' + str(ITEMS[itemID].qty)
        pickWeight.text = 'Weight: ' + str(ITEMS[itemID].weight)
        pickVal.text = 'Value: ' + str(ITEMS[itemID].val)
        pickDesc.text = ITEMS[itemID].tags + '\n' + str(ITEMS[itemID].desc)

        pick.pos = PICK.pos

    else:
        pick.pos = SCREEN_POS_OFF
