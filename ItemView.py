from SysFuncs import *
from BagItem import *
from LoadSaves import *
from AppInit import *

IV_ICON = SizeMap(172, 172, LISTITEM.sizePair)
IV_NAME = SizeMap(790, 75, LISTITEM.sizePair)
IV_MISC = SizeMap(790, 65, LISTITEM.sizePair)

IV_ICON_POS = (14 / scale, 14 / scale)
IV_NAME_POS = (218 / scale, 102 / scale)
IV_MISC_POS = (218 / scale, 15 / scale)

class ItemView(ButtonBehavior, RelativeLayout):
    def __init__(self, itemID, **kwargs):
        try:
            self.itemID = itemID

            self.view = RelativeLayout(size_hint = FILLS)

            self.dBG = Image(size_hint = FILLS, source = 'images/IMG_ITEMVIEWBG.png',
                allow_stretch = True, keep_ratio = False)
            self.dicon = Image(size_hint = IV_ICON.hSizePair, pos = IV_ICON_POS,
                source = 'images/none.png', allow_stretch = True, keep_ratio = False)
            self.dname = Label(size_hint = IV_NAME.hSizePair, pos = IV_NAME_POS,
                halign = 'left', valign = 'middle', text = 'Item Name',
                font_name = FONT_BASK, font_size = FONT_SIZE_A, color = [1,1,1,1],
                shorten = True, shorten_from = 'right')
            self.dmisc = BoxLayout(size_hint = IV_MISC.hSizePair, pos = IV_MISC_POS,
                orientation = 'horizontal')
            self.dqty = Label(size_hint = FILLS, text = 'Quantity: ',
                font_name = FONT_BASK, font_size = FONT_SIZE_B, color = [1,1,1,1])
            self.dweight = Label(size_hint = FILLS, text = 'Weight: ',
                font_name = FONT_BASK, font_size = FONT_SIZE_B, color = [1,1,1,1])
            self.dval = Label(size_hint = FILLS, text = 'Value: ', font_name = FONT_BASK,
                font_size = FONT_SIZE_B, color = [1,1,1,1])

            super(ItemView, self).__init__(size_hint = FILLS, **kwargs)

            self.dicon.source = ITEMS[self.itemID].icon
            self.dname.text = ITEMS[self.itemID].name

            self.dqty.text += str(ITEMS[self.itemID].qty)
            self.dweight.text += str(ITEMS[self.itemID].weight)
            self.dval.text += str(ITEMS[self.itemID].val)

            print("Creating ItemView for " + str(self.itemID) + ": " + str(ITEMS[self.itemID].qty) + ", " + str(ITEMS[self.itemID].weight) + ", " + str(ITEMS[self.itemID].val))

            self.dmisc.add_widget(self.dqty)
            self.dmisc.add_widget(self.dweight)
            self.dmisc.add_widget(self.dval)

            self.view.add_widget(self.dBG)
            self.view.add_widget(self.dicon)
            self.view.add_widget(self.dname)
            self.view.add_widget(self.dmisc)

            self.dname.text_size[0] = IV_NAME.hw * IV_NAME.parentW / scale

            self.add_widget(self.view)

            ITEMVIEWS[int(self.itemID)] = self

        except Exception as ex:
            print("ERROR || ItemView.__init__() failure: " + str(ex))

    def on_press(self):
        print('button named ' + str(self.itemID) + ' was pressed!')
