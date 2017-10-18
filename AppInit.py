from SysFuncs import *
from LoadSaves import *
from Bag import *
from BagItem import *
from AnchorLabel import *

FONT_BASK = 'fonts/BASKVILLE.TTF'
WHITE = [1,1,1,1]
BLACK = [0,0,0,1]
CLEAR = [0,0,0,0]

VIEW_CHECK_ACTIVE = 'images/IMG_VIEW_CHECK_ACTIVE.png'
VIEW_CHECK_INACTIVE = 'images/IMG_VIEW_CHECK_INACTIVE.png'
IMG_BLACK = 'images/IMG_BLACK.png'
IMG_WHITE = 'images/IMG_WHITE.png'



class HasBase():
    def __init__(self, **kwargs):
        super(HasBase, self).__init__()
        self.base = False

    # POS
    @property
    def pos(self):
        if self.base: return self.base.pos

    @pos.setter
    def pos(self, new_val):
        if self.base: self.base.pos = new_val

    # SIZE_HINT
    @property
    def size_hint(self):
        if self.size_hint: return self.base.size_hint

    @size_hint.setter
    def size_hint(self, new_val):
        if self.size_hint: self.base.size_hint = new_val



class Opens():
    def open(self, index = 0):
        self.is_open = True
        self.container.add_widget(self.base, index)

    def close(self):
        self.is_open = False
        self.container.remove_widget(self.base)



class Size():
    def __init__(self, **kwargs):
        # Stylization ====================================================================
        self.MAX = max(scale.X, scale.Y)
        self.FONT_SIZE_A = 32/self.MAX
        self.FONT_SIZE_B = 20/self.MAX
        self.FONT_SIZE_C = 16/self.MAX
        self.FONT_SIZE_D = 24/self.MAX
        self.FONT_SIZE_HEAD = 48/self.MAX

        # Sizes ==========================================================================
        self.APP_W = 432/scale.X
        self.APP_H = 768/scale.Y
        self.Frame = SizeMap(0, 0, 432, 768, (self.APP_W, self.APP_H))



class Base():
    def __init__(self, Size, **kwargs):
        # FRAME
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_MAIN.png',
            allow_stretch = True, keep_ratio = False)

        # SCREENS
        self.screenMain = RelativeLayout()
        self.screenSettings = RelativeLayout()



class Halt(Button):
    def __init__(self, **kwargs):
        self.pos = ZEROS
        self.size_hint = size.Frame.pair
        self.disabled = False
        self.opacity = 0.5
        self.background_normal = self.background_down = IMG_BLACK
        self.background_disabled_normal = IMG_BLACK

        if 'pos' in kwargs: self.pos = kwargs.pop('pos')
        if 'size_hint' in kwargs: self.size_hint = kwargs.pop('size_hint')
        if 'disabled' in kwargs: self.disabled = kwargs.pop('disabled')
        if 'opacity' in kwargs: self.opacity = kwargs.pop('opacity')

        super(Halt, self).__init__(**kwargs)



class Menu(HasBase):
    def __init__(self, Size, **kwargs):
        self.MENU = SizeMap(0, 670, 432, 98, Size.Frame.pair)
        self.BTN_BAG = SizeMap(18, 18, 72, 72, self.MENU.pair)
        self.BTN_OPTS = SizeMap(342, 18, 72, 72, self.MENU.pair)
        self.TITLE = SizeMap(153, 34, 128, 40, self.MENU.pair)

        self.base = RelativeLayout(pos = self.MENU.pos, size_hint = self.MENU.hpair)
        self.title = Label(size_hint = self.TITLE.hpair, pos = self.TITLE.pos,
            font_name = FONT_BASK, font_size = Size.FONT_SIZE_A, color = WHITE)
        self.bag = Image(size_hint = self.BTN_BAG.hpair,
            pos = self.BTN_BAG.pos,
            source = 'images/IMG_BAGS.png', keep_ratio = False, allow_stretch = True)
        self.bagBtn = Button(size_hint = self.BTN_BAG.hpair,
            pos = self.BTN_BAG.pos, background_color = CLEAR)
        self.opts = Image(size_hint = self.BTN_OPTS.hpair,
            pos = self.BTN_OPTS.pos, source = 'images/IMG_SETTINGS.png',
            keep_ratio = False, allow_stretch = True)
        self.optsBtn = Button(size_hint = self.BTN_OPTS.hpair,
            pos = self.BTN_OPTS.pos, background_color = CLEAR)



