from SysFuncs import *
from AppInit import *
from Bag import *
from Currency import *
from AnchorLabel import *


def LoadBagPickGridData():
    pass

def OpenBagPickMenu(obj):
    '''Open up the bagPick menu on-screen.'''
    if bagPick.is_open:
        bagPick.pos = screenPos.OFF
        bagPick.is_open = False

    else:
        bagPick.pos = size.BAGPICK.pos
        bagPick.is_open = True


class BagPickItem(ButtonBehavior, RelativeLayout):
    def __init__(self, itemID, **kwargs):
        NAME = BPI_NAME
        MISC = BPI_MISC
        ITEM = BPI_ITEM

        self.bagID = str(bagID)
        self.size_hint = FILLS

        super(BagPickItem, self).__init__(size_hint = FILLS, **kwargs)

        bg_var = int(self.bagID) % 3
        bg = 'images/IMG_COZYVIEW_BG_1.png'

        if bg_var == 1:
            bg = 'images/IMG_COZYVIEW_BG_2.png'
        elif bg_var == 2:
            bg = 'images/IMG_COZYVIEW_BG_3.png'

        self.dBG = Image(size_hint = FILLS, source = bg, allow_stretch = True,
            keep_ratio = False)
        self.dicon = Image(size_hint = IV_ICON.hpair, pos = IV_ICON.pos,
            source = 'images/IMG_CLEAR.png', allow_stretch = True, keep_ratio = False)
        self.dname = Label(size_hint = IV_NAME.hpair, pos = IV_NAME.pos,
            halign = 'left', valign = 'middle', text = 'Item Name', color = BLACK,
            font_name = FONT_BASK, font_size = FONT_SIZE_A, shorten = True,
            shorten_from = 'right')
        self.dmisc = BoxLayout(size_hint = IV_MISC.hpair, pos = IV_MISC.pos,
            orientation = 'horizontal')
        self.dqty = Label(size_hint = FILLS, text = 'Quantity: ', font_name = FONT_BASK,
            font_size = FONT_SIZE_C, color = BLACK)
        self.dweight = Label(size_hint = FILLS, text = 'Weight: ', font_name = FONT_BASK,
            font_size = FONT_SIZE_C, color = BLACK)
        self.dval = Label(size_hint = FILLS, text = 'Value: ', font_name = FONT_BASK,
            font_size = FONT_SIZE_C, color = BLACK)
        self.ddescwrap = StencilLayout(size_hint = IV_DESC.hpair, pos = IV_DESC.pos)
        self.ddesc = TextInput(size_hint = (0.99, None), disabled = True,
            pos_hint = {'x': 0.01, 'top': 1}, font_name = FONT_BASK,
            font_size = FONT_SIZE_C, background_color = CLEAR, foreground_color = BLACK,
            disabled_foreground_color = BLACK)

        self.dicon.source = ITEMS[self.itemID].icon
        self.dname.text = ITEMS[self.itemID].name

        self.ddescwrap.add_widget(self.ddesc)

        self.dqty.text += str(ITEMS[self.itemID].qty)
        self.dweight.text += str(ITEMS[self.itemID].weight)
        self.dval.text += str(ITEMS[self.itemID].val)
        self.ddesc.text = str(ITEMS[self.itemID].desc)

        for widge in [self.dqty, self.dweight, self.dval]:
            self.dmisc.add_widget(widge)

        for widge in [self.dBG, self.dicon, self.dname, self.dmisc, self.ddescwrap]:
            self.add_widget(widge)
