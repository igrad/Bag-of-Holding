from SysFuncs import *
from LoadSaves import *
from AppInit import *

def OpenItemOpts(btn):
    if itemOpts.is_open:
        itemOpts.close()
    else:
        itemOpts.lbl.text = ITEMS[str(btn.itemID)].name
        itemOpts.open()