class Tabs(HasBase):
    def __init__(self, Size, **kwargs):
        self.TABS = SizeMap(0, 602, 432, 60, Size.Frame.pair)
        self.BTN = SizeMap(0, 0, 144, 60, self.TABS.pair)

        self.base = BoxLayout(size_hint = self.TABS.hpair, pos = self.TABS.pos,
            orientation = 'horizontal')
        self.new = Button(size_hint = self.BTN.hpair, text = 'NEW', color = WHITE,
            font_name = FONT_BASK, font_size = Size.FONT_SIZE_A,
            background_color = CLEAR)
        self.sort = Button(size_hint = self.BTN.hpair, text = 'SORT',
            color = WHITE, font_name = FONT_BASK, font_size = Size.FONT_SIZE_A,
            background_color = CLEAR)
        self.view = Button(size_hint = self.BTN.hpair, text = 'VIEW',
            color = WHITE, font_name = FONT_BASK, font_size = Size.FONT_SIZE_A,
            background_color = CLEAR)



class Search(HasBase):
    def __init__(self, Size, **kwargs):
        self.SEARCH = SizeMap(11, 563, 326, 34, Size.Frame.pair)
        self.INPUT = SizeMap(34, 0, 284, 34, self.SEARCH.pair)

        self.base = RelativeLayout(size_hint = self.SEARCH.hpair, pos = self.SEARCH.pos)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_SEARCH.png',
            allow_stretch = True, keep_ratio = False)
        self.input = TextInput(size_hint = self.INPUT.hpair,
            pos = self.INPUT.pos, hint_text = 'Search for an item...',
            font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            foreground_color = BLACK, write_tab = False, multiline = False,
            cursor_color = BLACK, background_normal = '', background_active = '',
            background_color = CLEAR)



class Cont(HasBase):
    def __init__(self, Size, **kwargs):
        self.CONT = SizeMap(0, 0, 432, 557, Size.Frame.pair)
        self.SPACE = SizeMap(0, 0, 0, 5, self.CONT.pair)
        self.PAD = SizeMap(0, 0, 2, 2, self.CONT.pair)
        self.SCROLL = SizeMap(0, 0, 12, 0, self.CONT.pair)

        self.ITEMVIEW_COZY = SizeMap(0, 0, 408, 84, self.CONT.pair)
        self.ITEMVIEW_NORM = SizeMap(0, 0, 408, 24, self.CONT.pair)
        self.ITEMVIEW_CARD = SizeMap(0, 0, 408, 156, self.CONT.pair)
        self.IV_COZY_ICON = SizeMap(8, 8, 68, 68, self.ITEMVIEW_COZY.pair)
        self.IV_COZY_NAME = SizeMap(84, 40, 316, 30, self.ITEMVIEW_COZY.pair)
        self.IV_COZY_MISC = SizeMap(84, 10, 316, 24, self.ITEMVIEW_COZY.pair)
        self.IV_NORM_ICON = SizeMap(4, 4, 16, 16, self.ITEMVIEW_NORM.pair)
        self.IV_NORM_NAME = SizeMap(24, -2, 204, 24, self.ITEMVIEW_NORM.pair)
        self.IV_NORM_MISC = SizeMap(232, 2, 184, 24, self.ITEMVIEW_NORM.pair)
        self.IV_CARD_ICON = SizeMap(8, 80, 68, 68, self.ITEMVIEW_CARD.pair)
        self.IV_CARD_NAME = SizeMap(84, 112, 316, 30, self.ITEMVIEW_CARD.pair)
        self.IV_CARD_MISC = SizeMap(84, 82, 316, 24, self.ITEMVIEW_CARD.pair)
        self.IV_CARD_DESC = SizeMap(8, 8, 392, 64, self.ITEMVIEW_CARD.pair)

        self.base = RelativeLayout(size_hint = self.CONT.hpair, pos = self.CONT.pos)
        self.scroll = ScrollView(size_hint = FILLS, do_scroll_x = False,
            bar_width = self.SCROLL.x)
        self.list = GridLayout(size_hint = (1.0, None), cols = 1,
            padding = list(self.PAD.pair), spacing = list(self.SPACE.pair),
            row_force_default = True)



