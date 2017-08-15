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
    def open(self):
        if self.pos_on != None:
            self.is_open = True
            self.base.pos = self.pos_on
        else:
            return 'No open position specified!'

    def close(self):
        if self.pos_off != None:
            self.is_open = False
            self.base.pos = self.pos_off
        else:
            return 'No close position specified!'



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
        self.FRAME = SizeMap(0, 0, 432, 768, (self.APP_W, self.APP_H))

        # MAIN
        self.MENU = SizeMap(0, 670, 432, 98, self.FRAME.pair)
        self.MENU_BTN_BAG = SizeMap(18, 18, 72, 72, self.MENU.pair)
        self.MENU_BTN_OPTS = SizeMap(342, 18, 72, 72, self.MENU.pair)
        self.MENU_TITLE = SizeMap(153, 34, 128, 40, self.MENU.pair)

        self.TABS = SizeMap(0, 602, 432, 60, self.FRAME.pair)
        self.TABS_BTN = SizeMap(0, 0, 144, 60, self.TABS.pair)

        self.SEARCH = SizeMap(11, 563, 326, 34, self.FRAME.pair)
        self.SEARCH_INPUT = SizeMap(34, 0, 284, 34, self.SEARCH.pair)

        self.CONT = SizeMap(0, 0, 432, 557, self.FRAME.pair)
        self.CONT_SPACE = SizeMap(0, 0, 0, 5, self.CONT.pair)
        self.CONT_PAD = SizeMap(0, 0, 2, 2, self.CONT.pair)
        self.CONT_SCROLL = SizeMap(0, 0, 12, 0, self.CONT.pair)

        # BAGPICK MENU
        self.BAGPICK = SizeMap(0, 0, 380, 768, self.FRAME.pair)
        self.BAGPICK_HALT = SizeMap(0, 0, 368, 768, self.BAGPICK.pair)
        self.BAGPICK_BACK = SizeMap(360, 0, 72, 768, self.BAGPICK.pair)
        self.BAGPICK_NAME = SizeMap(8, 698, 344, 56, self.BAGPICK.pair)
        self.BAGPICK_SCROLL = SizeMap(8, 60, 344, 636, self.BAGPICK.pair)
        self.BAGPICK_ITEM = SizeMap(0, 0, 344, 64, self.BAGPICK_SCROLL.pair)
        self.BAGPICK_ITEM_NAME = SizeMap(0, 24, 344, 40, self.BAGPICK_ITEM.pair)
        self.BAGPICK_ITEM_MISC = SizeMap(0, 4, 344, 20, self.BAGPICK_ITEM.pair)
        self.BAGPICK_NEW = SizeMap(8, 20, 344, 32, self.BAGPICK.pair)

        # BAGOPEN MENU
        self.BAGOPEN = SizeMap(32, 272, 368, 224, self.FRAME.pair)
        self.BAGOPEN_HALT = SizeMap(-36, -276, 432, 768, self.BAGOPEN.pair)
        self.BAGOPEN_NAME = SizeMap(12, 180, 344, 32, self.BAGOPEN.pair)
        self.BAGOPEN_BTNS = SizeMap(12, 12, 344, 160, self.BAGOPEN.pair)
        self.BAGOPEN_BTN = SizeMap(0, 0, 344, 40, self.BAGOPEN_BTNS.pair)

        # BAGDELETE MENU
        self.BAGDELETE = SizeMap(0, 0, 0, 0, self.FRAME.pair)

        # SELECTED ITEM
        # Note: spacing should be (20, 20, 392, 516)
        self.PICK = SizeMap(0, 105, 432, 557, self.FRAME.pair)
        self.PICK_HALT = SizeMap(0, -105, 432, 768, self.PICK.pair)
        self.PICK_NAME = SizeMap(20, 476, 392, 40, self.PICK.pair)
        self.PICK_ICON = SizeMap(138, 316, 156, 156, self.PICK.pair)
        self.PICK_MISC = SizeMap(21, 287, 390, 27, self.PICK.pair)
        self.PICK_QTY = SizeMap(0, 0, 130, 27, self.PICK.pair)
        self.PICK_WEIGHT = SizeMap(0, 1, 390, 27, self.PICK_MISC.pair)
        self.PICK_VAL = SizeMap(0, 0, 130, 27, self.PICK.pair)
        self.PICK_TAGS = SizeMap(20, 256, 392, 27, self.PICK.pair)
        self.PICK_DESC = SizeMap(20, 20, 392, 232, self.PICK.pair)
        self.PICK_OPTS = SizeMap(8, 550, 26, 26, self.PICK.pair)
        self.PICK_X = SizeMap(396, 550, 26, 26, self.PICK.pair)

        # ICON MENU
        self.ICON = SizeMap(36, 106, 360, 556, self.FRAME.pair)
        self.ICON_HALT = SizeMap(-36, -106, 432, 768, self.ICON.pair)
        self.ICON_SCROLL = SizeMap(20, 60, 320, 476, self.ICON.pair)
        self.ICON_BAR = SizeMap(0, 0, 4, 0, self.ICON_SCROLL.pair)
        self.ICON_GRID = SizeMap(0, 0, 320, 476, self.ICON_SCROLL.pair)
        self.ICON_PAD = SizeMap(16, 16, 90, 90, self.ICON_SCROLL.pair)
        self.ICON_SPACE = SizeMap(0, 0, 90, 16, self.ICON_SCROLL.pair)
        self.ICON_HEIGHT = SizeMap(0, 0, 80, 80, self.ICON_SCROLL.pair)
        self.ICON_CANCEL = SizeMap(20, 20, 156, 32, self.ICON.pair)
        self.ICON_SAVE = SizeMap(184, 20, 156, 32, self.ICON.pair)

        # DROP MENUS
        self.DROP_NEW = SizeMap(0, 174, 422, 496, self.FRAME.pair)
        self.DROP_SORT = SizeMap(140, 474, 288, 196, self.FRAME.pair)
        self.DROP_VIEW = SizeMap(148, 414, 284, 256, self.FRAME.pair)
        self.DROP_NEW_HALT = SizeMap(4, 8, 408, 420, self.DROP_NEW.pair)
        self.DROP_SORT_HALT = SizeMap(8, 8, 272, 120, self.DROP_SORT.pair)
        self.DROP_VIEW_HALT = SizeMap(8, 8, 272, 180, self.DROP_VIEW.pair)

        # ITEMS
        self.ITEMVIEW_COZY = SizeMap(0, 0, 408, 84, self.CONT.pair)
        self.ITEMVIEW_NORM = SizeMap(0, 0, 408, 24, self.CONT.pair)
        self.ITEMVIEW_CARD = SizeMap(0, 0, 408, 156, self.CONT.pair)
        self.IV_COZY_ICON = SizeMap(8, 8, 68, 68, self.ITEMVIEW_COZY.pair)
        self.IV_COZY_NAME = SizeMap(84, 40, 316, 30, self.ITEMVIEW_COZY.pair)
        self.IV_COZY_MISC = SizeMap(84, 10, 316, 24, self.ITEMVIEW_COZY.pair)
        self.IV_NORM_ICON = SizeMap(4, 4, 16, 16, self.ITEMVIEW_NORM.pair)
        self.IV_NORM_NAME = SizeMap(24, 2, 204, 24, self.ITEMVIEW_NORM.pair)
        self.IV_NORM_MISC = SizeMap(232, 2, 172, 24, self.ITEMVIEW_NORM.pair)
        self.IV_CARD_ICON = SizeMap(8, 80, 68, 68, self.ITEMVIEW_CARD.pair)
        self.IV_CARD_NAME = SizeMap(84, 112, 316, 30, self.ITEMVIEW_CARD.pair)
        self.IV_CARD_MISC = SizeMap(84, 82, 316, 24, self.ITEMVIEW_CARD.pair)
        self.IV_CARD_DESC = SizeMap(8, 8, 392, 64, self.ITEMVIEW_CARD.pair)

        # NEW
        self.NEW_NAME = SizeMap(12, 375, 392, 30, self.DROP_NEW.pair)
        self.NEW_ICON = SizeMap(12, 213, 144, 144, self.DROP_NEW.pair)
        self.NEW_QTY = SizeMap(226, 327, 178, 30, self.DROP_NEW.pair)
        self.NEW_QTY_L = SizeMap(157, 327, 65, 30, self.DROP_NEW.pair)
        self.NEW_WEIGHT = SizeMap(226, 270, 178, 30, self.DROP_NEW.pair)
        self.NEW_WEIGHT_L = SizeMap(157, 270, 65, 30, self.DROP_NEW.pair)
        self.NEW_VAL = SizeMap(226, 213, 178, 30, self.DROP_NEW.pair)
        self.NEW_VAL_L = SizeMap(157, 213, 65, 30, self.DROP_NEW.pair)
        self.NEW_TAGS = SizeMap(12, 60, 192, 135, self.DROP_NEW.pair)
        self.NEW_TAGS_L = SizeMap(12, 196, 192, 30, self.DROP_NEW.pair)
        self.NEW_DESC = SizeMap(212, 60, 192, 135, self.DROP_NEW.pair)
        self.NEW_CANCEL = SizeMap(12, 16, 192, 36, self.DROP_NEW.pair)
        self.NEW_SAVE = SizeMap(212, 16, 192, 36, self.DROP_NEW.pair)

        # SORT
        self.SORT_TYPE = SizeMap(16, 12, 124, 92, self.DROP_SORT.pair)
        self.SORT_TYPE_L = SizeMap(16, 106, 124, 30, self.DROP_SORT.pair)
        self.SORT_TYPE_BTN = SizeMap(0, 0, 124, 22, self.SORT_TYPE.pair)
        self.SORT_ORDER = SizeMap(148, 60, 124, 46, self.DROP_SORT.pair)
        self.SORT_ORDER_L = SizeMap(148, 104, 124, 30, self.DROP_SORT.pair)
        self.SORT_ORDER_BTN = SizeMap(0, 0, 124, 22, self.SORT_ORDER.pair)

        # VIEW
        self.VIEW_NORM = SizeMap(16, 132, 256, 48, self.DROP_VIEW.pair)
        self.VIEW_NORM_L = SizeMap(184, 144, 49, 24, self.DROP_VIEW.pair)
        self.VIEW_NORM_CHECK = SizeMap(245, 153, 13, 12, self.DROP_VIEW.pair)
        self.VIEW_COZY = SizeMap(16, 74, 256, 48, self.DROP_VIEW.pair)
        self.VIEW_COZY_L = SizeMap(184, 86, 49, 24, self.DROP_VIEW.pair)
        self.VIEW_COZY_CHECK = SizeMap(245, 95, 13, 12, self.DROP_VIEW.pair)
        self.VIEW_CARD = SizeMap(16, 16, 256, 48, self.DROP_VIEW.pair)
        self.VIEW_CARD_L = SizeMap(184, 28, 49, 24, self.DROP_VIEW.pair)
        self.VIEW_CARD_CHECK = SizeMap(245, 37, 13, 12, self.DROP_VIEW.pair)



