from SysFuncs import *
from BagItem import *
from LoadSaves import *
from AppInit import *

class ItemView(ButtonBehavior, RelativeLayout):
    '''Button designed to contain the aesthetics of an item on main Contents area.'''
    def __init__(self, itemID, **kwargs):
        try:
            super(ItemView, self).__init__(size_hint = FILLS, **kwargs)

            ITEMVIEWS[int(self.itemID)] = self

        except Exception as ex:
            LogMsg("ERROR || ItemView.__init__() failure: " + str(ex))

    def on_press(self):
        LogMsg('button named ' + str(self.itemID) + ' was pressed!')


class CozyView(ItemView):
    def __init__(self, itemID, **kwargs):
        self.itemID = itemID
        self.view = RelativeLayout(size_hint = FILLS)

        self.IV_ICON = IV_COZY_ICON
        self.IV_NAME = IV_COZY_NAME
        self.IV_MISC = IV_COZY_MISC

        self.dBG = Image(size_hint = FILLS, source = 'images/IMG_ITEMVIEWBG.png',
            allow_stretch = True, keep_ratio = False)
        self.dicon = Image(size_hint = self.IV_ICON.hpair, pos = self.IV_ICON.pos,
            source = 'images/none.png', allow_stretch = True, keep_ratio = False)
        self.dname = Label(size_hint = self.IV_NAME.hpair, pos = self.IV_NAME.pos,
            halign = 'left', valign = 'middle', text = 'Item Name',
            font_name = FONT_BASK, font_size = FONT_SIZE_A, color = [1,1,1,1],
            shorten = True, shorten_from = 'right')
        self.dmisc = BoxLayout(size_hint = self.IV_MISC.hpair, pos = self.IV_MISC.pos,
            orientation = 'horizontal')
        self.dqty = Label(size_hint = FILLS, text = 'Quantity: ',
            font_name = FONT_BASK, font_size = FONT_SIZE_B, color = [1,1,1,1])
        self.dweight = Label(size_hint = FILLS, text = 'Weight: ',
            font_name = FONT_BASK, font_size = FONT_SIZE_B, color = [1,1,1,1])
        self.dval = Label(size_hint = FILLS, text = 'Value: ', font_name = FONT_BASK,
            font_size = FONT_SIZE_B, color = [1,1,1,1])

        self.dicon.source = ITEMS[self.itemID].icon
        self.dname.text = ITEMS[self.itemID].name

        self.dqty.text += str(ITEMS[self.itemID].qty)
        self.dweight.text += str(ITEMS[self.itemID].weight)
        self.dval.text += str(ITEMS[self.itemID].val)

        self.dname.text_size[0] = IV_NAME.hw * IV_NAME.parentW / YSCALE

        for widge in [self.dqty, self.dweight, self.dval]:
            self.dmisc.add_widget(widge)

        for widge in [self.dBG, self.dicon, self.dname, self.dmisc]:
            self.view.add_widget(widge)

        self.add_widget(self.view)

        super(CozyView, self).__init__(itemID = itemID, **kwargs)

class NormView(ItemView):
    def __init__(self, itemID, **kwargs):
        self.IV_ICON = IV_NORM_ICON
        self.IV_NAME = IV_NORM_NAME
        self.IV_MISC = IV_NORM_MISC

        super(NormView, self).__init__(itemID = itemID, **kwargs)

class CardView(ItemView):
    def __init__(self, itemID, **kwargs):
        self.IV_ICON = IV_CARD_ICON
        self.IV_NAME = IV_CARD_NAME
        self.IV_MISC = IV_CARD_MISC

        super(CardView, self).__init__(itemID = itemID, **kwargs)
