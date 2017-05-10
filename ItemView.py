from SysFuncs import *
from BagItem import *
from LoadSaves import *
from AppInit import *
from AnchorLabel import *

def NoOnPressFunc():
    pass

def SetItemViewsOnPress(func):
    if func == None:
        func = NoOnPressFunc
    CozyView.on_press = func
    NormView.on_press = func
    CardView.on_press = func

class CozyView(ButtonBehavior, RelativeLayout):
    def __init__(self, itemID, **kwargs):
        self.itemID = str(itemID)
        self.size_hint = FILLS

        super(CozyView, self).__init__(size_hint = FILLS, **kwargs)

        self.IV_ICON = IV_COZY_ICON
        self.IV_NAME = IV_COZY_NAME
        self.IV_MISC = IV_COZY_MISC

        bg_var = int(self.itemID) % 3
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

        print('item keys: ' + str(ITEMS.keys()))

        self.dicon.source = ITEMS[self.itemID].icon
        self.dname.text = ITEMS[self.itemID].name

        self.dqty.text += str(ITEMS[self.itemID].qty)
        self.dweight.text += str(ITEMS[self.itemID].weight)
        self.dval.text += str(ITEMS[self.itemID].val)

        for widge in [self.dqty, self.dweight, self.dval]:
            self.dmisc.add_widget(widge)

        for widge in [self.dBG, self.dicon, self.dname, self.dmisc]:
            self.add_widget(widge)

        ITEMVIEWS[self.itemID] = self


    def UpdateItemView(self, **kwargs):
        try:
            if 'name' in kwargs: self.dname.text = str(kwargs['name'])
            if 'qty' in kwargs: self.dqty.text = 'Quantity: ' + str(kwargs['qty'])
            if 'weight' in kwargs: self.dweight.text = 'Weight: ' + str(kwargs['weight'])
            if 'val' in kwargs: self.dval.text = 'Value: ' + str(kwargs['val'])
            if 'icon' in kwargs: self.dicon.source = str(kwargs['icon'])

        except Exception as ex:
            LogExc('CozyView.UpdateItemView()')



class NormView(ButtonBehavior, RelativeLayout):
    def __init__(self, itemID, **kwargs):
        self.itemID = str(itemID)
        self.size_hint = FILLS

        super(NormView, self).__init__(size_hint = FILLS, **kwargs)

        self.IV_ICON = IV_NORM_ICON
        self.IV_NAME = IV_NORM_NAME
        self.IV_MISC = IV_NORM_MISC

        self.dBG = Image(size_hint = FILLS, source = 'images/IMG_BLACK.png',
            color = [0,0,0,0.45], allow_stretch = True, keep_ratio = False)
        self.dicon = Image(size_hint = self.IV_ICON.hpair, pos = self.IV_ICON.pos,
            source = '', allow_stretch = True, keep_ratio = False)
        self.dname = AnchorLabel(size_hint = self.IV_NAME.hpair, pos = self.IV_NAME.pos,
            anchor_x = 'left', anchor_y = 'bottom', halign = 'left', text = '',
            color = WHITE, font_name = FONT_BASK, font_size = FONT_SIZE_C,
            shorten = True, shorten_from = 'right')
        self.dmisc = BoxLayout(size_hint = self.IV_MISC.hpair, pos = self.IV_MISC.pos,
            orientation = 'horizontal')
        self.dqty = AnchorLabel(size_hint = FILLS, anchor_x = 'right',
            anchor_y = 'bottom', halign = 'right', text = '', font_name = FONT_BASK,
            font_size = FONT_SIZE_C, color = WHITE)
        self.dweight = AnchorLabel(size_hint = FILLS, anchor_x = 'right',
            anchor_y = 'bottom', halign = 'right', text = '', font_name = FONT_BASK,
            font_size = FONT_SIZE_C, color = WHITE)
        self.dval = AnchorLabel(size_hint = FILLS, anchor_x = 'right',
            anchor_y = 'bottom', halign = 'right', text = '',
            font_name = FONT_BASK,font_size = FONT_SIZE_C, color = WHITE)

        self.dicon.source = ITEMS[self.itemID].icon
        self.dname.text = ITEMS[self.itemID].name

        self.dqty.text = str(ITEMS[self.itemID].qty)
        self.dweight.text += str(ITEMS[self.itemID].weight)
        self.dval.text += str(ITEMS[self.itemID].val)

        for widge in [self.dqty, self.dweight, self.dval]:
            self.dmisc.add_widget(widge)

        for widge in [self.dBG, self.dicon, self.dname, self.dmisc]:
            self.add_widget(widge)

        ITEMVIEWS[self.itemID] = self

    def UpdateItemView(self, **kwargs):
        try:
            if 'name' in kwargs: self.dname.text = str(kwargs['name'])
            if 'qty' in kwargs: self.dqty.text = str(kwargs['qty'])
            if 'weight' in kwargs: self.dweight.text = str(kwargs['weight'])
            if 'val' in kwargs: self.dval.text = str(kwargs['val'])
            if 'icon' in kwargs: self.dicon.source = str(kwargs['icon'])

        except Exception as ex:
            LogExc('NormView.UpdateItemView()')

class CardView(ButtonBehavior, RelativeLayout):
    def __init__(self, itemID, **kwargs):
        self.IV_ICON = IV_CARD_ICON
        self.IV_NAME = IV_CARD_NAME
        self.IV_MISC = IV_CARD_MISC

        self.itemID = str(itemID)
        self.size_hint = FILLS

        super(CardView, self).__init__(size_hint = FILLS, **kwargs)

        bg_var = int(self.itemID) % 3
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
            self.add_widget(widge)

        ITEMVIEWS[self.itemID] = self

    def UpdateItemView(self, **kwargs):
        try:
            if 'name' in kwargs: self.dname.text = str(kwargs['name'])
            if 'qty' in kwargs: self.dqty.text = str(kwargs['qty'])
            if 'weight' in kwargs: self.dweight.text = str(kwargs['weight'])
            if 'val' in kwargs: self.dval.text = str(kwargs['val'])
            if 'desc' in kwargs: self.ddesc.text = str(kwargs['desc'])
            if 'icon' in kwargs: self.dicon.source = str(kwargs['icon'])
            if 'tags' in kwargs: self.dtags.text = str(kwargs['tags'])

        except Exception as ex:
            LogExc('CardView.UpdateItemView()')