class ScreenPos():
    def __init__(self, Size, **kwargs):
        self.ON = ZEROS
        self.OFF = (Size.APP_W, Size.APP_H)
        self.FAR_OFF = (Size.APP_W*2, Size.APP_H*2)



class Base():
    def __init__(self, Size, ScreenPos, **kwargs):
        # FRAME
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_MAIN.png',
            allow_stretch = True, keep_ratio = False)

        # SCREENS
        self.screenMain = RelativeLayout(pos = ScreenPos.ON, size_hint = FILLS)
        self.screenSettings = RelativeLayout(pos = ScreenPos.OFF, size_hint = FILLS)



class Menu(HasBase):
    def __init__(self, Size, ScreenPos, **kwargs):
        # Menu
        self.base = RelativeLayout(pos = Size.MENU.pos, size_hint = Size.MENU.hpair)
        self.title = Label(size_hint = Size.MENU_TITLE.hpair, pos = Size.MENU_TITLE.pos,
            font_name = FONT_BASK, font_size = Size.FONT_SIZE_A, color = WHITE)
        self.bag = Image(size_hint = Size.MENU_BTN_BAG.hpair,
            pos = Size.MENU_BTN_BAG.pos,
            source = 'images/IMG_BAGS.png', keep_ratio = False, allow_stretch = True)
        self.bagBtn = Button(size_hint = Size.MENU_BTN_BAG.hpair,
            pos = Size.MENU_BTN_BAG.pos, background_color = CLEAR)
        self.opts = Image(size_hint = Size.MENU_BTN_OPTS.hpair,
            pos = Size.MENU_BTN_OPTS.pos, source = 'images/IMG_SETTINGS.png',
            keep_ratio = False, allow_stretch = True)
        self.optsBtn = Button(size_hint = Size.MENU_BTN_OPTS.hpair,
            pos = Size.MENU_BTN_OPTS.pos, background_color = CLEAR)



