from SysFuncs import *
from AppInit import *
from Bag import *
from Currency import *
from AnchorLabel import *

def PreviewBagMenu(btn):
    '''Open or close the bagOpen menu.'''
    if not bagOpen.is_open:
        bag = BAGS[btn.bagID]
        bagOpen.name.text = bag.name
        bagOpen.bagID = btn.bagID

        bagOpen.open()
    else:
        bagOpen.close()


def OnBagDeleteSelected(btn):
    '''Open bagDelete menu.'''
    if not bagDelete.is_open:
        bagDelete.open()
    else:
        bagDelete.close()
