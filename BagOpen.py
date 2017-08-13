from SysFuncs import *
from AppInit import *
from Bag import *
from Currency import *
from AnchorLabel import *

def PreviewBagMenu(obj):
    if not bagOpen.is_open:
        bag = BAGS[obj.bagID]
        bagOpen.name.text = bag.name
        bagOpen.bagID = obj.bagID

        bagOpen.open()
    else:
        bagOpen.close()


def OnBagDeleteSelected(obj):
    if not bagDelete.is_open:
        bagDelete.open()
    else:
        bagDelete.close()
