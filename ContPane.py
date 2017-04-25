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
    viewNorm_Check.source = VIEW_CHECK_INACTIVE
    viewCozy_Check.source = VIEW_CHECK_INACTIVE
    viewCard_Check.source = VIEW_CHECK_INACTIVE

    if viewType == 'norm': viewNorm_Check.source = VIEW_CHECK_ACTIVE
    elif viewType == 'cozy': viewCozy_Check.source = VIEW_CHECK_ACTIVE
    elif viewType == 'card': viewCard_Check.source = VIEW_CHECK_ACTIVE

def SelectItem(btn):
    if pick.pos != list(PICK.pos):
        pick.itemID = itemID = btn.itemID
        pickName.text = ITEMS[itemID].name
        pickIcon.source = ITEMS[itemID].icon
        pickQty_I.text = str(ITEMS[itemID].qty)
        pickWeight_I.text = str(ITEMS[itemID].weight)
        pickVal_I.text = str(ITEMS[itemID].val)
        pickDesc.text = ITEMS[itemID].tags + '\n' + str(ITEMS[itemID].desc)

        pick.pos = PICK.pos
    else:
        pick.pos = SCREEN_POS_OFF

def EditItem(btn):
    if editWidges.pos != list(ZEROS):
        itemID = pick.itemID
        editName.text = ITEMS[itemID].name
        editIcon.source = ITEMS[itemID].icon
        editQty.text = str(ITEMS[itemID].qty)
        editWeight.text = str(ITEMS[itemID].weight)
        editVal.text = str(ITEMS[itemID].val)
        editTags.text = str(ITEMS[itemID].tags)
        editDesc.text =  ITEMS[itemID].desc

        editWidges.pos = ZEROS
        pickWidges.pos = SCREEN_POS_OFF

    else:
        editWidges.pos = SCREEN_POS_OFF
        pickWidges.pos = ZEROS
