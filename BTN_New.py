from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *

def OpenNew(obj):
    newName.text = ''
    newIcon.source = 'images/blankIcon.png'
    newQty.text = ''
    newWeight.text = ''
    newVal.text = ''
    newTags.text = ''
    newDesc.text = ''


def InputItem(obj):
    '''Process the values input on the New Item screen, create a new item from those
    values, save it to memory, and add it to the currently-opened bag.'''
    # Set the defaults to input if the user didn't enter anything
    if newName.text == '': newName.text = 'Unnamed Item'
    if newIcon.source == '': newIcon.source = 'images/blankIcon.png'
    if newQty.text == '': newQty.text = '1'
    if newWeight.text == '': newWeight.text = '1'
    if newVal.text == '': newVal.text = '1'
    if newTags.text == '': newTags.text = 'notag'
    if newDesc.text == '': newDesc.text = 'An undescribable item!'

    # Create the item itself. Automatically added to ITEMS
    newItem = BagItem(name = newName.text, icon = newIcon.source, qty = newQty.text,
        weight = newWeight.text, val = newVal.text, tags = newTags.text,
        desc = newDesc.text)

    # Add the item to the open bag
    BAGS[CURRENTBAG].AddItem(int(newItem.ID))

    # Display a success message to the user

    # Reset text input fields
    newName.text = ''
    newIcon.source = 'images/blankIcon.png'
    newQty.text = ''
    newWeight.text = ''
    newVal.text = ''
    newTags.text = ''
    newDesc.text = ''
