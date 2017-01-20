from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *

def OpenContPane_Filters(obj):
    # Do not reset any fields
    anim = Animation(pos = CONT_POS_FILTERS, duration = T_SCREENSHIFT, t = ANIMTYPE)
    anim.start(contpane)
