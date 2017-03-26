from SysFuncs import *
from LoadSaves import *
from Bag import *
from BagItem import *
from InvisBtn import *
from AnchorLabel import *

#=======================================================================================#
# SYSTEM VARIABLES                                                                      #
#=======================================================================================#
if True:
    # Stylization =======================================================================
    FONT_SIZE_A = 32
    FONT_SIZE_B = 20
    FONT_SIZE_C = 16
    FONT_BASK = 'fonts/BASKVILLE.TTF'
    WHITE = [1,1,1,1]
    BLACK = [0,0,0,1]
    CLEAR = [0,0,0,0]

    # Sizes =============================================================================
    APP_W = 432 / XSCALE
    APP_H = 768 / YSCALE
    FRAME = SizeMap(0, 0, 432, 768, (APP_W, APP_H))

    # MAIN
    MENU = SizeMap(0, 670, 432, 98, FRAME.pair)
    MENU_BTN_BAG = SizeMap(18, 18, 72, 72, MENU.pair)
    MENU_BTN_OPTS = SizeMap(342, 18, 72, 72, MENU.pair)
    MENU_TITLE = SizeMap(153, 34, 128, 40, MENU.pair)

    TABS = SizeMap(0, 602, 432, 60, FRAME.pair)
    TABS_BTN = SizeMap(0, 0, 144, 60, TABS.pair)

    # DROP MENUS
    DROP_NEW = SizeMap(0, 174, 422, 496, FRAME.pair)
    DROP_NEW_HALT = SizeMap(4, 8, 408, 420, DROP_NEW.pair)
    DROP_SORT = SizeMap(140, 414, 288, 256, FRAME.pair)
    DROP_SORT_HALT = SizeMap(8, 8, 272, 180, DROP_NEW.pair)
    DROP_VIEW = SizeMap(4, 182, 408, 480, FRAME.pair)

    CONT = SizeMap(0, 0, 432, 557, FRAME.pair)
    CONTPANE = SizeMap(0, 0, 1040, 1560, CONT.pair)
    CONT_SPACE = SizeMap(0, 0, 0, 5, CONT.pair)
    CONT_PAD = SizeMap(0, 0, 2, 2, CONT.pair)
    CONT_SCROLL = SizeMap(0, 0, 20, 0, CONT.pair)

    # ITEMS
    ITEMVIEW_COZY = SizeMap(0, 0, 408, 84, CONTPANE.pair)
    ITEMVIEW_NORM = SizeMap(0, 0, 408, 24, CONTPANE.pair)
    ITEMVIEW_CARD = SizeMap(0, 0, 408, 120, CONTPANE.pair)
    IV_COZY_ICON = SizeMap(8, 8, 68, 68, ITEMVIEW_COZY.pair)
    IV_COZY_NAME = SizeMap(84, 40, 316, 30, ITEMVIEW_COZY.pair)
    IV_COZY_MISC = SizeMap(84, 10, 316, 24, ITEMVIEW_COZY.pair)
    IV_NORM_ICON = SizeMap(14, 14, 172, 172, ITEMVIEW_NORM.pair)
    IV_NORM_NAME = SizeMap(218, 102, 790, 75, ITEMVIEW_NORM.pair)
    IV_NORM_MISC = SizeMap(218, 15, 790, 65, ITEMVIEW_NORM.pair)
    IV_CARD_ICON = SizeMap(14, 14, 172, 172, ITEMVIEW_CARD.pair)
    IV_CARD_NAME = SizeMap(218, 102, 790, 75, ITEMVIEW_CARD.pair)
    IV_CARD_MISC = SizeMap(218, 15, 790, 65, ITEMVIEW_CARD.pair)

    # NEW
    NEW_NAME = SizeMap(12, 375, 392, 30, DROP_NEW.pair)
    NEW_ICON = SizeMap(12, 213, 144, 144, DROP_NEW.pair)
    NEW_QTY = SizeMap(226, 327, 178, 30, DROP_NEW.pair)
    NEW_QTY_L = SizeMap(157, 327, 65, 30, DROP_NEW.pair)
    NEW_WEIGHT = SizeMap(226, 270, 178, 30, DROP_NEW.pair)
    NEW_WEIGHT_L = SizeMap(157, 270, 65, 30, DROP_NEW.pair)
    NEW_VAL = SizeMap(226, 213, 178, 30, DROP_NEW.pair)
    NEW_VAL_L = SizeMap(157, 213, 65, 30, DROP_NEW.pair)
    NEW_TAGS = SizeMap(12, 60, 192, 135, DROP_NEW.pair)
    NEW_TAGS_L = SizeMap(12, 196, 192, 30, DROP_NEW.pair)
    NEW_DESC = SizeMap(212, 60, 192, 135, DROP_NEW.pair)
    NEW_CANCEL = SizeMap(12, 16, 192, 36, DROP_NEW.pair)
    NEW_SAVE = SizeMap(212, 16, 192, 36, DROP_NEW.pair)

    # Positions =========================================================================
    # SCREENS
    SCREEN_POS_ON = ZEROS
    SCREEN_POS_OFF = (APP_W, 0)


