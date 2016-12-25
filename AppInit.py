from SysFuncs import *
from LoadSaves import *
from Bag import *
from BagItem import *

scale = (2)
#=======================================================================================#
# SYSTEM VARIABLES                                                                      #
#=======================================================================================#
if True:
    # Stylization =======================================================================
    FONT_SIZE_A = 16
    FONT_SIZE_B = 8
    FONT_BASK = 'fonts/BASKVILLE.TTF'

    # Sizes =============================================================================
    APP_W = 1080 / scale
    APP_H = 1920 / scale
    FRAME = SizeMap(1080, 1920, (APP_W, APP_H))

    # MAIN
    MENU = SizeMap(1040, 180, FRAME.sizePair)
    MENU_BTN = SizeMap(172, 172, MENU.sizePair)
    MENU_TITLE = SizeMap(560, 80, MENU.sizePair)

    TABS = SizeMap(1050, 125, FRAME.sizePair)
    TABS_BTN = SizeMap(342, 120, TABS.sizePair)
    TABS_BTN_MID = SizeMap(345, 120, TABS.sizePair)
    TABS_PICK = SizeMap(350, 125, TABS.sizePair)

    CONT = SizeMap(1040, 1560, FRAME.sizePair)
    CONT_SPACE = SizeMap(0, 5, CONT.sizePair)
    CONT_PAD = SizeMap(2, 5, CONT.sizePair)

    # ITEMS
    LISTITEM = SizeMap(1030, 200, CONT.sizePair)

    # NEW
    NEW_TEXT_BIG = SizeMap(980, 105, CONT.sizePair)
    NEW_ICON = SizeMap(395, 395, CONT.sizePair)
    NEW_TEXT_SMALL = SizeMap(545, 105, CONT.sizePair)
    NEW_DESC = SizeMap(980, 605, CONT.sizePair)
    NEW_BTN = SizeMap(520, 150, CONT.sizePair)

    # Positions =========================================================================
    # SCREENS
    SCREEN_POS_ON = ZEROS
    SCREEN_POS_OFF = (APP_W, 0)
    # MAIN
    MENU_POS = (20 / scale, 1720 / scale)
    MENU_TITLE_POS = (260 / scale, 1723 / scale)
    MENU_BTN_BAG_POS = (5 / scale, 5 / scale)
    MENU_BTN_OPTS_POS = (865 / scale, 5 / scale)

    TABS_POS = (15 / scale, 1588 / scale)
    PICK_POS_A = (0 / scale, 0 / scale)
    PICK_POS_B = (349 / scale, 0 / scale)
    PICK_POS_C = (700 / scale, 0 / scale)
    TAB_POS_A = (5 / scale, 2 / scale)
    TAB_POS_B = (352 / scale, 2 / scale)
    TAB_POS_C = (702 / scale, 2 / scale)

    CONT_POS = (20 / scale, 20 / scale)
    CONT_POS_R = (1080 / scale, 20 / scale)
    CONT_POS_L = (-1080 / scale, 20 / scale)

    # NEW
    NEW_NAME_POS = (30 / scale, 1415 / scale)
    NEW_ICON_POS = (30 / scale, 980 / scale)
    NEW_QTY_POS = (465 / scale, 1270 / scale)
    NEW_WEIGHT_POS = (465 / scale, 1125 / scale)
    NEW_VAL_POS = (465 / scale, 980 / scale)
    NEW_TAGS_POS = (30 / scale, 835 / scale)
    NEW_DESC_POS = (30 / scale, 190 / scale)
    NEW_CANCEL_POS = (0 / scale, 0 / scale)
    NEW_SAVE_POS = (520 / scale, 0 / scale)

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
    menu = RelativeLayout(pos = MENU_POS, size_hint = MENU.hSizePair)
    menu_Title = Label(size_hint = MENU_TITLE.hSizePair, pos = MENU_TITLE_POS,
        font_name = FONT_BASK, font_size = FONT_SIZE_A, color = [1,1,1,1])
    menu_Btn_Bag = Button(size_hint = MENU_BTN.hSizePair, pos = MENU_BTN_BAG_POS,
        background_color = [0,0,0,0])
    menu_Btn_Opts = Button(size_hint = MENU_BTN.hSizePair, pos = MENU_BTN_OPTS_POS,
        background_color = [0,0,0,0])

    # Tabs
    tabs = RelativeLayout(pos = TABS_POS, size_hint = TABS.hSizePair)
    tabs_Pick = Image(size_hint = TABS_PICK.hSizePair, pos = PICK_POS_A,
        source = 'images/IMG_FRAME.png')
    tabs_Items = Button(size_hint = TABS_BTN.hSizePair, pos = TAB_POS_A,
        background_color = [0,0,0,0])
    tabs_Filter = Button(size_hint = TABS_BTN_MID.hSizePair, pos = TAB_POS_B,
        text_size = NONES, background_color = [0,0,0,0])
    tabs_New = Button(size_hint = TABS_BTN.hSizePair, pos = TAB_POS_C,
        background_color = [0,0,0,0])

    # Content Panes
    contpane_items = RelativeLayout(pos = CONT_POS, size_hint = CONT.hSizePair)
    contpane_new = RelativeLayout(pos = CONT_POS_R, size_hint = CONT.hSizePair)

    # Items Content
    cont_Scroll = ScrollView(size_hint = FILLS, do_scroll_x = False, bar_width = 0)
    cont_List = GridLayout(size_hint = (1.0, 0), cols = 1,
        padding = list(CONT_PAD.sizePair), spacing = list(CONT_SPACE.sizePair),
        row_default_height = LISTITEM.h / scale, row_force_default = True)


    # NEW ITEM WIDGETS
    # Input Fields
    new_name = TextInput(size_hint = NEW_TEXT_BIG.hSizePair, hint_text = 'Name',
        pos = NEW_NAME_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)

    new_icon = Image(size_hint = NEW_ICON.hSizePair, source = 'images/blankIcon.png',
        pos = NEW_ICON_POS, allow_stretch = True, keep_ratio = False)

    new_qty = TextInput(size_hint = NEW_TEXT_SMALL.hSizePair, hint_text = 'Quantity',
        pos = NEW_QTY_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_weight = TextInput(size_hint = NEW_TEXT_SMALL.hSizePair, hint_text = 'Weight',
        pos = NEW_WEIGHT_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_val = TextInput(size_hint = NEW_TEXT_SMALL.hSizePair, hint_text = 'Value',
        pos = NEW_VAL_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)

    new_tags = TextInput(size_hint = NEW_TEXT_BIG.hSizePair, hint_text = 'Tags',
        pos = NEW_TAGS_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_desc = TextInput(size_hint = NEW_DESC.hSizePair, hint_text = 'Item description',
        pos = NEW_DESC_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)

    new_cancel = Button(size_hint = NEW_BTN.hSizePair, text = 'CANCEL',
        pos = NEW_CANCEL_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
    new_save = Button(size_hint = NEW_BTN.hSizePair, text = 'SAVE',
        pos = NEW_SAVE_POS, font_name = FONT_BASK, font_size = FONT_SIZE_A)