class BagPick(Opens, HasBase):
    def __init__(self, Size, **kwargs):
        # BAGPICK MENU
        self.BAGPICK = SizeMap(0, 0, 380, 768, Size.Frame.pair)
        self.HALT = SizeMap(0, 0, 368, 768, self.BAGPICK.pair)
        self.BACK = SizeMap(360, 0, 72, 768, self.BAGPICK.pair)
        self.NAME = SizeMap(8, 698, 344, 56, self.BAGPICK.pair)
        self.SCROLL = SizeMap(8, 60, 344, 636, self.BAGPICK.pair)
        self.ITEM = SizeMap(0, 0, 344, 64, self.SCROLL.pair)
        self.ITEM_NAME = SizeMap(0, 24, 344, 40, self.ITEM.pair)
        self.ITEM_MISC = SizeMap(0, 4, 344, 20, self.ITEM.pair)
        self.NEW = SizeMap(8, 20, 344, 32, self.BAGPICK.pair)

        self.container = base.screenMain
        self.is_open = False

        self.base = RelativeLayout(size_hint = self.BAGPICK.hpair, pos = self.BAGPICK.pos)
        self.back = Button(pos = self.BACK.pos,
            size_hint = self.BACK.hpair, background_normal = IMG_BLACK,
            background_down = IMG_BLACK, opacity = 0.5)
        self.halt = Halt(size_hint = self.HALT.hpair, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_BAG_PICK_BG.png',
            allow_stretch = True, keep_ratio = False)
        self.name = Label(size_hint = self.NAME.hpair,
            pos = self.NAME.pos, text = 'Bags', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_A)
        self.scroll = ScrollView(size_hint = self.SCROLL.hpair,
            pos = self.SCROLL.pos, do_scroll_x = False, bar_width = 0)
        self.grid = GridLayout(size_hint = (1.0, None), cols = 1,
            row_default_height = self.ITEM.h, row_force_default = True)
        self.newBag = AnchorButton(size_hint = self.NEW.hpair,
            pos = self.NEW.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, text = 'New Bag')



