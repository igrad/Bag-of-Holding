from SysFuncs import *
from LoadSaves import *
from Bag import *
from BagItem import *

SCALE = 2

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
    FRAME = SizeMap(1080, 1920, (APP_W, APP_H))

    # MAIN
    MENU = SizeMap(1040, 180, FRAME.pair)
    MENU_BTN = SizeMap(172, 172, MENU.pair)
    MENU_TITLE = SizeMap(560, 80, MENU.pair)

    TABS = SizeMap(1050, 125, FRAME.pair)
    TABS_BTN = SizeMap(342, 120, TABS.pair)
    TABS_BTN_MID = SizeMap(345, 120, TABS.pair)
    TABS_PICK = SizeMap(350, 125, TABS.pair)

    CONT = SizeMap(1040, 1560, FRAME.pair)
    CONT_SPACE = SizeMap(0, 5, CONT.pair)
    CONT_PAD = SizeMap(2, 5, CONT.pair)

    # ITEMS
    LISTITEM = SizeMap(1030, 200, CONT.pair)

    # FILTER
    FILT_NAME = SizeMap(980, 105, CONT.pair)
    FILT_CATLBL = SizeMap(300, 105, CONT.pair)
    FILT_CAT = SizeMap(400, 105, CONT.pair)
    FILT_SORTLBL = SizeMap(300, 105, CONT.pair)
    FILT_SORT = SizeMap(400, 105, CONT.pair)
    FILT_TAGSLBL = SizeMap(980, 105, CONT.pair)
    FILT_TAGS = SizeMap(980, 605, CONT.pair)

    # NEW
    NEW_TEXT_BIG = SizeMap(980, 105, CONT.pair)
    NEW_ICON = SizeMap(395, 395, CONT.pair)
    NEW_TEXT_SMALL = SizeMap(545, 105, CONT.pair)
    NEW_DESC = SizeMap(980, 605, CONT.pair)
    NEW_BTN = SizeMap(520, 150, CONT.pair)

    # Positions =========================================================================
    # SCREENS
    SCREEN_POS_ON = ZEROS
    SCREEN_POS_OFF = (APP_W, 0)
    # MAIN
    MENU_POS = (20 / SCALE, 1720 / SCALE)
    MENU_TITLE_POS = (260 / SCALE, 1723 / SCALE)
    MENU_BTN_BAG_POS = (5 / SCALE, 5 / SCALE)
    MENU_BTN_OPTS_POS = (865 / SCALE, 5 / SCALE)

    TABS_POS = (15 / SCALE, 1588 / SCALE)
    PICK_POS_A = (0 / SCALE, 0 / SCALE)
    PICK_POS_B = (349 / SCALE, 0 / SCALE)
    PICK_POS_C = (700 / SCALE, 0 / SCALE)
    TAB_POS_A = (5 / SCALE, 2 / SCALE)
    TAB_POS_B = (352 / SCALE, 2 / SCALE)
    TAB_POS_C = (702 / SCALE, 2 / SCALE)

    CONT_POS = (20 / SCALE, 20 / SCALE)
    CONT_POS_R = (1080 / SCALE, 20 / SCALE)
    CONT_POS_L = (-1080 / SCALE, 20 / SCALE)

    # FILTER
    FILT_NAME_POS = (30 / SCALE, 1415 / SCALE)
    FILT_CATLBL_POS = (30 / SCALE, 1270 / SCALE)
    FILT_CAT_POS = (370 / SCALE, 1270 / SCALE)
    FILT_SORTLBL_POS = (30 / SCALE, 1125 / SCALE)
    FILT_SORT_POS = (370 / SCALE, 1125 / SCALE)
    FILT_TAGS_POS = (30 / SCALE, 980 / SCALE)
    FILT_TAGSREAD_POS = (30 / SCALE, 835 / SCALE)

    # NEW
    NEW_NAME_POS = (30 / SCALE, 1415 / SCALE)
    NEW_ICON_POS = (30 / SCALE, 980 / SCALE)
    NEW_QTY_POS = (465 / SCALE, 1270 / SCALE)
    NEW_WEIGHT_POS = (465 / SCALE, 1125 / SCALE)
    NEW_VAL_POS = (465 / SCALE, 980 / SCALE)
    NEW_TAGS_POS = (30 / SCALE, 835 / SCALE)
    NEW_DESC_POS = (30 / SCALE, 190 / SCALE)
    NEW_CANCEL_POS = (0 / SCALE, 0 / SCALE)
    NEW_SAVE_POS = (520 / SCALE, 0 / SCALE)

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
    menu = RelativeLayout(pos = MENU_POS, size_hint = MENU.hpair)
    menu_Title = Label(size_hint = MENU_TITLE.hpair, pos = MENU_TITLE_POS,
        font_name = FONT_BASK, font_size = FONT_SIZE_A, color = [1,1,1,1])
    menu_Btn_Bag = Button(size_hint = MENU_BTN.hpair, pos = MENU_BTN_BAG_POS,
        background_color = [0,0,0,0])
    menu_Btn_Opts = Button(size_hint = MENU_BTN.hpair, pos = MENU_BTN_OPTS_POS,
        background_color = [0,0,0,0])

    # Tabs
    tabs = RelativeLayout(pos = TABS_POS, size_hint = TABS.hpair)
    tabs_Pick = Image(size_hint = TABS_PICK.hpair, pos = PICK_POS_A,
        source = 'images/IMG_FRAME.png')
    tabs_Items = Button(size_hint = TABS_BTN.hpair, pos = TAB_POS_A,
        background_color = [0,0,0,0])
    tabs_Filter = Button(size_hint = TABS_BTN_MID.hpair, pos = TAB_POS_B,
        text_size = NONES, background_color = [0,0,0,0])
    tabs_New = Button(size_hint = TABS_BTN.hpair, pos = TAB_POS_C,
        background_color = [0,0,0,0])

    # Content Panes
    contpane_items = RelativeLayout(pos = CONT_POS, size_hint = CONT.hpair)
    contpane_new = RelativeLayout(pos = CONT_POS_R, size_hint = CONT.hpair)

    # Items Content
    cont_Scroll = ScrollView(size_hint = FILLS, do_scroll_x = False, bar_width = 0)
    cont_List = GridLayout(size_hint = (1.0, 0), cols = 1,
        padding = list(CONT_PAD.pair), spacing = list(CONT_SPACE.pair),
        row_default_height = LISTITEM.h / SCALE, row_force_default = True)


    # FILTERS ITEM WIDGETS
    filt_name = TextInput(size_hint = FILT_NAME.hpair, hint_text = 'Item name includes',
        pos = FILT_NAME_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_catlbl = Label(size_hint = FILT_CATLBL.hpair, text = 'Sort by',
        pos = FILT_CATLBL_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_cat = DropDown(size_hint = FILT_CAT.hpair, pos = FILT_CAT_POS)
    filt_cat_name = Button(size_hint = FILT_CAT.hpair, text = 'name',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_cat_qty = Button(size_hint = FILT_CAT.hpair, text = 'quantity',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_cat_weight = Button(size_hint = FILT_CAT.hpair, text = 'weight',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_cat_qty = Button(size_hint = FILT_CAT.hpair, text = 'value',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_sortlbl = Label(size_hint = FILT_SORTLBL.hpair, text = 'Sort type',
        pos = FILT_SORTLBL_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_sort = DropDown(size_hint = FILT_SORT.hpair, pos = FILT_SORT_POS)
    filt_sort_asc = Button(size_hint = FILT_SORT.hpair, text = 'ascending',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_sort_des = Button(size_hint = FILT_SORT.hpair, text = 'descending',
        font_name = FONT_BASK, font_size = FONT_SIZE_A)
    filt_tagslbl = Label(size_hint = FILT_TAGSLBL.hpair, pos = FILT_TAGSLBL_POS,
        font_name = FONT_BASK, font_size = FONT_SIZE_A,
        text = 'Only show items with these tags:')
    filt_tags_scroll = ScrollView(size_hint = FILT_TAGS.hpair, pos = FILT_TAGS_POS,
        do_scroll_x = False, bar_width = 0)
    filt_tags = GridLayout(size_hint = (1.0, 0), cols = 1, padding = ZEROS,
        spacing = ZEROS, row_force_default = True,
        row_default_height = FILT_TAGSLBL.h / SCALE)



    # NEW ITEM WIDGETS
    new_name = TextInput(size_hint = NEW_TEXT_BIG.hpair, hint_text = 'Name',
        pos = NEW_NAME_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)

    new_icon = Image(size_hint = NEW_ICON.hpair, source = 'images/blankIcon.png',
        pos = NEW_ICON_POS, allow_stretch = True, keep_ratio = False)

    new_qty = TextInput(size_hint = NEW_TEXT_SMALL.hpair, hint_text = 'Quantity',
        pos = NEW_QTY_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_weight = TextInput(size_hint = NEW_TEXT_SMALL.hpair, hint_text = 'Weight',
        pos = NEW_WEIGHT_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_val = TextInput(size_hint = NEW_TEXT_SMALL.hpair, hint_text = 'Value',
        pos = NEW_VAL_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)

    new_tags = TextInput(size_hint = NEW_TEXT_BIG.hpair, hint_text = 'Tags',
        pos = NEW_TAGS_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_desc = TextInput(size_hint = NEW_DESC.hpair, hint_text = 'Item description',
        pos = NEW_DESC_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)

    new_cancel = Button(size_hint = NEW_BTN.hpair, text = 'CANCEL',
        pos = NEW_CANCEL_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_save = Button(size_hint = NEW_BTN.hpair, text = 'SAVE',
        pos = NEW_SAVE_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
