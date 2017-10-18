from SysFuncs import *
from AppInit import *
from Bag import *
from Currency import *
from AnchorLabel import *
from BagOpts import PreviewBagMenu


def LoadBagPickGridData():
    pass

def OpenBagPickMenu(obj):
    '''Open up the bagPick menu on-screen.'''
    if bagPick.is_open:
        bagPick.close()

    else:
        bagPick.grid.clear_widgets()

        # Create a list of all of the bagIDs where the bags are sorted alphabetically
        # by name.
        bagIDs = [y.ID for y in sorted([BAGS[str(bagID)] for bagID in BAGS.keys()],
        key = lambda x: x.name, reverse = True)]

        for bagID in bagIDs:
            bpi = BagPickItem(bagID)
            bpi.bagID = bagID
            bpi.bind(on_press = PreviewBagMenu)
            bagPick.grid.add_widget(bpi)

        bagPick.open()


class BagPickItem(ButtonBehavior, RelativeLayout):
    def __init__(self, bagID, **kwargs):
        NAME = bagPick.ITEM_NAME
        MISC = bagPick.ITEM_MISC
        BPI = bagPick.ITEM

        self.bagID = str(bagID)
        self.size_hint = FILLS

        super(BagPickItem, self).__init__(size_hint = FILLS, **kwargs)

        bg_var = int(self.bagID) % 3
        bg = 'images/IMG_PICK_ITEM_1.png'

        if bg_var == 1:
            bg = 'images/IMG_PICK_ITEM_2.png'
        elif bg_var == 2:
            bg = 'images/IMG_PICK_ITEM_3.png'

        self.BG = Image(size_hint = FILLS, source = bg, allow_stretch = True,
            keep_ratio = False)
        self.name = Label(size_hint = NAME.hpair, pos = NAME.pos,
            halign = 'left', valign = 'middle', text = 'Item Name', color = BLACK,
            font_name = FONT_BASK, font_size = FONT_SIZE_A, shorten = True,
            shorten_from = 'right')
        self.misc = BoxLayout(size_hint = MISC.hpair, pos = MISC.pos,
            orientation = 'horizontal')
        self.tot_items = Label(size_hint = FILLS, text = 'Items: ',
            font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK)
        self.tot_weight = Label(size_hint = FILLS, text = 'Weight: ',
            font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK)
        self.tot_val = Label(size_hint = FILLS, text = 'Value: ', font_name = FONT_BASK,
            font_size = FONT_SIZE_C, color = BLACK)

        self.name.text = BAGS[self.bagID].name

        self.UpdateTotals()

        for widge in [self.tot_items, self.tot_weight, self.tot_val]:
            self.misc.add_widget(widge)

        for widge in [self.BG, self.name, self.misc]:
            self.add_widget(widge)


    def UpdateTotals(self):
        BAGS[self.bagID].SetTotals()
        self.tot_items.text += str(BAGS[self.bagID].tot_items)
        self.tot_weight.text += str(BAGS[self.bagID].tot_weight)
        self.tot_val.text += str(BAGS[self.bagID].tot_val)
