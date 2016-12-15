from SysFuncs import *
from Bag import *
from BagItem import *
from SaveStores import *

#=======================================================================================#
# SYSTEM VARIABLES                                                                      #
#=======================================================================================#
if True:
    # Stylization
    FONT_SIZE_A = 16
    FONT_SIZE_B = 8
    FONT_BASK = 'fonts/BASKVILLE.TTF'

    # Sizes
    NONES = (None, None)
    ZEROS = (0.0, 0.0)
    FILLS = (1.0, 1.0)

    APP_W = 1080
    APP_H = 1920
    FRAME = SizeMap(1080, 1920, (APP_W, APP_H))

    MENU = SizeMap(1040, 180, FRAME.sizePair)
    MENU_BTN = SizeMap(172, 172, MENU.sizePair)
    MENU_TITLE = SizeMap(560, 80, MENU.sizePair)

    TABS = SizeMap(1050, 125, FRAME.sizePair)
    TABS_BTN = SizeMap(342, 120, TABS.sizePair)
    TABS_BTN_MID = SizeMap(345, 120, TABS.sizePair)
    TABS_PICK = SizeMap(350, 125, TABS.sizePair)

    CONT = SizeMap(1040, 1560, FRAME.sizePair)
    LISTITEM = SizeMap(1030, 172, CONT.sizePair)

    # Positions
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

#=======================================================================================#
# APP WIDGETS                                                                           #
#=======================================================================================#
if True:
    # SYSTEM
    CURRENTBAG = 0


    # FRAME
    BG = Image(size_hint = FILLS, source = 'images/IMG_MAIN_BG.png')
    Border = Image(size_hint = FILLS, source = 'images/IMG_MAIN_BORDER.png')


    # MAIN WIDGETS
    screen_main = RelativeLayout(pos = ZEROS, size_hint = NONES, size = FRAME.sizePair)

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

    cont = RelativeLayout(pos = CONT_POS, size_hint = CONT.hSizePair)
    cont_Scroll = ScrollView(size_hint = FILLS, do_scroll_x = False, bar_width = 0)
    cont_List = GridLayout(size_hint = LISTITEM.hSizePair, cols = 1,
                           row_force_default = True, row_default_height = 172,
                           spacing = [0, 5], padding = [5, 0])


    # NEW ITEM WIDGETS
    screen_new = RelativeLayout(pos = ZEROS, size_hint = FRAME.hSizePair)

    # Input Fields
    new_name = TextInput(size_hint = NONES, size = (1030, 60), hint_text = 'Name')
    new_icon = Image(size_hint = )
