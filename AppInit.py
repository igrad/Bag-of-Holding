from SysFuncs import *
from LoadSaves import *
from Bag import *
from BagItem import *

#=======================================================================================#
# SYSTEM VARIABLES                                                                      #
#=======================================================================================#
if True:
    # Stylization =======================================================================
    FONT_SIZE_A = 32
    FONT_SIZE_B = 20
    FONT_BASK = 'fonts/BASKVILLE.TTF'

    # Sizes =============================================================================
    APP_W = 1080 / SCALE
    APP_H = 1920 / SCALE
    FRAME = SizeMap(0, 0, 1080, 1920, (APP_W, APP_H))

    # MAIN
    MENU = SizeMap(20, 1720, 1040, 180, FRAME.pair)
    MENU_BTN_BAG = SizeMap(5, 5, 172, 172, MENU.pair)
    MENU_BTN_OPTS = SizeMap(865, 5, 172, 172, MENU.pair)
    MENU_TITLE = SizeMap(260, 1723, 560, 80, MENU.pair)

    TABS = SizeMap(15, 1588, 1050, 125, FRAME.pair)
    TABS_BTN = SizeMap(0, 0, 342, 120, TABS.pair)
    TABS_BTN_MID = SizeMap(0, 0, 345, 120, TABS.pair)
    TABS_PICK = SizeMap(0, 0, 350, 125, TABS.pair)

    CONT = SizeMap(20, 20, 3120, 1560, FRAME.pair)
    CONTPANE = SizeMap(0, 0, 1040, 1560, CONT.pair)
    CONT_SPACE = SizeMap(0, 0, 0, 5, CONT.pair)
    CONT_PAD = SizeMap(0, 0, 2, 5, CONT.pair)

    # ITEMS
    LISTITEM = SizeMap(0, 0, 1030, 200, CONTPANE.pair)

    # FILTER
    FILT_NAME = SizeMap(30, 1415, 980, 105, CONTPANE.pair)
    FILT_CATLBL = SizeMap(30, 1270, 300, 105, CONTPANE.pair)
    FILT_CAT = SizeMap(370, 1270, 400, 105, CONTPANE.pair)
    FILT_SORTLBL = SizeMap(30, 1125, 300, 105, CONTPANE.pair)
    FILT_SORT = SizeMap(370, 1125, 400, 105, CONTPANE.pair)
    FILT_TAGSLBL = SizeMap(30, 980, 980, 105, CONTPANE.pair)
    FILT_TAGS = SizeMap(30, 835, 980, 605, CONTPANE.pair)

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
    PICK_POS_A = (0 / SCALE, 0 / SCALE)
    PICK_POS_B = (349 / SCALE, 0 / SCALE)
    PICK_POS_C = (700 / SCALE, 0 / SCALE)
    TAB_POS_A = (5 / SCALE, 2 / SCALE)
    TAB_POS_B = (352 / SCALE, 2 / SCALE)
    TAB_POS_C = (702 / SCALE, 2 / SCALE)

    CONT_POS_ITEMS = (20 / SCALE, 20 / SCALE)
    CONT_POS_FILTERS = (-1 * CONT.w + (20 / SCALE), 20 / SCALE)
    CONT_POS_NEW = (-2 * CONT.w + (20 / SCALE), 20 / SCALE)

    #CONT_POS_R = (1080 / SCALE, 20 / SCALE)
    #CONT_POS_L = (-1080 / SCALE, 20 / SCALE)
    CONTPANE_POS_A = (0, 0)
    CONTPANE_POS_B = (CONT.w, 0)
    CONTPANE_POS_C = (2 * CONT.w, 0)


#=======================================================================================#
# APP WIDGETS                                                                           #
#=======================================================================================#
if True:
    # FRAME
    BG = Image(size_hint = FILLS, source = 'images/IMG_MAIN_BG.png')
    Border = Image(size_hint = FILLS, source = 'images/IMG_MAIN_BORDER.png')


    # SCREENS
    screen_main = RelativeLayout(pos = SCREEN_POS_ON, size_hint = FILLS)
    screen_settings = RelativeLayout(pos = SCREEN_POS_OFF, size_hint = FILLS)


    # Menu
    menu = RelativeLayout(pos = MENU.pos, size_hint = MENU.hpair)
    menu_Title = Label(size_hint = MENU_TITLE.hpair, pos = MENU_TITLE.pos,
        font_name = FONT_BASK, font_size = FONT_SIZE_A, color = [1,1,1,1])
    menu_Btn_Bag = Button(size_hint = MENU_BTN_BAG.hpair, pos = MENU_BTN_BAG.pos,
        background_color = [0,0,0,0])
    menu_Btn_Opts = Button(size_hint = MENU_BTN_OPTS.hpair, pos = MENU_BTN_OPTS.pos,
        background_color = [0,0,0,0])

    # Tabs
    tabs = RelativeLayout(pos = TABS.pos, size_hint = TABS.hpair)
    tabs_Pick = Image(size_hint = TABS_PICK.hpair, pos = PICK_POS_A,
        source = 'images/IMG_FRAME.png')
    tabs_Items = Button(size_hint = TABS_BTN.hpair, pos = TAB_POS_A,
        background_color = [0,0,0,0])
    tabs_Filter = Button(size_hint = TABS_BTN_MID.hpair, pos = TAB_POS_B,
        text_size = NONES, background_color = [0,0,0,0])
    tabs_New = Button(size_hint = TABS_BTN.hpair, pos = TAB_POS_C,
        background_color = [0,0,0,0])

    # Content Panes
    contpane = RelativeLayout(pos = CONT.pos, size_hint = CONT.hpair)
    contpane_items = RelativeLayout(pos = CONTPANE_POS_A, size_hint = CONTPANE.hpair)
    contpane_filters = RelativeLayout(pos = CONTPANE_POS_B, size_hint = CONTPANE.hpair)
    contpane_new = RelativeLayout(pos = CONTPANE_POS_C, size_hint = CONTPANE.hpair)

    # Items Content
    cont_Scroll = ScrollView(size_hint = FILLS, do_scroll_x = False, bar_width = 0)
    cont_List = GridLayout(size_hint = (1.0, 0), cols = 1,
        padding = list(CONT_PAD.pair), spacing = list(CONT_SPACE.pair),
        row_default_height = LISTITEM.h / SCALE, row_force_default = True)


    # FILTERS ITEM WIDGETS
    filt_name = TextInput(size_hint = FILT_NAME.hpair, hint_text = 'Item name includes',
        pos = FILT_NAME.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_catlbl = Label(size_hint = FILT_CATLBL.hpair, text = 'Sort by',
        pos = FILT_CATLBL.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_cat = DropDown(size_hint = FILT_CAT.hpair, pos = FILT_CAT.pos)
    filt_cat_name = Button(size_hint = FILT_CAT.hpair, text = 'name',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_cat_qty = Button(size_hint = FILT_CAT.hpair, text = 'quantity',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_cat_weight = Button(size_hint = FILT_CAT.hpair, text = 'weight',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_cat_val = Button(size_hint = FILT_CAT.hpair, text = 'value',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_sortlbl = Label(size_hint = FILT_SORTLBL.hpair, text = 'Sort type',
        pos = FILT_SORTLBL.pos, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_sort = DropDown(size_hint = FILT_SORT.hpair, pos = FILT_SORT.pos)
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
        row_default_height = FILT_TAGSLBL.h / SCALE)



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
