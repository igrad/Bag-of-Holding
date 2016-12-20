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
