from SysFuncs import *
from BagItem import *
from LoadSaves import *
from AppInit import *

IV_ICON = SizeMap(172, 172, LISTITEM.sizePair)
IV_NAME = SizeMap(790, 75, LISTITEM.sizePair)
IV_DESC = SizeMap(800, 65, LISTITEM.sizePair)

IV_ICON_POS = (14 / scale, 14 / scale)
IV_NAME_POS = (218 / scale, 102 / scale)

class ItemView(ButtonBehavior, RelativeLayout):
    view = RelativeLayout(size_hint = FILLS)
    itemID = 0

    dBG = Image(size_hint = FILLS, source = 'images/IMG_ITEMVIEWBG.png',
        allow_stretch = True, keep_ratio = False)
    dicon = Image(size_hint = IV_ICON.hSizePair, pos = IV_ICON_POS,
        source = 'images/none.png', allow_stretch = True, keep_ratio = False)
    dname = Label(size_hint = IV_NAME.hSizePair, pos = IV_NAME_POS, halign = 'left',
        valign = 'middle', text = 'Item Name', font_name = FONT_BASK,
        font_size = FONT_SIZE_A, color = [1,1,1,1], shorten = True,
        shorten_from = 'right')

    def __init__(self, itemID, **kwargs):
        try:
            self.itemID = itemID

            super(ItemView, self).__init__(size_hint = FILLS, **kwargs)

            print('INFO || ItemView.__init__() item text = ' + ITEMS[itemID].name)

            self.dicon.source = ITEMS[self.itemID].icon
            self.dname.text = ITEMS[self.itemID].name


            self.view.add_widget(self.dBG)
            self.view.add_widget(self.dicon)
            self.view.add_widget(self.dname)

            print('BINDING...\ntext_size = ' + str(self.dname.text_size) + '\nsize = ' + str(self.dname.size))

            self.dname.text_size[0] = IV_NAME.hw * IV_NAME.parentW / scale

            self.add_widget(self.view)

            ITEMVIEWS.append(self)

        except Exception as ex:
            print(str(ex))

    def on_press(self):
        print('button named ' + str(self.itemID) + ' was pressed!')