class Tabs(HasBase):
    def __init__(self, Size, ScreenPos, **kwargs):
        # Tabs
        self.base = BoxLayout(size_hint = Size.TABS.hpair, pos = Size.TABS.pos,
            orientation = 'horizontal')
        self.new = Button(size_hint = Size.TABS_BTN.hpair, text = 'NEW', color = WHITE,
            font_name = FONT_BASK, font_size = Size.FONT_SIZE_A,
            background_color = CLEAR)
        self.sort = Button(size_hint = Size.TABS_BTN.hpair, text = 'SORT',
            color = WHITE, font_name = FONT_BASK, font_size = Size.FONT_SIZE_A,
            background_color = CLEAR)
        self.view = Button(size_hint = Size.TABS_BTN.hpair, text = 'VIEW',
            color = WHITE, font_name = FONT_BASK, font_size = Size.FONT_SIZE_A,
            background_color = CLEAR)



class Search(HasBase):
    def __init__(self, Size, ScreenPos, **kwargs):
        # Search
        self.base = RelativeLayout(size_hint = Size.SEARCH.hpair, pos = Size.SEARCH.pos)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_SEARCH.png',
            allow_stretch = True, keep_ratio = False)
        self.input = TextInput(size_hint = Size.SEARCH_INPUT.hpair,
            pos = Size.SEARCH_INPUT.pos, hint_text = 'Search for an item...',
            font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            foreground_color = BLACK, write_tab = False, multiline = False,
            cursor_color = BLACK, background_normal = '', background_active = '',
            background_color = CLEAR)



