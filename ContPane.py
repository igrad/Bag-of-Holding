from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *
from Tabs import *

from kivy.clock import Clock, partial


SORT_ATTR = 'Name'
SORT_METHOD = 'Ascending'

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
    bag = BAGS[str(openBagID)]

    # Update the contents of the contPane GridLayout by creating individual ItemViews
    cont.list.clear_widgets()
    ITEMVIEWS.clear()

    if bag.view == 'cozy':
        ItemView = CozyView
        cont.list.row_default_height = cont.ITEMVIEW_COZY.h
    elif bag.view == 'norm':
        ItemView = NormView
        cont.list.row_default_height = cont.ITEMVIEW_NORM.h
    elif bag.view == 'card':
        ItemView = CardView
        cont.list.row_default_height = cont.ITEMVIEW_CARD.h

    # If no items were explicitly listed for this function, check the search input to see
    # if there's anything worthwhile there.
    checkSearchInput = False
    if items == None:
        items = bag.items
        checkSearchInput = True

    # Apply the sorting method to the items of this bag
    items = ApplySort(items)

    bg_var = 0
    for itemID in items:
        itemID = str(itemID)

        newItem = ItemView(itemID = itemID, bg_var = bg_var)

        if bag.view == 'card':
            newItem.SetDescNumLines()

        cont.list.add_widget(ITEMVIEWS[str(itemID)])

        bg_var += 1

    # Apply the search input parameters if not explicitly specified in the items arg
    if checkSearchInput == True:
        LiveFilterFromSearch(None, None)


def FilterItemViews(filterPart):
    '''Identify which items within this bag should be included in the search results.
    ----------
    List filterPart: A list of three strings
        [0]: Attribute to be checked. If 'any', will check all attributes of the item
        [1]: The value which we compare the attribute values to.
        [2]: The comparison operator, '==', '>', '<', or ' in '.'''

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
        value = str(search.input.text)

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
    openBagID = str(openBagID)
    LoadBags(openBagID)

    bagIDs = list(BAGS.keys())
    bagID = 0

    if len(bagIDs) < 1:
        newBag = Bag()
        bagID = newBag.ID
    else:
        if openBagID in bagIDs:
            bagID = openBagID
        else:
            # TODO Notify user that the bag they've selected could not be found
            bagID = str(bagIDs[0])

    CURRENTBAG = bagID
    VIEW_TYPE = BAGS[bagID].view

    LoadItems(BAGS[bagID].items)

    # Update the bag title on-screen
    menu.title.text = BAGS[CURRENTBAG].name

    PopulateItemViews(openBagID)

    HighlightView(VIEW_TYPE)


def HighlightView(viewType):
    '''Check the corresponding view selection in the VIEW tab.'''
    dview.norm_Check.source = VIEW_CHECK_INACTIVE
    dview.cozy_Check.source = VIEW_CHECK_INACTIVE
    dview.card_Check.source = VIEW_CHECK_INACTIVE

    if viewType == 'norm': dview.norm_Check.source = VIEW_CHECK_ACTIVE
    elif viewType == 'cozy': dview.cozy_Check.source = VIEW_CHECK_ACTIVE
    elif viewType == 'card': dview.card_Check.source = VIEW_CHECK_ACTIVE


def SelectItem(btn):
    '''Called when an ItemView is called for display in the PICK screen.'''

    if btn == 'picknoupdate':
        pick.open()
    elif (pick.is_open) or (btn == None):
        pick.close()

        args = dict()
        if pick.name.text != str(ITEMS[pick.itemID].name):
            args['name'] = str(pick.name.text)
        if pick.icon.background_normal != ITEMS[pick.itemID].icon:
            args['icon'] = str(pick.icon.background_normal)
        if pick.qty_I.text != str(ITEMS[pick.itemID].qty):
            args['qty'] = str(pick.qty_I.text)
        if pick.weight_I.text != str(ITEMS[pick.itemID].weight):
            args['weight'] = str(pick.weight_I.text)
        if pick.val_I.text != str(ITEMS[pick.itemID].val):
            args['val'] = str(pick.val_I.text)
        if pick.tags.text != str(ITEMS[pick.itemID].tags):
            args['tags'] = str(pick.tags.text)
        if pick.desc.text != str(ITEMS[pick.itemID].desc):
            args['desc'] = str(pick.desc.text)

        if len(args) > 0:
            ITEMS[pick.itemID].UpdateItem(**args)
            ITEMVIEWS[str(pick.itemID)].UpdateItemView(**args)
    else:
        if type(btn) != int:
            pick.itemID = btn.itemID

        pick.name.text = ITEMS[pick.itemID].name
        #pick.icon.source = ITEMS[pick.itemID].icon
        pick.icon.background_normal = ITEMS[pick.itemID].icon
        pick.icon.background_down = ITEMS[pick.itemID].icon
        pick.qty_I.text = str(ITEMS[pick.itemID].qty)
        pick.weight_I.text = str(ITEMS[pick.itemID].weight)
        pick.val_I.text = str(ITEMS[pick.itemID].val)
        pick.tags.text = str(ITEMS[pick.itemID].tags)
        pick.desc.text = str(ITEMS[pick.itemID].desc)

        try:
            pick.icon.selected = int(ITEMS[pick.itemID].icon[-7:-4])
        except:
            pick.icon.selected = None

        pick.opts.itemID = pick.itemID

        pick.open()


def ApplySort(obj):
    '''Apply the sorting method to the contents of the bag.'''
    reverse = False

    global SORT_METHOD, SORT_ATTR

    if SORT_METHOD == 'Descending':
        reverse = True

    if SORT_ATTR == 'Name':
        return [y.ID for y in sorted([ITEMS[str(item)] for item in obj],
        key = lambda x: x.name, reverse = reverse)]
    elif SORT_ATTR == 'Quantity':
        return [y.ID for y in sorted([ITEMS[str(item)] for item in obj],
        key = lambda x: x.qty, reverse = reverse)]
    elif SORT_ATTR == 'Weight':
        return [y.ID for y in sorted([ITEMS[str(item)] for item in obj],
        key = lambda x: x.weight, reverse = reverse)]
    elif SORT_ATTR == 'Value':
        return [y.ID for y in sorted([ITEMS[str(item)] for item in obj],
        key = lambda x: x.val, reverse = reverse)]


def SortChanged(attr, method):
    '''Indicate that the sorting parameters have been changed.'''
    global SORT_ATTR, SORT_METHOD
    SORT_ATTR = attr
    SORT_METHOD = method
