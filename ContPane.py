from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *
from Tabs import *


COMPARISONPHRASES = []

FIELDS = ['name', 'qty', 'quantity', 'lbs', 'kg', 'weight', 'val', 'value', 'tag', 'tags', 'desc', 'description']
COMPARATORS = ['=', '>', '<']


def GenerateComparisonPhrases():
    items = BAGS[CURRENTBAG].items

    z = [[x + y for x in FIELDS] for y in COMPARATORS]

    for x in z:
        for y in x:
            COMPARISONPHRASES.append(y)


def PopulateItemViews(openBagID, items = None):
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

    if items == None:
        items = bag.items
    else:
        print('Loading filter to screen...')

    for itemID in items:
        itemID = str(itemID)

        newItem = ItemView(itemID = itemID)

        # Apply the search input parameters if not explicitly specified in the items arg
        if items == None:
            LiveFilterFromSearch(None, None, False)

        # Filters of this bag need to be applied
        # TODO Apply filters after opening new bag

        # Add the remaining ItemViews to the grid
        # This will need to be made a function of the filter. IE, if the item
        # passes through the filter, post it to the grid.

        contList.add_widget(ITEMVIEWS[str(itemID)])


def FilterItemViews(filterPart):
    try:
        typedPre = 'str(ITEMS[key].' + filterPart[0] + ')'
        typedPart1 = 'str(filterPart[1])'

        if str(filterPart[1]).isdigit:
            typedPre = 'int(ITEMS[key].' + filterPart[0] + ')'
            typedPart1 = 'int(filterPart[1])'

        evalStr = typedPre + filterPart[2] + typedPart1
        print('\nEvalStr == ' + evalStr)

        passed = []
        for key in ITEMS.keys():
            try:
                if eval(evalStr):
                    passed.append(key)
            except ValueError:
                continue

        PopulateItemViews(CURRENTBAG, passed)

        return True

    except Exception as ex:
        LogExc('ContPane.FilterItemViews(' + str(filterPart) + ')')
        return False


def LiveFilterFromSearch(obj, value, forceupdate = True):
    '''Generate filter for the ContPane as text is input to the search bar.
    ----------
    None obj: The widget from which this request came
    Str value: Text input/search string
    Bool forceupdate: If false, this will not force the ContPane to refresh

    If a search filter is successfully applied, returns True. If no changes are made,
    returns False.'''
    if value == None:
        value = str(searchInput.text)

    compString = value.replace(' ', '').lower()

    if compString == '':
        return False

    try:
        for phrase in COMPARISONPHRASES:
            if phrase in compString:
                if phrase == compString:
                    return

                def ReplacePhrase(newWord, compString = compString, phrase = phrase):
                    compString = compString.replace(phrase[:-1], newWord)
                    phrase = str(newWord) + str(phrase[-1:])

                    return compString, phrase

                if 'quantity' in phrase:
                    compString, phrase = ReplacePhrase('qty')
                elif 'lbs' in phrase or 'kg' in phrase:
                    compString, phrase = ReplacePhrase('weight')
                elif 'value' in phrase:
                    compString, phrase = ReplacePhrase('val')

                print('Phrase going into = comparison: {0}'.format(phrase))
                if '=' in phrase:
                    compString = compString.replace(phrase, phrase + '=')
                    phrase = str(phrase) + '='

                comp = []

                if '==' in compString:
                    comp = compString.split('==', 1)
                    comp.append('==')
                elif '>' in compString:
                    comp = compString.split('>', 1)
                    comp.append('>')
                elif '<' in compString:
                    comp = compString.split('<', 1)
                    comp.append('<')
                else:
                    return False

                # If the filter could not be applied correctly, end the sequence
                if not FilterItemViews(comp):
                    return False

                # If the filter was applied successfully, exit with success code
                return True

        # If forceupdate is true, force a visual update in ContPane
        if forceupdate:
            PopulateItemViews(CURRENTBAG)

            return True

    except Exception as ex:
        LogExc('LiveFilterFromSearch(' + str(obj) + ', ' + str(value) + ')')

        return False


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
    '''Check the corresponding view selection in the VIEW tab.'''
    viewNorm_Check.source = VIEW_CHECK_INACTIVE
    viewCozy_Check.source = VIEW_CHECK_INACTIVE
    viewCard_Check.source = VIEW_CHECK_INACTIVE

    if viewType == 'norm': viewNorm_Check.source = VIEW_CHECK_ACTIVE
    elif viewType == 'cozy': viewCozy_Check.source = VIEW_CHECK_ACTIVE
    elif viewType == 'card': viewCard_Check.source = VIEW_CHECK_ACTIVE


def SelectItem(btn):
    '''Called when an ItemView is called for display in the PICK screen.'''
    if pick.pos != list(PICK.pos):
        pick.itemID = btn.itemID
        pickName.text = ITEMS[pick.itemID].name
        pickIcon.source = ITEMS[pick.itemID].icon
        pickQty_I.text = str(ITEMS[pick.itemID].qty)
        pickWeight_I.text = str(ITEMS[pick.itemID].weight)
        pickVal_I.text = str(ITEMS[pick.itemID].val)
        pickTags.text = str(ITEMS[pick.itemID].tags)
        pickDesc.text = str(ITEMS[pick.itemID].desc)

        pick.pos = PICK.pos
    else:
        pick.pos = SCREEN_POS_OFF

        args = dict()
        if pickName.text != str(ITEMS[pick.itemID].name):
            args['name'] = str(pickName.text)
        if pickIcon.source != ITEMS[pick.itemID].icon:
            args['icon'] = str(pickIcon.source)
        if pickQty_I.text != str(ITEMS[pick.itemID].qty):
            args['qty'] = str(pickQty_I.text)
        if pickWeight_I.text != str(ITEMS[pick.itemID].weight):
            args['weight'] = str(pickWeight_I.text)
        if pickVal_I.text != str(ITEMS[pick.itemID].val):
            args['val'] = str(pickVal_I.text)
        if pickTags.text != str(ITEMS[pick.itemID].tags):
            args['tags'] = str(pickTags.text)
        if pickDesc.text != str(ITEMS[pick.itemID].desc):
            args['desc'] = str(pickDesc.text)

        if len(args) > 0:
            ITEMS[pick.itemID].UpdateItem(**args)
            ITEMVIEWS[str(pick.itemID)].UpdateItemView(**args)
