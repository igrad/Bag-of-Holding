from SysFuncs import *
from BagItem import *
from LoadSaves import *
from AppInit import *

IV_ICON = SizeMap(120, 120, LISTITEM.sizePair)
IV_NAME = SizeMap(895, 70, LISTITEM.sizePair)
IV_DESC = SizeMap(895, 50, LISTITEM.sizePair)

IV_ICON_POS = (5 / scale, 5 / scale)

class ItemView(Button):
    view = RelativeLayout(size_hint = FILLS)
    itemID = 0
    dicon = Image(size_hint = IV_ICON.hSizePair, source = 'images/none.png',
                  pos = IV_ICON_POS, allow_stretch = True, keep_ratio = False)
    dname = Label(text = 'Item Name', font_name = FONT_BASK, font_size = FONT_SIZE_A,
                  color = [0,0,0,1], size = IV_NAME.sizePair)

    def __init__(self, itemID, **kwargs):
        try:
            self.itemID = itemID

            super(ItemView, self).__init__(**kwargs)

            print("TROUBLESHOOTING || This Item's ID: " + str(self.itemID))
            print("TROUBLESHOOTING || List of available IDs: " + str(ITEMS.keys()))

            self.dicon.source = ITEMS[self.itemID].icon
            self.dname.text = ITEMS[self.itemID].name

            view.add_widget(self.dicon)
            view.add_widget(self.dname)

            self.add_widget(self.view)

            ITEMVIEWS.append(self)

        except Exception as ex:
            print(str(ex))