class Cont(HasBase):
    def __init__(self, Size, ScreenPos, **kwargs):
        # Content
        self.base = RelativeLayout(size_hint = Size.CONT.hpair, pos = Size.CONT.pos)
        self.scroll = ScrollView(size_hint = FILLS, do_scroll_x = False,
            bar_width = Size.CONT_SCROLL.x)
        self.list = GridLayout(size_hint = (1.0, None), cols = 1,
            padding = list(Size.CONT_PAD.pair), spacing = list(Size.CONT_SPACE.pair),
            row_force_default = True)



class BagPick(Opens, HasBase):
    def __init__(self, pos_on, pos_off, Size, ScreenPos, **kwargs):
        # Bag selection menu
        self.pos_on = pos_on
        self.pos_off = pos_off
        self.is_open = False

        self.base = RelativeLayout(size_hint = Size.BAGPICK.hpair, pos = ScreenPos.OFF)
        self.back = Button(pos = Size.BAGPICK_BACK.pos,
            size_hint = Size.BAGPICK_BACK.hpair, background_normal = IMG_BLACK,
            background_down = IMG_BLACK, opacity = 0.5)
        self.halt = Button(pos = Size.BAGPICK_HALT.pos,
            size_hint = Size.BAGPICK_HALT.hpair, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_BAG_PICK_BG.png',
            allow_stretch = True, keep_ratio = False)
        self.name = Label(size_hint = Size.BAGPICK_NAME.hpair,
            pos = Size.BAGPICK_NAME.pos, text = 'Bags', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_A)
        self.scroll = ScrollView(size_hint = Size.BAGPICK_SCROLL.hpair,
            pos = Size.BAGPICK_SCROLL.pos, do_scroll_x = False, bar_width = 0)
        self.grid = GridLayout(size_hint = (1.0, None), cols = 1,
            row_default_height = Size.BAGPICK_ITEM.h, row_force_default = True)
        self.newBag = AnchorButton(size_hint = Size.BAGPICK_NEW.hpair,
            pos = Size.BAGPICK_NEW.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, text = 'New Bag')



