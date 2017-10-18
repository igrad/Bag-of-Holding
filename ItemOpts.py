from SysFuncs import *
from LoadSaves import *
from AppInit import *

def OpenItemOpts(btn, itemID = None):
    if itemOpts.is_open:
        itemOpts.close()
    else:
        ID = itemID

        if btn != None:
            ID = btn.itemID
            itemOpts.move.itemID = ID

        itemOpts.lbl.text = ITEMS[str(ID)].name
        itemOpts.open()


def OpenItemMove(btn):
    if itemMove.is_open:
        itemMove.close()
        OpenItemOpts(None, itemMove.returnToOpts)
    else:
        itemOpts.close()
        itemMove.returnToOpts = btn.itemID
        itemMove.open()
