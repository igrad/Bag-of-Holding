from SysFuncs import *
from LoadSaves import *
from Bag import *
from BagItem import *
from modules.DropBtn import *

#=======================================================================================#
# SYSTEM VARIABLES                                                                      #
#=======================================================================================#
if True:
    # Stylization =======================================================================
    FONT_SIZE_A = 32
    FONT_SIZE_B = 20
    FONT_BASK = 'fonts/BASKVILLE.TTF'
    WHITE = [1,1,1,1]
    BLACK = [0,0,0,1]
    CLEAR = [0,0,0,0]

    # Sizes =============================================================================
    APP_W = 432 / XSCALE
    APP_H = 768 / YSCALE
    FRAME = SizeMap(0, 0, 432, 768, (APP_W, APP_H))

    # MAIN
    MENU = SizeMap(0, 671, 432, 98, FRAME.pair)
    MENU_BTN_BAG = SizeMap(19, 19, 72, 72, MENU.pair)
    MENU_BTN_OPTS = SizeMap(343, 19, 72, 72, MENU.pair)
    MENU_TITLE = SizeMap(153, 35, 128, 40, MENU.pair)

    TABS = SizeMap(0, 603, 432, 60, FRAME.pair)
    TABS_BTN = SizeMap(0, 0, 144, 60, TABS.pair)

    CONT = SizeMap(20, 20, 3120, 1560, FRAME.pair)
    CONTPANE = SizeMap(0, 0, 1040, 1560, CONT.pair)
    CONT_SPACE = SizeMap(0, 0, 0, 5, CONT.pair)
    CONT_PAD = SizeMap(0, 0, 2, 5, CONT.pair)

    # ITEMS
    LISTITEM = SizeMap(0, 0, 1030, 200, CONTPANE.pair)

    # FILTER
    FILT_NAME = SizeMap(30, 1415, 980, 105, CONTPANE.pair)
    FILT_CATLBL = SizeMap(30, 1270, 300, 105, CONTPANE.pair)
    FILT_CAT = SizeMap(370, 1270, 240, 60, CONTPANE.pair)
    FILT_SORTLBL = SizeMap(30, 1125, 300, 105, CONTPANE.pair)
    FILT_SORT = SizeMap(370, 1125, 400, 105, CONTPANE.pair)
    FILT_TAGSLBL = SizeMap(30, 980, 980, 105, CONTPANE.pair)
    FILT_TAGS = SizeMap(30, 835, 980, 205, CONTPANE.pair)

    # NEW
    NEW_NAME = SizeMap(30, 1415, 980, 105, CONTPANE.pair)
    NEW_ICON = SizeMap(30, 980, 395, 395, CONTPANE.pair)
    NEW_QTY = SizeMap(465, 1270, 545, 105, CONTPANE.pair)
    NEW_WEIGHT = SizeMap(465, 1125, 545, 105, CONTPANE.pair)
    NEW_VAL = SizeMap(465, 980, 545, 105, CONTPANE.pair)
    NEW_TAGS = SizeMap(30, 835, 980, 105, CONTPANE.pair)
    NEW_DESC = SizeMap(30, 190, 980, 605, CONTPANE.pair)
    NEW_CANCEL = SizeMap(0, 0, 520, 150, CONTPANE.pair)
    NEW_SAVE = SizeMap(520, 0, 520, 150, CONTPANE.pair)

    # Positions =========================================================================
    # SCREENS
    SCREEN_POS_ON = ZEROS
    SCREEN_POS_OFF = (APP_W, 0)

    # MAIN
    PICK_POS_A = (0 / XSCALE, 0 / YSCALE)
    PICK_POS_B = (349 / XSCALE, 0 / YSCALE)
    PICK_POS_C = (700 / XSCALE, 0 / YSCALE)
    TAB_POS_A = (5 / XSCALE, 2 / YSCALE)
    TAB_POS_B = (352 / XSCALE, 2 / YSCALE)
    TAB_POS_C = (702 / XSCALE, 2 / YSCALE)

    CONT_POS_ITEMS = (20 / XSCALE, 20 / YSCALE)
    CONT_POS_FILTERS = (-1 * CONT.w + (20 / XSCALE), 20 / YSCALE)
    CONT_POS_NEW = (-2 * CONT.w + (20 / XSCALE), 20 / YSCALE)

    CONTPANE_POS_A = (0, 0)
    CONTPANE_POS_B = (CONT.w, 0)
    CONTPANE_POS_C = (2 * CONT.w, 0)


