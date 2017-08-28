import SysFuncs
from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from ContPane import PopulateItemViews, HighlightView, SortChanged


#=======================================================================================#
# NEW                                                                                   #
#=======================================================================================#
def OpenNew(obj):
    '''Open/close the New drop menu from the tabs bar.'''
    if (dnew.is_open) or (obj == None):
        dnew.close()
        tabs.new.color = WHITE
    else:
        dnew.open()
        tabs.new.color = BLACK

        if dsort.is_open: OpenSort('close')
        if dview.is_open: OpenView('close')


def InputItem(obj):
    '''Process the values input on the New Item screen, create a new item from those
    values, save it to memory, and add it to the currently-opened bag.'''
    # Set the defaults to input if the user didn't enter anything
    if dnew.name.text == '': dnew.name.text = 'Unnamed Item'
    if dnew.icon.background_normal == '': dnew.icon.background_normal = 'images/blankIcon.png'
    if dnew.icon.background_down == '': dnew.icon.background_down = 'images/blankIcon.png'
    if dnew.qty.text == '': dnew.qty.text = '1'
    if dnew.weight.text == '': dnew.weight.text = '1'
    if dnew.val.text == '': dnew.val.text = '1'
    if dnew.tags.text == '': dnew.tags.text = 'notag'
    if dnew.desc.text == '': dnew.desc.text = 'An undescribable item!'

    # Create the item itself. Automatically added to ITEMS
    newItem = BagItem(name = dnew.name.text, icon = dnew.icon.background_normal,
        qty = dnew.qty.text, weight = dnew.weight.text, val = dnew.val.text,
        tags = dnew.tags.text, desc = dnew.desc.text)

    # Add the item to the open bag
    BAGS[CURRENTBAG].AddItem(int(newItem.ID))

    # Display a success message to the user

    # Reset text input fields
    dnew.name.text = ''
    dnew.icon.background_down = 'images/blankIcon.png'
    dnew.icon.background_normal = 'images/blankIcon.png'
    dnew.icon.selected = None
    dnew.qty.text = ''
    dnew.weight.text = ''
    dnew.val.text = ''
    dnew.tags.text = ''
    dnew.desc.text = ''

    PopulateItemViews(CURRENTBAG)


#=======================================================================================#
# SORT                                                                                  #
#=======================================================================================#
def OpenSort(obj):
    '''Open/close the Sort drop menu from the tabs bar.'''
    if (dsort.is_open) or (obj == 'open'):
        dsort.close()
        tabs.sort.color = WHITE
    else:
        dsort.open()
        tabs.sort.color = BLACK

        if dnew.is_open: OpenNew('close')
        if dview.is_open: OpenView('close')


def UpdateSort(obj):
    '''Called when one of the buttons within the sort menu is pressed.'''
    print('\n\nbutton pressed: ' + obj.text)

    sort_attr = ''
    sort_method = ''

    findAttr = True
    findMethod = True

    if obj.text in ['Name', 'Quantity', 'Weight', 'Value']:
        sort_attr = obj.text
        findAttr = False
    else:
        sort_method = obj.text
        findMethod = False

    if findAttr:
        l = ToggleButton.get_widgets('sortAttr')
        for item in l:
            if item.state == 'down':
                print('Found item currently activated: {}'.format(item.text))
                sort_attr = item.text

    if findMethod:
        l = ToggleButton.get_widgets('sortMethod')
        for item in l:
            if item.state == 'down':
                print('Found item currently activated: {}'.format(item.text))
                sort_method = item.text

    SortChanged(sort_attr, sort_method)
    PopulateItemViews(CURRENTBAG)


#=======================================================================================#
# VIEW                                                                                  #
#=======================================================================================#
def OpenView(obj):
    if (dview.is_open) or (obj == 'open'):
        dview.close()
        tabs.view.color = WHITE
    else:
        dview.open()
        tabs.view.color = BLACK

        if dnew.is_open: OpenNew('close')
        if dsort.is_open: OpenSort('close')


def SetView(obj):
    viewType = obj.view_type
    VIEW_TYPE = viewType
    BAGS[CURRENTBAG].UpdateBag(view = viewType)
    PopulateItemViews(CURRENTBAG)

    HighlightView(obj.view_type)
