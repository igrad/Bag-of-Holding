from SysFuncs import *
from AppInit import *
from Bag import *
from BagItem import *

# This file contains all of the button-bound functions relating to the creation of a new
# BagItem through the New tab on the main screen of the app.

def OpenContPane_New(obj):
    new_name.text = ''
    new_icon.source = 'images/blankIcon.png'
    new_qty.text = ''
    new_weight.text = ''
    new_val.text = ''
    new_tags.text = ''
    new_desc.text = ''

    contpane_items.pos = CONT_POS_L
    contpane_new.pos = CONT_POS

def InputItem(obj):
    '''Process the values input on the New Item screen, create a new item from those values, save it to memory, and add it to the currently-opened bag.'''
    # Set the defaults to input if the user didn't enter anything
    if new_name.text == '': new_name.text = 'Unnamed Item'
    if new_icon.source == '': new_icon.source = 'images/blankIcon.png'
    if new_qty.text == '': new_qty.text = '1'
    if new_weight.text == '': new_weight.text = '0'
    if new_val.text == '': new_val.text = '0'
    if new_tags.text == '': new_tags.text = 'notag'
    if new_desc.text == '': new_desc.text = 'An undescribable item!'

    # Create the item itself. Automtically added to ITEMS
    newItem = BagItem(name = new_name.text, icon = new_icon.source, qty = new_qty.text,
        weight = new_weight.text, val = new_val.text, tags = new_tags.text,
        desc = new_desc.text)

    # Add the item to the open bag
    BAGS[CURRENTBAG].AddItem(newItem.ID)

    # Display a success message to the user

    # Reset text input fields
    new_name.text = ''
    new_icon.source = 'images/blankIcon.png'
    new_qty.text = ''
    new_weight.text = ''
    new_val.text = ''
    new_tags.text = ''
    new_desc.text = ''
