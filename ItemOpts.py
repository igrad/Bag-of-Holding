from SysFuncs import *
from LoadSaves import *
from AppInit import *

def OpenItemOpts(btn, itemID = None):
    if itemOpts.is_open:
        Opens.close(itemOpts)
    else:
        ID = itemID

        if btn != None:
            ID = btn.itemID
            itemOpts.move.itemID = ID

        itemOpts.lbl.text = ITEMS[str(ID)].name
        Opens.open(itemOpts)


def OpenItemMove(btn):
    if itemMove.is_open:
        Opens.close(itemMove)
        OpenItemOpts(None, itemMove.returnToOpts)
    else:
        Opens.close(itemOpts)
        itemMove.returnToOpts = btn.itemID



        Opens.open(itemMove)
