from SysFuncs import *
from AppInit import *
from Bag import *
from Currency import *
from AnchorLabel import *

def OpenBagPickMenu(obj):
    '''Open up the bagPick menu on-screen.'''
    if bagPick.is_open:
        bagPick.pos = SCREEN_POS_OFF
        bagPick.is_open = False

    else:
        bagPick.pos = BAGPICK.pos
        bagPick.is_open = True
