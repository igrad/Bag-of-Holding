from SysFuncs import *
from BagItem import *
from LoadSaves import *
from AppInit import *
from AnchorLabel import *

class CozyView(ButtonBehavior, RelativeLayout):
    def __init__(self, itemID, **kwargs):
        self.itemID = itemID
        self.view = RelativeLayout(size_hint = FILLS)

        self.IV_ICON = IV_COZY_ICON
        self.IV_NAME = IV_COZY_NAME
        self.IV_MISC = IV_COZY_MISC

        bg_var = self.itemID % 3
        bg = 'images/IMG_COZYVIEW_BG_1.png'

        if bg_var == 1:
            bg = 'images/IMG_COZYVIEW_BG_2.png'
        elif bg_var == 2:
            bg = 'images/IMG_COZYVIEW_BG_3.png'

        self.dBG = Image(size_hint = FILLS, source = bg, allow_stretch = True,
            keep_ratio = False)
        self.dicon = Image(size_hint = self.IV_ICON.hpair, pos = self.IV_ICON.pos,
            source = 'images/IMG_CLEAR.png', allow_stretch = True, keep_ratio = False)
        self.dname = Label(size_hint = self.IV_NAME.hpair, pos = self.IV_NAME.pos,
            halign = 'left', valign = 'middle', text = 'Item Name', color = BLACK,
            font_name = FONT_BASK, font_size = FONT_SIZE_A, shorten = True,
            shorten_from = 'right')
        self.dmisc = BoxLayout(size_hint = self.IV_MISC.hpair, pos = self.IV_MISC.pos,
            orientation = 'horizontal')
        self.dqty = Label(size_hint = FILLS, text = 'Quantity: ',
            font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK)
        self.dweight = Label(size_hint = FILLS, text = 'Weight: ',
            font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK)
        self.dval = Label(size_hint = FILLS, text = 'Value: ', font_name = FONT_BASK,
            font_size = FONT_SIZE_C, color = BLACK)

        self.dicon.source = ITEMS[self.itemID].icon
        self.dname.text = ITEMS[self.itemID].name

        self.dqty.text += str(ITEMS[self.itemID].qty)
        self.dweight.text += str(ITEMS[self.itemID].weight)
        self.dval.text += str(ITEMS[self.itemID].val)

        for widge in [self.dqty, self.dweight, self.dval]:
            self.dmisc.add_widget(widge)

        for widge in [self.dBG, self.dicon, self.dname, self.dmisc]:
            self.view.add_widget(widge)

        super(CozyView, self).__init__(size_hint = FILLS, **kwargs)

        self.add_widget(self.view)

        print('creating cozy item: ' + str(self.dname.text))

        ITEMVIEWS[int(self.itemID)] = self

class NormView(ButtonBehavior, RelativeLayout):
    def __init__(self, itemID, **kwargs):
        self.itemID = itemID
        self.view = RelativeLayout(size_hint = FILLS)

        self.IV_ICON = IV_NORM_ICON
        self.IV_NAME = IV_NORM_NAME
        self.IV_MISC = IV_NORM_MISC

        self.dBG = Image(size_hint = FILLS, source = 'images/IMG_BLACK.png',
            color = [0,0,0,0.45], allow_stretch = True, keep_ratio = False)
        self.dicon = Image(size_hint = self.IV_ICON.hpair, pos = self.IV_ICON.pos,
            source = str(ITEMS[self.itemID].icon), allow_stretch = True,
            keep_ratio = False)
        self.dname = AnchorLabel(size_hint = self.IV_NAME.hpair, pos = self.IV_NAME.pos,
            anchor_x = 'left', anchor_y = 'bottom', halign = 'left',
            text = str(ITEMS[self.itemID].name), color = WHITE, font_name = FONT_BASK,
            font_size = FONT_SIZE_C, shorten = True, shorten_from = 'right')
        self.dmisc = BoxLayout(size_hint = self.IV_MISC.hpair, pos = self.IV_MISC.pos,
            orientation = 'horizontal')
        self.dqty = AnchorLabel(size_hint = FILLS, anchor_x = 'right',
            anchor_y = 'bottom', halign = 'right', text = str(ITEMS[self.itemID].qty),
            font_name = FONT_BASK, font_size = FONT_SIZE_C, color = WHITE)
        self.dweight = AnchorLabel(size_hint = FILLS, anchor_x = 'right',
            anchor_y = 'bottom', halign = 'right', text = str(ITEMS[self.itemID].weight),
            font_name = FONT_BASK, font_size = FONT_SIZE_C, color = WHITE)
        self.dval = AnchorLabel(size_hint = FILLS, anchor_x = 'right',
            anchor_y = 'bottom', halign = 'right', text = str(ITEMS[self.itemID].val),
            font_name = FONT_BASK,font_size = FONT_SIZE_C, color = WHITE)

        #self.dicon.source = ITEMS[self.itemID].icon
        self.dname.text = ITEMS[self.itemID].name

        #self.dqty.text = str(ITEMS[self.itemID].qty)
        #self.dweight.text += str(ITEMS[self.itemID].weight)
        #self.dval.text += str(ITEMS[self.itemID].val)

        for widge in [self.dqty, self.dweight, self.dval]:
            self.dmisc.add_widget(widge)

        for widge in [self.dBG, self.dicon, self.dname, self.dmisc]:
            self.view.add_widget(widge)

        super(NormView, self).__init__(size_hint = FILLS, **kwargs)

        self.add_widget(self.view)

        print('creating norm item: ' + str(self.dname.text))

        ITEMVIEWS[int(self.itemID)] = self

class CardView():
    def __init__(self, itemID, **kwargs):
        self.IV_ICON = IV_CARD_ICON
        self.IV_NAME = IV_CARD_NAME
        self.IV_MISC = IV_CARD_MISC

        #super(CardView, self).__init__(itemID = itemID, **kwargs)

        # On hold until project is more complete