#=======================================================================================#
# APP WIDGETS                                                                           #
#=======================================================================================#
if True:
    # FRAME
    BG = Image(size_hint = FILLS, source = 'images/IMG_MAIN.png')

    # SCREENS
    screenMain = RelativeLayout(pos = SCREEN_POS_ON, size_hint = FILLS)
    screenSettings = RelativeLayout(pos = SCREEN_POS_OFF, size_hint = FILLS)

    # Menu
    menu = RelativeLayout(pos = MENU.pos, size_hint = MENU.hpair)
    menuTitle = Label(size_hint = MENU_TITLE.hpair, pos = MENU_TITLE.pos,
        font_name = FONT_BASK, font_size = FONT_SIZE_A, color = WHITE)
    menuBag = Button(size_hint = MENU_BTN_BAG.hpair, pos = MENU_BTN_BAG.pos,
        background_color = CLEAR)
    menuOpts = Button(size_hint = MENU_BTN_OPTS.hpair, pos = MENU_BTN_OPTS.pos,
        background_color = CLEAR)

    # Tabs
    tabs = BoxLayout(size_hint = TABS.hpair, pos = TABS.pos, orientation = 'horizontal')
    tabsNew = Button(size_hint = TABS_BTN.hpair, text = 'NEW', color = WHITE,
        font_name = FONT_BASK, font_size = FONT_SIZE_A, background_color = CLEAR)
    tabsSort = Button(size_hint = TABS_BTN.hpair, text = 'SORT', color = WHITE,
        font_name = FONT_BASK, font_size = FONT_SIZE_A, background_color = CLEAR)
    tabsView = Button(size_hint = TABS_BTN.hpair, text = 'VIEW', color = WHITE,
        font_name = FONT_BASK, font_size = FONT_SIZE_A, background_color = CLEAR)

    # Tab drops
    dropNew = RelativeLayout(size_hint = DROP_NEW.hpair, pos = SCREEN_POS_OFF)
    dropNewHalt = InvisBtn(size_hint = DROP_NEW_HALT.hpair, pos = DROP_NEW_HALT.pos)
    dropNewBG = Image(size_hint = FILLS, source = 'images/IMG_DROP_NEW.png')

    dropSort = RelativeLayout(size_hint = DROP_SORT.hpair, pos = SCREEN_POS_OFF)
    dropSortHalt = InvisBtn(size_hint = DROP_SORT_HALT.hpair, pos = DROP_SORT_HALT.pos)
    dropSortBG = Image(size_hint = FILLS, source = 'images/IMG_DROP_SORT.png')

    # Content
    cont = RelativeLayout(pos = CONT.pos, size_hint = CONT.hpair)
    contScroll = ScrollView(size_hint = FILLS, do_scroll_x = False,
        bar_width = CONT_SCROLL.x)
    contList = GridLayout(size_hint = (1.0, None), cols = 1,
        padding = list(CONT_PAD.pair), spacing = list(CONT_SPACE.pair),
        row_force_default = True)

    # NEW ITEM WIDGETS
    newName = TextInput(size_hint = NEW_NAME.hpair, hint_text = 'Name',
        pos = NEW_NAME.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C)

    newIcon = Image(size_hint = NEW_ICON.hpair, source = 'images/blankIcon.png',
        pos = NEW_ICON.pos, allow_stretch = True, keep_ratio = False)

    newQty = TextInput(size_hint = NEW_QTY.hpair, hint_text = 'Quantity',
        pos = NEW_QTY.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C)
    newQty_L = AnchorLabel(size_hint = NEW_QTY_L.hpair, text = 'Quantity',
        pos = NEW_QTY_L.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
        anchor_x = 'right', color = BLACK, halign = 'right')
    newWeight = TextInput(size_hint = NEW_WEIGHT.hpair, hint_text = 'Weight',
        pos = NEW_WEIGHT.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C)
    newWeight_L = AnchorLabel(size_hint = NEW_WEIGHT_L.hpair, text = 'Weight',
        pos = NEW_WEIGHT_L.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
        anchor_x = 'right', color = BLACK, halign = 'right')
    newVal = TextInput(size_hint = NEW_VAL.hpair, hint_text = 'Value',
        pos = NEW_VAL.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C)
    newVal_L = AnchorLabel(size_hint = NEW_VAL_L.hpair, text = 'Value',
        pos = NEW_VAL_L.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
        anchor_x = 'right', color = BLACK, halign = 'right')

    newTags = TextInput(size_hint = NEW_TAGS.hpair, hint_text = 'Tags',
        pos = NEW_TAGS.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C)
    newDesc = TextInput(size_hint = NEW_DESC.hpair, hint_text = 'Item description',
        pos = NEW_DESC.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C)

    newCancel = Button(size_hint = NEW_CANCEL.hpair, text = 'CANCEL',
        pos = NEW_CANCEL.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C)
    newSave = Button(size_hint = NEW_SAVE.hpair, text = 'SAVE',
        pos = NEW_SAVE.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C)
