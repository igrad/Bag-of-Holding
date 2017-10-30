from SysFuncs import *
from AppInit import *
from Bag import *
from Currency import *
from AnchorLabel import *

def PreviewBagMenu(btn):
    '''Open or close the bagOpts menu.'''
    if not bagOpts.is_open:
        bag = BAGS[btn.bagID]
        bagOpts.name.text = bag.name
        bagOpts.bagID = btn.bagID

        Opens.open(bagOpts)
    else:
        Opens.close(bagOpts)


def OnBagDeleteSelected(btn):
    '''Open bagDelete menu.'''
    if not bagDelete.is_open:
        Opens.open(bagDelete)
    else:
        Opens.close(bagDelete)
