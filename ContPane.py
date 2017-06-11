from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *
from Tabs import *

from kivy.clock import Clock, partial


COMPARISONPHRASES = []

FIELDS = ['name', 'qty', 'quantity', 'lbs', 'kg', 'weight', 'val', 'value', 'tag', 'tags', 'desc', 'description']
COMPARATORS = ['=', '>', '<']

SEARCHTRIGGEREVENT = None

def BuildSearchTimer(obj, value):
    global SEARCHTRIGGEREVENT
    SEARCHTRIGGEREVENT = Clock.schedule_once(partial(LiveFilterFromSearch, obj, value), 0.5)
    SEARCHTRIGGEREVENT.cancel()


def ScheduleSearch(obj, value):
    global SEARCHTRIGGEREVENT

    if SEARCHTRIGGEREVENT == None:
        BuildSearchTimer(obj, value)
    try:
        SEARCHTRIGGEREVENT.cancel()
        SEARCHTRIGGEREVENT = Clock.schedule_once(partial(LiveFilterFromSearch, obj, value), 0.5)
    except:
        LogErr('Search not scheduled yet')


def GenerateComparisonPhrases():
    items = BAGS[CURRENTBAG].items
    z = [[x + y for x in FIELDS] for y in COMPARATORS]

    for x in z:
        for y in x:
            COMPARISONPHRASES.append(y)


def PopulateItemViews(openBagID, items = None):
    '''Create the ItemView objects and put them on-screen.
    str openBagID: ID number of the bag to open.
    List items: list of items to be loaded, defaults to None to load all items in bag.'''
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

    checkSearchInput = False
    if items == None:
        items = bag.items
        checkSearchInput = True

    for itemID in items:
        itemID = str(itemID)

        newItem = ItemView(itemID = itemID)

        if bag.view == 'card':
            newItem.SetDescNumLines()

        contList.add_widget(ITEMVIEWS[str(itemID)])



    # Apply the search input parameters if not explicitly specified in the items arg
    if checkSearchInput == True:
        LiveFilterFromSearch(None, None)

    # Filters of this bag need to be applied
    # TODO Apply filters after opening new bag

    # Add the remaining ItemViews to the grid
    # This will need to be made a function of the filter. IE, if the item
    # passes through the filter, post it to the grid.


def FilterItemViews(filterPart):
    '''Identify which items within this bag should be included in the search results.
    ----------
    List filterPart: A list of three strings
        [0]: Attribute to be checked. If 'any', will check all attributes of the item
        [1]: The value which we compare the attribute values to.
        [2]: The comparison operator, '==', '>', '<', or ' in '.'''

    def ExtractNumber(string):
        number = ''
        for x in str(string):
            if x in '0123456789,.':
                number += x

        if number != '':
            return float(number)
        else:
            return string

    try:
        # Determine if a specific field is being queried
        params = [filterPart[0]]
        evalStrings = []

        if filterPart[0] == 'any':
            params = ['name', 'qty', 'weight', 'val', 'tags', 'desc']

        for param in params:
            typedPart0 = ''
            typedPart1 = ''

            if filterPart[2] == ' in ':
                typedPart0 = 'str(filterPart[1]).lower()'
                typedPart1 = 'str(ITEMS[key].' + param + ').lower()'
            elif str(filterPart[1]).isdigit:
                typedPart0 = 'float(ExtractNumber(ITEMS[key].' + param + '))'
                typedPart1 = str(float(filterPart[1]))

            evalStrings.append(typedPart0 + filterPart[2] + typedPart1)

            #print("evalStr == " + typedPart0 + filterPart[2] + typedPart1)

        passed = []
        for key in ITEMS.keys():
            for evalStr in evalStrings:
                try:
                    if eval(evalStr):
                        passed.append(key)
                        break
                except ValueError:
                    LogExc('ValueError raised: ')
                    continue

        PopulateItemViews(CURRENTBAG, passed)

        return True

    except Exception as ex:
        LogExc('ContPane.FilterItemViews(' + str(filterPart) + ')')
        return False


def LiveFilterFromSearch(obj, value, dt = 0):
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

    if dt != 0 and compString == '':
        # If this func was triggered by a scheduled search, we can force the ContPane to
        # update when there's nothing input.
        PopulateItemViews(CURRENTBAG)
        return False
    elif compString == '':
        # If this func was NOT triggered by a scheduled search, we cannot force the
        # ContPane update because this function is nested in other functions. All we
        # need is the return value indicating that there is nothing in the search field.
        return False

    try:
        # Check if any comparison phrases are found in the query
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

                if '=' in phrase and '==' not in compString:
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


        # If no phrases are found, perform a regular search
        FilterItemViews(['any', value, ' in '])

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

    if btn == 'picknoupdate':
        pick.is_open = True
        pick.pos = PICK.pos
    elif (pick.pos == list(PICK.pos)) or (btn == None):
        pick.is_open = False
        pick.pos = SCREEN_POS_OFF

        args = dict()
        if pickName.text != str(ITEMS[pick.itemID].name):
            args['name'] = str(pickName.text)
        if pickIcon.background_normal != ITEMS[pick.itemID].icon:
            args['icon'] = str(pickIcon.background_normal)
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
    else:
        pick.is_open = True

        if type(btn) != int:
            pick.itemID = btn.itemID

        pickName.text = ITEMS[pick.itemID].name
        #pickIcon.source = ITEMS[pick.itemID].icon
        pickIcon.background_normal = ITEMS[pick.itemID].icon
        pickIcon.background_down = ITEMS[pick.itemID].icon
        pickQty_I.text = str(ITEMS[pick.itemID].qty)
        pickWeight_I.text = str(ITEMS[pick.itemID].weight)
        pickVal_I.text = str(ITEMS[pick.itemID].val)
        pickTags.text = str(ITEMS[pick.itemID].tags)
        pickDesc.text = str(ITEMS[pick.itemID].desc)

        try:
            pickIcon.selected = int(ITEMS[pick.itemID].icon[-7:-4])
        except:
            pickIcon.selected = None

        pick.pos = PICK.pos