class BagOpts(Opens, HasBase):
    def __init__(self, Size,**kwargs):
        # BAGOPTS MENU
        self.BAGOPTS = SizeMap(32, 272, 368, 232, Size.Frame.pair)
        self.HALT = SizeMap(-36, -276, 432, 768, self.BAGOPTS.pair)
        self.BACK = SizeMap(0, 0, 368, 232, self.BAGOPTS.pair)
        self.NAME = SizeMap(12, 180, 344, 32, self.BAGOPTS.pair)
        self.BTNS = SizeMap(12, 12, 344, 160, self.BAGOPTS.pair)
        self.BTN = SizeMap(0, 0, 344, 40, self.BTNS.pair)

        self.container = base.screenMain
        self.is_open = False

        self.base = RelativeLayout(size_hint = self.BAGOPTS.hpair, pos = self.BAGOPTS.pos)
        self.halt = Halt(pos = self.HALT.pos)
        self.back = Button(pos = self.BACK.pos, size_hint = self.BACK.hpair, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_PROMPT_SMALL.png',
            allow_stretch = True, keep_ratio = False)
        self.name = Label(size_hint = self.NAME.hpair,
            pos = self.NAME.pos, text = 'Bag Name', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_A)
        self.btns = BoxLayout(size_hint = self.BTNS.hpair,
            pos = self.BTNS.pos, orientation = 'vertical')
        self.weight = AnchorButton(size_hint = self.BTN.hpair,
            text = 'Set weight system', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_1.png')
        self.currency = AnchorButton(size_hint = self.BTN.hpair,
            text = 'Set currency system', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_2.png')
        self.delete = AnchorButton(size_hint = self.BTN.hpair,
            text = 'Delete bag', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_3.png')
        self.done = AnchorButton(size_hint = self.BTN.hpair,
            text = 'Done', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_4.png')



class BagDelete(Opens, HasBase):
    def __init__(self, Size, **kwargs):
        # BAGDELETE MENU
        self.BAGDELETE = SizeMap(32, 272, 368, 232, Size.Frame.pair)
        self.HALT = SizeMap(-32, -272, 432, 768, self.BAGDELETE.pair)
        self.BACK = SizeMap(0, 0, 368, 232, self.BAGDELETE.pair)
        self.BG = SizeMap(0, 0, 368, 232, self.BAGDELETE.pair)
        self.LBL = SizeMap(12, 180, 344, 32, self.BAGDELETE.pair)
        self.CANCEL = SizeMap(12, 12, 168, 40, self.BAGDELETE.pair)
        self.CONFIRM = SizeMap(188, 12, 168, 40, self.BAGDELETE.pair)

        self.container = base.screenMain
        self.is_open = False

        self.base = RelativeLayout(size_hint = self.BAGDELETE.hpair,
            pos = self.BAGDELETE.pos)
        self.halt = Halt(pos = self.HALT.pos)
        self.back = Button(pos = self.BACK.pos, size_hint = self.BACK.hpair, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_PROMPT_SMALL.png',
            allow_stretch = True, keep_ratio = False)
        self.lbl = Label(size_hint = self.LBL.hpair, pos = self.LBL.pos)



class Pick(Opens, HasBase):
    def __init__(self, Size, **kwargs):
        # Note: spacing should be (20, 20, 392, 516)
        self.PICK = SizeMap(0, 105, 432, 557, Size.Frame.pair)
        self.HALT = SizeMap(0, -105, 432, 768, self.PICK.pair)
        self.NAME = SizeMap(20, 476, 392, 40, self.PICK.pair)
        self.ICON = SizeMap(138, 316, 156, 156, self.PICK.pair)
        self.MISC = SizeMap(21, 287, 390, 27, self.PICK.pair)
        self.QTY = SizeMap(0, 0, 130, 27, self.PICK.pair)
        self.WEIGHT = SizeMap(0, 1, 390, 27, self.MISC.pair)
        self.VAL = SizeMap(0, 0, 130, 27, self.PICK.pair)
        self.TAGS = SizeMap(20, 256, 392, 27, self.PICK.pair)
        self.DESC = SizeMap(20, 20, 392, 232, self.PICK.pair)
        self.OPTS = SizeMap(8, 550, 26, 26, self.PICK.pair)
        self.X = SizeMap(396, 550, 26, 26, self.PICK.pair)

        self.container = base.screenMain
        self.is_open = False

        self.base = RelativeLayout(size_hint = self.PICK.hpair, pos = self.PICK.pos)
        self.halt = Halt(pos = self.HALT.pos, disabled = True)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_PICK.png',
            allow_stretch = True, keep_ratio = False)
        self.widges = RelativeLayout(size_hint = FILLS, pos = ZEROS)
        self.name = TextInput(size_hint = self.NAME.hpair,
            pos = self.NAME.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_A, foreground_color = BLACK,
            border = [2,2,2,2], write_tab = False, multiline = False,
            cursor_color = BLACK, background_normal = 'images/IMG_1x1BORDER.png',
            hint_text = 'Item Name', background_active = 'images/IMG_1x1BORDER.png')
        self.icon = Button(size_hint = self.ICON.hpair, pos = self.ICON.pos,
            background_normal = 'images/blankIcon.png',
            background_down = 'images/blankIcon.png', border = [0,0,0,0])
        self.misc = BoxLayout(size_hint = self.MISC.hpair,
            pos = self.MISC.pos, orientation = 'horizontal')
        self.qty_L = AnchorLabel(pos = self.QTY.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, color = BLACK, text = 'Quantity: ',
            anchor_x = 'right', halign = 'right', valign = 'bottom')
        self.qty_I = TextInput(font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            foreground_color = BLACK, background_normal = 'images/IMG_1x1BORDER.png',
            background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
            write_tab = False, multiline = False, cursor_color = BLACK)
        self.weight_L = AnchorLabel(font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, text = 'Weight: ', anchor_x = 'right', halign = 'right',
            valign = 'bottom')
        self.weight_I = TextInput(font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            foreground_color = BLACK, background_normal = 'images/IMG_1x1BORDER.png',
            background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
            write_tab = False, multiline = False, cursor_color = BLACK)
        self.val_L = AnchorLabel(font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, text = 'Value: ', anchor_x = 'right', halign = 'right',
            valign = 'bottom')
        self.val_I = TextInput(font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            foreground_color = BLACK, background_normal = 'images/IMG_1x1BORDER.png',
            background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
            write_tab = False, multiline = False, cursor_color = BLACK)
        self.tags = TextInput(size_hint = self.TAGS.hpair,
            pos = self.TAGS.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, foreground_color = BLACK,
            background_normal = 'images/IMG_1x1BORDER.png',
            background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
            cursor_color = BLACK)
        self.desc = TextInput(size_hint = self.DESC.hpair,
            pos = self.DESC.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, foreground_color = BLACK,
            background_normal = 'images/IMG_1x1BORDER.png',
            background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
            cursor_color = BLACK)
        self.opts = AnchorButton(size_hint = self.OPTS.hpair,
            pos = self.OPTS.pos, source = 'images/IMG_SETTINGS.png',
            keep_ratio = True, allow_stretch = False, background_img = None)
        self.X = AnchorButton(size_hint = self.X.hpair, pos = self.X.pos,
            text = 'X', font_name = FONT_BASK, font_size = Size.FONT_SIZE_D,
            color = WHITE, background_img = None, valign = 'bottom')



class ItemOpts(Opens, HasBase):
    def __init__(self, Size, **kwargs):
        self.ITEMOPTS = SizeMap(32, 272, 368, 232, Size.Frame.pair)
        self.HALT = SizeMap(-32, -272, 432, 768, self.ITEMOPTS.pair)
        self.BACK = SizeMap(0, 0, 368, 232, self.ITEMOPTS.pair)
        self.BG = SizeMap(0, 0, 368, 232, self.ITEMOPTS.pair)
        self.LBL = SizeMap(12, 160, 344, 32, self.ITEMOPTS.pair)
        self.BTNS = SizeMap(12, 12, 344, 120, self.ITEMOPTS.pair)
        self.BTN = SizeMap(0, 0, 344, 40, self.BTNS.pair)

        self.container = base.screenMain
        self.is_open = False

        self.base = RelativeLayout(size_hint = self.ITEMOPTS.hpair,
            pos = self.ITEMOPTS.pos)
        self.halt = Halt(pos = self.HALT.pos)
        self.back = Button(pos = self.BACK.pos, size_hint = self.BACK.hpair, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_PROMPT_SMALL.png',
            allow_stretch = True, keep_ratio = False)
        self.lbl = Label(size_hint = self.LBL.hpair, pos = self.LBL.pos,
            font_name = FONT_BASK, font_size = Size.FONT_SIZE_A)
        self.btns = BoxLayout(size_hint = self.BTNS.hpair,
            pos = self.BTNS.pos, orientation = 'vertical')
        self.move = AnchorButton(size_hint = self.BTN.hpair,
            text = 'Move to another bag', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_2.png')
        self.delete = AnchorButton(size_hint = self.BTN.hpair,
            text = 'Delete item', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_3.png')
        self.cancel = AnchorButton(size_hint = self.BTN.hpair,
            text = 'Cancel', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_4.png')



class ItemMove(Opens, HasBase):
    def __init__(self, Size, **kwargs):
        self.ITEMMOVE = SizeMap(32, 272, 368, 232, Size.Frame.pair)
        self.HALT = SizeMap(-32, -272, 432, 768, self.ITEMMOVE.pair)
        self.BACK = SizeMap(0, 0, 368, 232, self.ITEMMOVE.pair)
        self.BG = SizeMap(0, 0, 368, 232, self.ITEMMOVE.pair)
        self.LBL = SizeMap(12, 180, 344, 32, self.ITEMMOVE.pair)
        self.SCROLL = SizeMap(12, 12, 344, 160, self.ITEMMOVE.pair)
        self.ITEM = SizeMap(0, 0, 344, 32, self.SCROLL.pair)
        self.CANCEL = SizeMap(12, 12, 344, 40, self.ITEMMOVE.pair)

        self.container = base.screenMain
        self.is_open = False

        self.base = RelativeLayout(size_hint = self.ITEMMOVE.hpair,
            pos = self.ITEMMOVE.pos)
        self.halt = Halt(pos = self.HALT.pos)
        self.back = Button(pos = self.BACK.pos, size_hint = self.BACK.hpair, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_PROMPT_SMALL.png',
            allow_stretch = True, keep_ratio = False)
        self.lbl = Label(size_hint = self.LBL.hpair, pos = self.LBL.pos,
            font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            text = 'Where should this item be moved to?')
        self.scroll = ScrollView(size_hint = self.SCROLL.hpair,
            pos = self.SCROLL.pos, do_scroll_x = False, bar_width = 0)
        self.grid = GridLayout(size_hint = (1.0, None), cols = 1,
            row_default_height = self.ITEM.h, row_force_default = True)
        self.cancel = AnchorButton(pos = self.CANCEL.pos, size_hint = self.CANCEL.hpair,
            text = 'Cancel', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_4.png')



class Icon(Opens, HasBase):
    def __init__(self, Size, **kwargs):
        # ICON MENU
        self.ICON = SizeMap(36, 106, 360, 556, Size.Frame.pair)
        self.HALT = SizeMap(-36, -106, 432, 768, self.ICON.pair)
        self.SCROLL = SizeMap(20, 60, 320, 476, self.ICON.pair)
        self.BAR = SizeMap(0, 0, 4, 0, self.SCROLL.pair)
        self.GRID = SizeMap(0, 0, 320, 476, self.SCROLL.pair)
        self.PAD = SizeMap(16, 16, 90, 90, self.SCROLL.pair)
        self.SPACE = SizeMap(0, 0, 90, 16, self.SCROLL.pair)
        self.HEIGHT = SizeMap(0, 0, 80, 80, self.SCROLL.pair)
        self.CANCEL = SizeMap(20, 20, 156, 32, self.ICON.pair)
        self.SAVE = SizeMap(184, 20, 156, 32, self.ICON.pair)

        self.container = base.screenMain
        self.is_open = False

        self.base = RelativeLayout(size_hint = self.ICON.hpair, pos = self.ICON.pos)
        self.halt = Halt(pos = self.HALT.pos, disabled = True)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_PICK.png',
            allow_stretch = True, keep_ratio = False)
        self.scroll = ScrollView(size_hint = self.SCROLL.hpair,
            pos = self.SCROLL.pos, do_scroll_x = False,
            bar_width = self.BAR.w)
        self.grid = GridLayout(size_hint = (1.0, None), cols = 4,
            row_default_height = self.HEIGHT.h, row_force_default = True,
            col_default_width = self.HEIGHT.w, col_force_default = True)
        self.cancel = Button(size_hint = self.CANCEL.hpair,
            pos = self.CANCEL.pos, text = 'Cancel', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, color = WHITE)
        self.save = Button(size_hint = self.SAVE.hpair, pos = self.SAVE.pos,
            text = 'Save', font_name = FONT_BASK, font_size = Size.FONT_SIZE_D,
            color = WHITE)



class New(Opens, HasBase):
    def __init__(self, Size, **kwargs):
        self.NEW = SizeMap(0, 174, 422, 496, Size.Frame.pair)
        self.HALT = SizeMap(4, 8, 408, 420, self.NEW.pair)
        self.NAME = SizeMap(12, 375, 392, 30, self.NEW.pair)
        self.ICON = SizeMap(12, 213, 144, 144, self.NEW.pair)
        self.QTY = SizeMap(226, 327, 178, 30, self.NEW.pair)
        self.QTY_L = SizeMap(157, 327, 65, 30, self.NEW.pair)
        self.WEIGHT = SizeMap(226, 270, 178, 30, self.NEW.pair)
        self.WEIGHT_L = SizeMap(157, 270, 65, 30, self.NEW.pair)
        self.VAL = SizeMap(226, 213, 178, 30, self.NEW.pair)
        self.VAL_L = SizeMap(157, 213, 65, 30, self.NEW.pair)
        self.TAGS = SizeMap(12, 60, 192, 135, self.NEW.pair)
        self.TAGS_L = SizeMap(12, 196, 192, 30, self.NEW.pair)
        self.DESC = SizeMap(212, 60, 192, 135, self.NEW.pair)
        self.CANCEL = SizeMap(12, 16, 192, 36, self.NEW.pair)
        self.SAVE = SizeMap(212, 16, 192, 36, self.NEW.pair)

        self.container = base.screenMain
        self.is_open = False

        self.base = RelativeLayout(size_hint = self.NEW.hpair, pos = self.NEW.pos)
        self.halt = Halt(size_hint = self.HALT.hpair, pos = self.HALT.pos, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_DROP_NEW.png',
            allow_stretch = True, keep_ratio = False)
        self.name = TextInput(size_hint = self.NAME.hpair, hint_text = 'Name',
            pos = self.NAME.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C,
            write_tab = False, multiline = False)
        self.icon = Button(size_hint = self.ICON.hpair, pos = self.ICON.pos,
            background_normal = 'images/blankIcon.png',
            background_down = 'images/blankIcon.png', border = [0,0,0,0])
        self.qty = TextInput(size_hint = self.QTY.hpair, hint_text = 'Quantity',
            pos = self.QTY.pos, font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            write_tab = False, multiline = False)
        self.qty_L = AnchorLabel(size_hint = self.QTY_L.hpair, text = 'Quantity',
            pos = self.QTY_L.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C,
            anchor_x = 'right', color = BLACK, halign = 'right')
        self.weight = TextInput(size_hint = self.WEIGHT.hpair, hint_text = 'Weight',
            pos = self.WEIGHT.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, write_tab = False, multiline = False)
        self.weight_L = AnchorLabel(size_hint = self.WEIGHT_L.hpair,
            text = 'Weight', pos = self.WEIGHT_L.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, anchor_x = 'right', color = BLACK,
            halign = 'right')
        self.val = TextInput(size_hint = self.VAL.hpair, hint_text = 'Value',
            pos = self.VAL.pos, font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            write_tab = False, multiline = False)
        self.val_L = AnchorLabel(size_hint = self.VAL_L.hpair, text = 'Value',
            pos = self.VAL_L.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C,
            anchor_x = 'right', color = BLACK, halign = 'right')
        self.tags = TextInput(size_hint = self.TAGS.hpair, hint_text = 'Tags',
            pos = self.TAGS.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C)
        self.desc = TextInput(size_hint = self.DESC.hpair,
            hint_text = 'Item description', pos = self.DESC.pos,
            font_name = FONT_BASK, font_size = Size.FONT_SIZE_C)
        self.cancel = Button(size_hint = self.CANCEL.hpair, text = 'CANCEL',
            pos = self.CANCEL.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C)
        self.save = Button(size_hint = self.SAVE.hpair, text = 'SAVE',
            pos = self.SAVE.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C)


    def open(self):
        super(New, self).open(1)



class Sort(Opens, HasBase):
    def __init__(self, Size, **kwargs):
        self.SORT = SizeMap(140, 474, 288, 196, Size.Frame.pair)
        self.HALT = SizeMap(8, 8, 272, 120, self.SORT.pair)
        self.TYPE = SizeMap(16, 12, 124, 92, self.SORT.pair)
        self.TYPE_L = SizeMap(16, 106, 124, 30, self.SORT.pair)
        self.TYPE_BTN = SizeMap(0, 0, 124, 22, self.TYPE.pair)
        self.ORDER = SizeMap(148, 60, 124, 46, self.SORT.pair)
        self.ORDER_L = SizeMap(148, 104, 124, 30, self.SORT.pair)
        self.ORDER_BTN = SizeMap(0, 0, 124, 22, self.ORDER.pair)

        self.container = base.screenMain
        self.is_open = False

        self.base = RelativeLayout(size_hint = self.SORT.hpair, pos = self.SORT.pos)
        self.halt = Halt(size_hint = self.HALT.hpair, pos = self.HALT.pos, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_DROP_SORT.png',
            allow_stretch = True, keep_ratio = False)
        self.type_L = AnchorLabel(size_hint = self.TYPE_L.hpair, text = 'Sort by',
            pos = self.TYPE_L.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, anchor_x = 'left', anchor_y = 'bottom',
            color = BLACK, halign = 'left')
        self.type = BoxLayout(size_hint = self.TYPE.hpair,
            pos = self.TYPE.pos, orientation = 'vertical')
        self.type_name = AnchorToggleButton(size_hint = self.TYPE_BTN.hpair,
            text = 'Name', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortAttr',
            allow_no_selection = False, state = 'down')
        self.type_qty = AnchorToggleButton(size_hint = self.TYPE_BTN.hpair,
            text = 'Quantity', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortAttr',
            allow_no_selection = False)
        self.type_weight = AnchorToggleButton(size_hint = self.TYPE_BTN.hpair,
            text = 'Weight', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortAttr',
            allow_no_selection = False)
        self.type_val = AnchorToggleButton(size_hint = self.TYPE_BTN.hpair,
            text = 'Value', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortAttr',
            allow_no_selection = False)
        self.order_L = AnchorLabel(size_hint = self.ORDER_L.hpair,
            text = 'Sort order', pos = self.ORDER_L.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, anchor_x = 'left', anchor_y = 'bottom',
            color = BLACK, halign = 'left')
        self.order = BoxLayout(size_hint = self.ORDER.hpair,
            pos = self.ORDER.pos, orientation = 'vertical')
        self.order_asc = AnchorToggleButton(size_hint = self.ORDER_BTN.hpair,
            text = 'Ascending', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortMethod',
            allow_no_selection = False, state = 'down')
        self.order_desc = AnchorToggleButton(size_hint = self.ORDER_BTN.hpair,
            text = 'Descending', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortMethod',
            allow_no_selection = False)


    def open(self):
        super(Sort, self).open(1)



class View(Opens, HasBase):
    def __init__(self, Size, **kwargs):
        self.VIEW = SizeMap(148, 414, 284, 256, Size.Frame.pair)
        self.HALT = SizeMap(8, 8, 272, 180, self.VIEW.pair)
        self.NORM = SizeMap(16, 132, 256, 48, self.VIEW.pair)
        self.NORM_L = SizeMap(184, 144, 49, 24, self.VIEW.pair)
        self.NORM_CHECK = SizeMap(245, 153, 13, 12, self.VIEW.pair)
        self.COZY = SizeMap(16, 74, 256, 48, self.VIEW.pair)
        self.COZY_L = SizeMap(184, 86, 49, 24, self.VIEW.pair)
        self.COZY_CHECK = SizeMap(245, 95, 13, 12, self.VIEW.pair)
        self.CARD = SizeMap(16, 16, 256, 48, self.VIEW.pair)
        self.CARD_L = SizeMap(184, 28, 49, 24, self.VIEW.pair)
        self.CARD_CHECK = SizeMap(245, 37, 13, 12, self.VIEW.pair)

        self.container = base.screenMain
        self.is_open = False

        self.base = RelativeLayout(size_hint = self.VIEW.hpair, pos = self.VIEW.pos)
        self.halt = Halt(size_hint = self.HALT.hpair, pos = self.HALT.pos, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_DROP_VIEW.png',
            allow_stretch = True, keep_ratio = False)
        self.norm = Button(size_hint = self.NORM.hpair, pos = self.NORM.pos,
            opacity = 0)
        self.norm_L = AnchorLabel(size_hint = self.NORM_L.hpair,
            pos = self.NORM_L.pos, text = 'Normal', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_B, color = WHITE, anchor_x = 'right',
            halign = 'right')
        self.norm_Check = Image(size_hint = self.NORM_CHECK.hpair,
            pos = self.NORM_CHECK.pos, source = VIEW_CHECK_INACTIVE)
        self.cozy = Button(size_hint = self.COZY.hpair, pos = self.COZY.pos,
            opacity = 0)
        self.cozy_L = AnchorLabel(size_hint = self.COZY_L.hpair,
            pos = self.COZY_L.pos, text = 'Cozy', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_B, color = WHITE, anchor_x = 'right',
            halign = 'right')
        self.cozy_Check = Image(size_hint = self.COZY_CHECK.hpair,
            pos = self.COZY_CHECK.pos, source = VIEW_CHECK_INACTIVE)
        self.card = Button(size_hint = self.CARD.hpair, pos = self.CARD.pos,
            opacity = 0)
        self.card_L = AnchorLabel(size_hint = self.CARD_L.hpair,
            pos = self.CARD_L.pos, text = 'Cards', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_B, color = WHITE, anchor_x = 'right',
            halign = 'right')
        self.card_Check = Image(size_hint = self.CARD_CHECK.hpair,
            pos = self.CARD_CHECK.pos, source = VIEW_CHECK_INACTIVE)


    def open(self):
        super(View, self).open(1)



LogMsg('Creating widget groups...')

size = Size()
base = Base(size)
menu = Menu(size)
tabs = Tabs(size)
search = Search(size)
cont = Cont(size)
bagPick = BagPick(size)
bagOpts = BagOpts(size)
bagDelete = BagDelete(size)
itemOpts = ItemOpts(size)
itemMove = ItemMove(size)
pick = Pick(size)
icon = Icon(size)
dnew = New(size)
dsort = Sort(size)
dview = View(size)

FONT_SIZE_A = size.FONT_SIZE_A
FONT_SIZE_B = size.FONT_SIZE_B
FONT_SIZE_C = size.FONT_SIZE_C
FONT_SIZE_D = size.FONT_SIZE_D
FONT_SIZE_HEAD = size.FONT_SIZE_HEAD
