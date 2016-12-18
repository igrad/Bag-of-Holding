from SysFuncs import *
from Bag import *
from BagItem import *
from SaveStores import *

#=======================================================================================#
# SYSTEM VARIABLES                                                                      #
#=======================================================================================#
if True:
    # Stylization =======================================================================
    FONT_SIZE_A = 16
    FONT_SIZE_B = 8
    FONT_BASK = 'fonts/BASKVILLE.TTF'

    # Sizes =============================================================================
    APP_W = 1080
    APP_H = 1920
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

    # ITEMS
    LISTITEM = SizeMap(1030, 172, CONT.sizePair)

    # NEW
    NEW_TEXT_BIG = SizeMap(980, 105, CONT.sizePair)
    NEW_ICON = SizeMap(395, 395, CONT.sizePair)
    NEW_TEXT_SMALL = SizeMap(545, 105, CONT.sizePair)
    NEW_DESC = SizeMap(980, 605, CONT.sizePair)
    NEW_BTN = SizeMap(520, 150, CONT.sizePair)

    # Positions =========================================================================
    # MAIN
    MENU_POS = (20, 1720)
    MENU_TITLE_POS = (260, 1723)
    MENU_BTN_BAG_POS = (5, 5)
    MENU_BTN_OPTS_POS = (865, 5)

    TABS_POS = (15, 1588)
    PICK_POS_A = (0, 0)
    PICK_POS_B = (349, 0)
    PICK_POS_C = (700, 0)
    TAB_POS_A = (5, 2)
    TAB_POS_B = (352, 2)
    TAB_POS_C = (702, 2)

    CONT_POS = (20, 20)
    CONT_POS_R = (1080, 20)
    CONT_POS_L = (-1080, 20)

    # NEW
    NEW_NAME_POS = (30, 1415)
    NEW_ICON_POS = (30, 980)
    NEW_QTY_POS = (465, 1270)
    NEW_WEIGHT_POS = (465, 1125)
    NEW_VAL_POS = (465, 980)
    NEW_TAGS_POS = (30, 835)
    NEW_DESC_POS = (30, 190)
    NEW_CANCEL_POS = (0, 0)
    NEW_SAVE_POS = (520, 0)

#=======================================================================================#
# APP WIDGETS                                                                           #
#=======================================================================================#
if True:
    # SYSTEM
    CURRENTBAG = 0


    # FRAME
    BG = Image(size_hint = FILLS, source = 'images/IMG_MAIN_BG.png')
    Border = Image(size_hint = FILLS, source = 'images/IMG_MAIN_BORDER.png')


    # SCREENS
    screen_main = RelativeLayout(pos = ZEROS, size_hint = FILLS, size = FRAME.sizePair)
    screen_settings = RelativeLayout(pos = screen_main.x, size_hint = FILLS,
        size = FRAME.sizePair)


    # Menu
    menu = RelativeLayout(pos = MENU_POS, size_hint = MENU.hSizePair)
    menu_Title = Label(size_hint = MENU_TITLE.hSizePair, pos = MENU_TITLE_POS,
        font_name = FONT_BASK, font_size = FONT_SIZE_A, color = [0,0,0,1])
    menu_Btn_Bag = Button(size_hint = MENU_BTN.hSizePair, pos = MENU_BTN_BAG_POS,
        background_color = [0,0,0,0.5])
    menu_Btn_Opts = Button(size_hint = MENU_BTN.hSizePair, pos = MENU_BTN_OPTS_POS,
        background_color = [0,0,0,0.5])

    # Tabs
    tabs = RelativeLayout(pos = TABS_POS, size_hint = TABS.hSizePair)
    tabs_Pick = Image(size_hint = TABS_PICK.hSizePair, pos = PICK_POS_A,
        source = 'images/IMG_FRAME.png')
    tabs_Items = Button(size_hint = TABS_BTN.hSizePair, pos = TAB_POS_A,
        background_color = [0,0,0,0.5])
    tabs_Filter = Button(size_hint = TABS_BTN_MID.hSizePair, pos = TAB_POS_B,
        text_size = NONES, background_color = [0,0,0,0.5])
    tabs_New = Button(size_hint = TABS_BTN.hSizePair, pos = TAB_POS_C,
        background_color = [0,0,0,0.5])

    # Content Panes
    contpane_items = RelativeLayout(pos = CONT_POS, size_hint = CONT.hSizePair)
    contpane_new = RelativeLayout(pos = CONT_POS_R, size_hint = CONT.hSizePair)

    # Items Content
    cont_Scroll = ScrollView(size_hint = FILLS, do_scroll_x = False, bar_width = 0)
    cont_List = GridLayout(size_hint = LISTITEM.hSizePair, cols = 1,
        row_force_default = True, row_default_height = 172, spacing = [0, 5],
        padding = [5, 0])


    # NEW ITEM WIDGETS
    screen_new = RelativeLayout(pos = ZEROS, size_hint = FRAME.hSizePair)

    # Input Fields
    new_name = TextInput(size_hint = NEW_TEXT_BIG.hSizePair, hint_text = 'Name',
        pos = NEW_NAME_POS, font_name = BASKVILLE, font_size = FONT_SIZE_B)
    new_icon = Image(size_hint = NEW_ICON.hSizePair, source = 'images/blankIcon.png',
        pos = NEW_ICON_POS, allow_stretch = True, keep_ratio = False)
    new_qty = TextInput(size_hint = NEW_TEXT_SMALL.hSizePair, hint_text = 'Quantity',
        pos = NEW_QTY_POS, font_name = BASKVILLE, font_size = FONT_SIZE_B)
    new_weight = TextInput(size_hint = NEW_TEXT_SMALL.hSizePair, hint_text = 'Weight',
        pos = NEW_WEIGHT_POS, font_name = BASKVILLE, font_size = FONT_SIZE_B)
    new_val = TextInput(size_hint = NEW_TEXT_SMALL.hSizePair, hint_text = 'Value',
        pos = NEW_VAL_POS, font_name = BASKVILLE, font_size = FONT_SIZE_B)