class BagOpen(Opens, HasBase):
    def __init__(self, pos_on, pos_off, Size, ScreenPos,**kwargs):
        # Bag open/edit menu
        self.pos_on = pos_on
        self.pos_off = pos_off
        self.is_open = False

        self.base = RelativeLayout(size_hint = Size.BAGOPEN.hpair, pos = self.pos_off)
        self.halt = Button(size_hint = Size.BAGOPEN_HALT.hpair,
            pos = Size.BAGOPEN_HALT.pos, background_normal = IMG_BLACK,
            background_down = IMG_BLACK, opacity = 0.5)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_BAG_OPEN_BG.png',
            allow_stretch = True, keep_ratio = False)
        self.name = Label(size_hint = Size.BAGOPEN_NAME.hpair,
            pos = Size.BAGOPEN_NAME.pos, text = 'Bag Name', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_A)
        self.btns = BoxLayout(size_hint = Size.BAGOPEN_BTNS.hpair,
            pos = Size.BAGOPEN_BTNS.pos, orientation = 'vertical')
        self.weight = AnchorButton(size_hint = Size.BAGOPEN_BTN.hpair,
            text = 'Set weight system', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_1.png')
        self.currency = AnchorButton(size_hint = Size.BAGOPEN_BTN.hpair,
            text = 'Set currency system', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_2.png')
        self.delete = AnchorButton(size_hint = Size.BAGOPEN_BTN.hpair,
            text = 'Delete bag', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_3.png')
        self.done = AnchorButton(size_hint = Size.BAGOPEN_BTN.hpair,
            text = 'Save Changes', color = WHITE, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, valign = 'bottom', border = [0,0,0,0],
            background_img = 'images/IMG_BTN_BG_4.png')



class BagDelete(Opens, HasBase):
    def __init__(self, pos_on, pos_off, Size, ScreenPos, **kwargs):
        self.pos_on = pos_on
        self.pos_off = pos_off
        self.is_open = False

        self.base = RelativeLayout(size_hint = Size.BAGDELETE.hpair, pos = self.pos_off)



class Pick(Opens, HasBase):
    def __init__(self, pos_on, pos_off, Size, ScreenPos, **kwargs):
        # Selected Item
        self.pos_on = pos_on
        self.pos_off = pos_off
        self.is_open = False

        self.base = RelativeLayout(size_hint = Size.PICK.hpair, pos = ScreenPos.OFF)
        self.halt = Button(pos = Size.PICK_HALT.pos, size_hint = Size.PICK_HALT.hpair,
            background_disabled_normal = IMG_BLACK, opacity = 0.5, disabled = True)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_PICK.png',
            allow_stretch = True, keep_ratio = False)
        self.widges = RelativeLayout(size_hint = FILLS, pos = ZEROS)
        self.name = TextInput(size_hint = Size.PICK_NAME.hpair,
            pos = Size.PICK_NAME.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_A, foreground_color = BLACK,
            border = [2,2,2,2], write_tab = False, multiline = False,
            cursor_color = BLACK, background_normal = 'images/IMG_1x1BORDER.png',
            hint_text = 'Item Name', background_active = 'images/IMG_1x1BORDER.png')
        self.icon = Button(size_hint = Size.PICK_ICON.hpair, pos = Size.PICK_ICON.pos,
            background_normal = 'images/blankIcon.png',
            background_down = 'images/blankIcon.png', border = [0,0,0,0])
        self.misc = BoxLayout(size_hint = Size.PICK_MISC.hpair,
            pos = Size.PICK_MISC.pos, orientation = 'horizontal')
        self.qty_L = AnchorLabel(pos = Size.PICK_QTY.pos, font_name = FONT_BASK,
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
        self.tags = TextInput(size_hint = Size.PICK_TAGS.hpair,
            pos = Size.PICK_TAGS.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, foreground_color = BLACK,
            background_normal = 'images/IMG_1x1BORDER.png',
            background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
            cursor_color = BLACK)
        self.desc = TextInput(size_hint = Size.PICK_DESC.hpair,
            pos = Size.PICK_DESC.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, foreground_color = BLACK,
            background_normal = 'images/IMG_1x1BORDER.png',
            background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
            cursor_color = BLACK)
        self.opts = AnchorButton(size_hint = Size.PICK_OPTS.hpair,
            pos = Size.PICK_OPTS.pos, source = 'images/IMG_SETTINGS.png',
            keep_ratio = True, allow_stretch = False, background_img = None)
        self.X = AnchorButton(size_hint = Size.PICK_X.hpair, pos = Size.PICK_X.pos,
            text = 'X', font_name = FONT_BASK, font_size = Size.FONT_SIZE_D,
            color = WHITE, background_img = None, valign = 'bottom')



class Icon(Opens, HasBase):
    def __init__(self, pos_on, pos_off, Size, ScreenPos, **kwargs):
        # Icon selection
        self.pos_on = pos_on
        self.pos_off = pos_off
        self.is_open = False

        self.base = RelativeLayout(size_hint = Size.ICON.hpair, pos = ScreenPos.FAR_OFF)
        self.halt = Button(pos = Size.ICON_HALT.pos, size_hint = Size.ICON_HALT.hpair,
            background_disabled_normal = IMG_BLACK, opacity = 0.5, disabled = True)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_PICK.png',
            allow_stretch = True, keep_ratio = False)
        self.scroll = ScrollView(size_hint = Size.ICON_SCROLL.hpair,
            pos = Size.ICON_SCROLL.pos, do_scroll_x = False,
            bar_width = Size.ICON_BAR.w)
        self.grid = GridLayout(size_hint = (1.0, None), cols = 4,
            row_default_height = Size.ICON_HEIGHT.h, row_force_default = True,
            col_default_width = Size.ICON_HEIGHT.w, col_force_default = True)
        self.cancel = Button(size_hint = Size.ICON_CANCEL.hpair,
            pos = Size.ICON_CANCEL.pos, text = 'Cancel', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_D, color = WHITE)
        self.save = Button(size_hint = Size.ICON_SAVE.hpair, pos = Size.ICON_SAVE.pos,
            text = 'Save', font_name = FONT_BASK, font_size = Size.FONT_SIZE_D,
            color = WHITE)



class New(Opens, HasBase):
    def __init__(self, pos_on, pos_off, Size, ScreenPos, **kwargs):
        # Tab drop: New
        self.pos_on = pos_on
        self.pos_off = pos_off
        self.is_open = False

        self.base = RelativeLayout(size_hint = Size.DROP_NEW.hpair,
            pos = ScreenPos.OFF)
        self.halt = Button(size_hint = Size.DROP_NEW_HALT.hpair,
            pos = Size.DROP_NEW_HALT.pos, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_DROP_NEW.png',
            allow_stretch = True, keep_ratio = False)
        self.name = TextInput(size_hint = Size.NEW_NAME.hpair, hint_text = 'Name',
            pos = Size.NEW_NAME.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C,
            write_tab = False, multiline = False)
        self.icon = Button(size_hint = Size.NEW_ICON.hpair, pos = Size.NEW_ICON.pos,
            background_normal = 'images/blankIcon.png',
            background_down = 'images/blankIcon.png', border = [0,0,0,0])
        self.qty = TextInput(size_hint = Size.NEW_QTY.hpair, hint_text = 'Quantity',
            pos = Size.NEW_QTY.pos, font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            write_tab = False, multiline = False)
        self.qty_L = AnchorLabel(size_hint = Size.NEW_QTY_L.hpair, text = 'Quantity',
            pos = Size.NEW_QTY_L.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C,
            anchor_x = 'right', color = BLACK, halign = 'right')
        self.weight = TextInput(size_hint = Size.NEW_WEIGHT.hpair, hint_text = 'Weight',
            pos = Size.NEW_WEIGHT.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, write_tab = False, multiline = False)
        self.weight_L = AnchorLabel(size_hint = Size.NEW_WEIGHT_L.hpair,
            text = 'Weight', pos = Size.NEW_WEIGHT_L.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, anchor_x = 'right', color = BLACK,
            halign = 'right')
        self.val = TextInput(size_hint = Size.NEW_VAL.hpair, hint_text = 'Value',
            pos = Size.NEW_VAL.pos, font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            write_tab = False, multiline = False)
        self.val_L = AnchorLabel(size_hint = Size.NEW_VAL_L.hpair, text = 'Value',
            pos = Size.NEW_VAL_L.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C,
            anchor_x = 'right', color = BLACK, halign = 'right')
        self.tags = TextInput(size_hint = Size.NEW_TAGS.hpair, hint_text = 'Tags',
            pos = Size.NEW_TAGS.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C)
        self.desc = TextInput(size_hint = Size.NEW_DESC.hpair,
            hint_text = 'Item description', pos = Size.NEW_DESC.pos,
            font_name = FONT_BASK, font_size = Size.FONT_SIZE_C)
        self.cancel = Button(size_hint = Size.NEW_CANCEL.hpair, text = 'CANCEL',
            pos = Size.NEW_CANCEL.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C)
        self.save = Button(size_hint = Size.NEW_SAVE.hpair, text = 'SAVE',
            pos = Size.NEW_SAVE.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C)



class Sort(Opens, HasBase):
    def __init__(self, pos_on, pos_off, Size, ScreenPos, **kwargs):
        self.pos_on = pos_on
        self.pos_off = pos_off
        self.is_open = False

        self.base = RelativeLayout(size_hint = Size.DROP_SORT.hpair,
            pos = ScreenPos.OFF)
        self.halt = Button(size_hint = Size.DROP_SORT_HALT.hpair,
            pos = Size.DROP_SORT_HALT.pos, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_DROP_SORT.png',
            allow_stretch = True, keep_ratio = False)
        self.type_L = AnchorLabel(size_hint = Size.SORT_TYPE_L.hpair, text = 'Sort by',
            pos = Size.SORT_TYPE_L.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, anchor_x = 'left', anchor_y = 'bottom',
            color = BLACK, halign = 'left')
        self.type = BoxLayout(size_hint = Size.SORT_TYPE.hpair,
            pos = Size.SORT_TYPE.pos, orientation = 'vertical')
        self.type_name = AnchorToggleButton(size_hint = Size.SORT_TYPE_BTN.hpair,
            text = 'Name', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortAttr',
            allow_no_selection = False, state = 'down')
        self.type_qty = AnchorToggleButton(size_hint = Size.SORT_TYPE_BTN.hpair,
            text = 'Quantity', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortAttr',
            allow_no_selection = False)
        self.type_weight = AnchorToggleButton(size_hint = Size.SORT_TYPE_BTN.hpair,
            text = 'Weight', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortAttr',
            allow_no_selection = False)
        self.type_val = AnchorToggleButton(size_hint = Size.SORT_TYPE_BTN.hpair,
            text = 'Value', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortAttr',
            allow_no_selection = False)
        self.order_L = AnchorLabel(size_hint = Size.SORT_ORDER_L.hpair,
            text = 'Sort order', pos = Size.SORT_ORDER_L.pos, font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_C, anchor_x = 'left', anchor_y = 'bottom',
            color = BLACK, halign = 'left')
        self.order = BoxLayout(size_hint = Size.SORT_ORDER.hpair,
            pos = Size.SORT_ORDER.pos, orientation = 'vertical')
        self.order_asc = AnchorToggleButton(size_hint = Size.SORT_ORDER_BTN.hpair,
            text = 'Ascending', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortMethod',
            allow_no_selection = False, state = 'down')
        self.order_desc = AnchorToggleButton(size_hint = Size.SORT_ORDER_BTN.hpair,
            text = 'Descending', font_name = FONT_BASK, font_size = Size.FONT_SIZE_C,
            color = BLACK, anchor_x = 'left', halign = 'left', group = 'sortMethod',
            allow_no_selection = False)



class View(Opens, HasBase):
    def __init__(self, pos_on, pos_off, Size, ScreenPos, **kwargs):
        self.pos_on = pos_on
        self.pos_off = pos_off
        self.is_open = False

        self.base = RelativeLayout(size_hint = Size.DROP_VIEW.hpair,
            pos = ScreenPos.OFF)
        self.halt = Button(size_hint = Size.DROP_VIEW_HALT.hpair,
            pos = Size.DROP_VIEW_HALT.pos, opacity = 0)
        self.BG = Image(size_hint = FILLS, source = 'images/IMG_DROP_VIEW.png',
            allow_stretch = True, keep_ratio = False)
        self.norm = Button(size_hint = Size.VIEW_NORM.hpair, pos = Size.VIEW_NORM.pos,
            opacity = 0)
        self.norm_L = AnchorLabel(size_hint = Size.VIEW_NORM_L.hpair,
            pos = Size.VIEW_NORM_L.pos, text = 'Normal', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_B, color = WHITE, anchor_x = 'right',
            halign = 'right')
        self.norm_Check = Image(size_hint = Size.VIEW_NORM_CHECK.hpair,
            pos = Size.VIEW_NORM_CHECK.pos, source = VIEW_CHECK_INACTIVE)
        self.cozy = Button(size_hint = Size.VIEW_COZY.hpair, pos = Size.VIEW_COZY.pos,
            opacity = 0)
        self.cozy_L = AnchorLabel(size_hint = Size.VIEW_COZY_L.hpair,
            pos = Size.VIEW_COZY_L.pos, text = 'Cozy', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_B, color = WHITE, anchor_x = 'right',
            halign = 'right')
        self.cozy_Check = Image(size_hint = Size.VIEW_COZY_CHECK.hpair,
            pos = Size.VIEW_COZY_CHECK.pos, source = VIEW_CHECK_INACTIVE)
        self.card = Button(size_hint = Size.VIEW_CARD.hpair, pos = Size.VIEW_CARD.pos,
            opacity = 0)
        self.card_L = AnchorLabel(size_hint = Size.VIEW_CARD_L.hpair,
            pos = Size.VIEW_CARD_L.pos, text = 'Cards', font_name = FONT_BASK,
            font_size = Size.FONT_SIZE_B, color = WHITE, anchor_x = 'right',
            halign = 'right')
        self.card_Check = Image(size_hint = Size.VIEW_CARD_CHECK.hpair,
            pos = Size.VIEW_CARD_CHECK.pos, source = VIEW_CHECK_INACTIVE)


LogMsg('Creating widget groups...')

size = Size()
screenPos = ScreenPos(size)
base = Base(size, screenPos)
menu = Menu(size, screenPos)
tabs = Tabs(size, screenPos)
search = Search(size, screenPos)
cont = Cont(size, screenPos)
bagPick = BagPick(size.BAGPICK.pos, screenPos.OFF, size, screenPos)
bagOpen = BagOpen(size.BAGOPEN.pos, screenPos.FAR_OFF, size, screenPos)
bagDelete = BagDelete(size.BAGDELETE.pos, screenPos.FAR_OFF, size, screenPos)
pick = Pick(size.PICK.pos, screenPos.OFF, size, screenPos)
icon = Icon(size.ICON.pos, screenPos.FAR_OFF, size, screenPos)
dnew = New(size.DROP_NEW.pos, screenPos.OFF, size, screenPos)
dsort = Sort(size.DROP_SORT.pos, screenPos.OFF, size, screenPos)
dview = View(size.DROP_VIEW.pos, screenPos.OFF, size, screenPos)

FONT_SIZE_A = size.FONT_SIZE_A
FONT_SIZE_B = size.FONT_SIZE_B
FONT_SIZE_C = size.FONT_SIZE_C
FONT_SIZE_D = size.FONT_SIZE_D
FONT_SIZE_HEAD = size.FONT_SIZE_HEAD
