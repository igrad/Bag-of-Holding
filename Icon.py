from SysFuncs import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *
from ContPane import SelectItem
from Tabs import OpenNew


NUM_DEFAULT_ICONS = 54

def LoadIcon(index, selected = False, is_new = False):
    '''Load a single icon onto the icon.grid.
    ----------
    Int index: Index of the child to be loaded/reloaded
    Bool selected: Determines if the item is highlighted or not
    Bool is_new: Determines if an existing item needs to be deleted'''

    try:
        if not is_new:
            try:
                icon.grid.remove_widget(icon.grid.children[index])
            except IndexError:
                pass

        wrap = RelativeLayout()

        if selected:
            selectBorder = Image(source = 'images/IMG_SELECTOR.png',
            allow_stretch = True, keep_ratio = False)

            wrap.add_widget(selectBorder, 1)

            icon.selected = index

        btn = Button(background_normal = 'images/icons/{:03d}.png'.format(index),
        background_down = 'images/icons/{:03d}.png'.format(index), border = [0,0,0,0])

        wrap.add_widget(btn, 0)

        btn.index = index
        btn.bind(on_press = HighlightIcon)

        icon.grid.add_widget(wrap, index)
        return True

    except:
        LogExc('Icon.LoadIcon({}, {}, {})'.format(index, selected, is_new))
        return False


def HighlightIcon(obj):
    '''Called when one of the icon options is pressed.'''
    if icon.selected != None:
        LoadIcon(icon.selected)

    LoadIcon(obj.index, selected = True)
    icon.selected = obj.index


def SaveIcon(obj):
    '''Called whent the Save button on the Icon selection window is pressed.'''
    if icon.selected == None:
        OpenIconMenu(None)

    newbg = icon.grid.children[icon.selected].children[0].background_down

    if icon.called_from == 'pick':
        pick.icon.background_normal = pick.icon.background_down = newbg
        OpenIconMenu('picknoupdate')
    elif icon.called_from == 'new':
        dnew.icon.background_normal = dnew.icon.background_down = newbg
        dnew.icon.selected = icon.selected
        OpenIconMenu(None)


def LoadAllIcons():
    '''Load all of the default icons into the grid of selectable icons.'''
    icon.grid.clear_widgets()

    # Load icons in reverse order so that their indices are set appropriately
    for i in range(NUM_DEFAULT_ICONS):
        LoadIcon(i, is_new = True)

    icon.selected = None

    LogMsg('Loaded all icons')


def OpenIconMenu(obj):
    '''Opens the icon menu.'''
    if icon.is_open:
        Opens.close(icon)

        if icon.called_from == 'pick':
            if obj == 'picknoupdate':
                SelectItem('picknoupdate')
            else:
                SelectItem(int(pick.itemID))
        return
    else:
        if obj.selected != None:
            # Set the position of the selector in the Icons window

            if (icon.selected != None) and (icon.selected != obj.selected):
                # Reset the position of the selector highlight
                LoadIcon(icon.selected)

            LoadIcon(obj.selected, selected = True)
        else:
            # If no item is specified by the opener, then don't highlight anything
            if icon.selected != None:
                LoadIcon(icon.selected)
            icon.selected = None

        if pick.is_open and obj != 'picknoupdate':
            SelectItem(None)
            icon.called_from = 'pick'
        elif dnew.is_open:
            icon.called_from = 'new'

        Opens.open(icon)