#=======================================================================================#
# APP WIDGETS                                                                           #
#=======================================================================================#
if True:
    # FRAME
    BG = Image(size_hint = FILLS, source = 'images/IMG_MAIN.png')


    # SCREENS
    screen_main = RelativeLayout(pos = SCREEN_POS_ON, size_hint = FILLS)
    screen_settings = RelativeLayout(pos = SCREEN_POS_OFF, size_hint = FILLS)


    # Menu
    menu = RelativeLayout(pos = MENU.pos, size_hint = MENU.hpair)
    menu_Title = Label(size_hint = MENU_TITLE.hpair, pos = MENU_TITLE.pos,
        font_name = FONT_BASK, font_size = FONT_SIZE_A, color = [1,1,1,1])
    menu_Btn_Bag = Button(size_hint = MENU_BTN_BAG.hpair, pos = MENU_BTN_BAG.pos,
        background_color = CLEAR)
    menu_Btn_Opts = Button(size_hint = MENU_BTN_OPTS.hpair, pos = MENU_BTN_OPTS.pos,
        background_color = CLEAR)

    # Tabs
    tabs = BoxLayout(pos = TABS.pos, size_hint = TABS.hpair, orientation = 'horizontal')
    tabs_Sort = Button(size_hint = TABS_BTN.hpair, text = 'Sort', color = WHITE,
        font_name = FONT_BASK, font_size = FONT_SIZE_A, background_color = CLEAR)
    tabs_Filt = Button(size_hint = TABS_BTN.hpair, background_color = CLEAR)
    tabs_View = Button(size_hint = TABS_BTN.hpair, background_color = CLEAR)

    # Content Panes
    contpane = RelativeLayout(pos = CONT.pos, size_hint = CONT.hpair)
    contpane_items = RelativeLayout(pos = CONTPANE_POS_A, size_hint = CONTPANE.hpair)
    contpane_filters = RelativeLayout(pos = CONTPANE_POS_B, size_hint = CONTPANE.hpair)
    contpane_new = RelativeLayout(pos = CONTPANE_POS_C, size_hint = CONTPANE.hpair)

    # Items Content
    cont_Scroll = ScrollView(size_hint = FILLS, do_scroll_x = False, bar_width = 0)
    cont_List = GridLayout(size_hint = (1.0, 0), cols = 1,
        padding = list(CONT_PAD.pair), spacing = list(CONT_SPACE.pair),
        row_default_height = LISTITEM.h / YSCALE, row_force_default = True)


    # FILTERS ITEM WIDGETS
    filt_name = TextInput(size_hint = FILT_NAME.hpair, hint_text = 'Item name includes',
        pos = FILT_NAME.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_catlbl = Label(size_hint = FILT_CATLBL.hpair, text = 'Sort by',
        pos = FILT_CATLBL.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_cat = DropBtn(sizeMap = CONTPANE, head_sizeMap = FILT_CAT, head_text = 'name',
        btn_bg = 'images/filtbtnbg.png', btn_font_name = FONT_BASK,
        btn_font_color = [0,0,1,1], btn_font_size = FONT_SIZE_A, btn_height = FILT_CAT.hh,
        drop_direction = 'below', drop_max_height = 900,
        drop_anim_open = {'duration': 0.30, 't': 'in_quad'},
        drop_anim_close = {'duration': 0.30, 't': 'out_quad'},
        options = ['name', 'quantity', 'weight', 'value'])
    filt_sortlbl = Label(size_hint = FILT_SORTLBL.hpair, text = 'Sort type',
        pos = FILT_SORTLBL.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_sort = DropDown(size_hint = ZEROS)
    filt_sort_pick = Button(size_hint = FILT_SORT.hpair, text = 'sort pick',
        pos = FILT_SORT.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_sort_asc = Button(size_hint = FILT_SORT.hpair, text = 'ascending',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_sort_des = Button(size_hint = FILT_SORT.hpair, text = 'descending',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_tagslbl = Label(size_hint = FILT_TAGSLBL.hpair, pos = FILT_TAGSLBL.pos,
        font_name = FONT_BASK, font_size = FONT_SIZE_A,
        text = 'Only show items with these tags:')
    filt_tags_scroll = ScrollView(size_hint = FILT_TAGS.hpair, pos = FILT_TAGS.pos,
        do_scroll_x = False, bar_width = 0)
    filt_tags = GridLayout(size_hint = (1.0, 0), cols = 1, padding = ZEROS,
        spacing = ZEROS, row_force_default = True,
        row_default_height = FILT_TAGSLBL.h / YSCALE)


    # NEW ITEM WIDGETS
    new_name = TextInput(size_hint = NEW_NAME.hpair, hint_text = 'Name',
        pos = NEW_NAME.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)

    new_icon = Image(size_hint = NEW_ICON.hpair, source = 'images/blankIcon.png',
        pos = NEW_ICON.pos, allow_stretch = True, keep_ratio = False)

    new_qty = TextInput(size_hint = NEW_QTY.hpair, hint_text = 'Quantity',
        pos = NEW_QTY.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_weight = TextInput(size_hint = NEW_WEIGHT.hpair, hint_text = 'Weight',
        pos = NEW_WEIGHT.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_val = TextInput(size_hint = NEW_VAL.hpair, hint_text = 'Value',
        pos = NEW_VAL.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)

    new_tags = TextInput(size_hint = NEW_TAGS.hpair, hint_text = 'Tags',
        pos = NEW_TAGS.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_desc = TextInput(size_hint = NEW_DESC.hpair, hint_text = 'Item description',
        pos = NEW_DESC.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)

    new_cancel = Button(size_hint = NEW_CANCEL.hpair, text = 'CANCEL',
        pos = NEW_CANCEL.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_save = Button(size_hint = NEW_SAVE.hpair, text = 'SAVE',
        pos = NEW_SAVE.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
