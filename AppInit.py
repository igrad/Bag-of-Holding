from SysFuncs import *
from LoadSaves import *
from Bag import *
from BagItem import *
from AnchorLabel import *

# Stylization =======================================================================
MAX = max(XSCALE, YSCALE)
FONT_SIZE_A = 32/MAX
FONT_SIZE_B = 20/MAX
FONT_SIZE_C = 16/MAX
FONT_SIZE_D = 24/MAX
FONT_SIZE_HEAD = 48/MAX
FONT_BASK = 'fonts/BASKVILLE.TTF'
WHITE = [1,1,1,1]
BLACK = [0,0,0,1]
CLEAR = [0,0,0,0]

VIEW_CHECK_ACTIVE = 'images/IMG_VIEW_CHECK_ACTIVE.png'
VIEW_CHECK_INACTIVE = 'images/IMG_VIEW_CHECK_INACTIVE.png'
IMG_CLEAR = 'images/IMG_CLEAR.png'
IMG_BLACK = 'images/IMG_BLACK.png'
IMG_WHITE = 'images/IMG_WHITE.png'

# Sizes =============================================================================
APP_W = 432/XSCALE
APP_H = 768/YSCALE
FRAME = SizeMap(0, 0, 432, 768, (APP_W, APP_H))

# MAIN
MENU = SizeMap(0, 670, 432, 98, FRAME.pair)
MENU_BTN_BAG = SizeMap(18, 18, 72, 72, MENU.pair)
MENU_BTN_OPTS = SizeMap(342, 18, 72, 72, MENU.pair)
MENU_TITLE = SizeMap(153, 34, 128, 40, MENU.pair)

TABS = SizeMap(0, 602, 432, 60, FRAME.pair)
TABS_BTN = SizeMap(0, 0, 144, 60, TABS.pair)

SEARCH = SizeMap(11, 563, 326, 34, FRAME.pair)
SEARCH_INPUT = SizeMap(34, 0, 284, 34, SEARCH.pair)

CONT = SizeMap(0, 0, 432, 557, FRAME.pair)
CONT_SPACE = SizeMap(0, 0, 0, 5, CONT.pair)
CONT_PAD = SizeMap(0, 0, 2, 2, CONT.pair)
CONT_SCROLL = SizeMap(0, 0, 12, 0, CONT.pair)

# SELECTED ITEM
# Note: spacing should be (20, 20, 392, 516)
PICK = SizeMap(0, 105, 432, 557, FRAME.pair)
PICK_HALT = SizeMap(0, -105, 432, 768, PICK.pair)
PICK_NAME = SizeMap(20, 476, 392, 40, PICK.pair)
PICK_ICON = SizeMap(138, 316, 156, 156, PICK.pair)
PICK_MISC = SizeMap(21, 287, 390, 27, PICK.pair)
PICK_QTY = SizeMap(0, 0, 130, 27, PICK.pair)
PICK_WEIGHT = SizeMap(0, 1, 390, 27, PICK_MISC.pair)
PICK_VAL = SizeMap(0, 0, 130, 27, PICK.pair)
PICK_TAGS = SizeMap(20, 256, 392, 27, PICK.pair)
PICK_DESC = SizeMap(20, 20, 392, 232, PICK.pair)
PICK_OPTS = SizeMap(8, 550, 26, 26, PICK.pair)
PICK_X = SizeMap(396, 550, 26, 26, PICK.pair)

ICON = SizeMap(36, 105, 360, 556, FRAME.pair)
ICON_HALT = SizeMap(-36, -105, 432, 768, ICON.pair)
ICON_SCROLL = SizeMap(20, 60, 320, 476, ICON.pair)
ICON_BAR = SizeMap(0, 0, 4, 0, ICON_SCROLL.pair)
ICON_GRID = SizeMap(0, 0, 320, 476, ICON_SCROLL.pair)
ICON_PAD = SizeMap(16, 16, 90, 90, ICON_SCROLL.pair)
ICON_SPACE = SizeMap(0, 0, 90, 16, ICON_SCROLL.pair)
ICON_HEIGHT = SizeMap(0, 0, 80, 80, ICON_SCROLL.pair)
ICON_CANCEL = SizeMap(20, 20, 156, 32, ICON.pair)
ICON_SAVE = SizeMap(184, 20, 156, 32, ICON.pair)

# DROP MENUS
DROP_NEW = SizeMap(0, 174, 422, 496, FRAME.pair)
DROP_SORT = SizeMap(140, 414, 288, 256, FRAME.pair)
DROP_VIEW = SizeMap(148, 414, 284, 256, FRAME.pair)
DROP_NEW_HALT = SizeMap(4, 8, 408, 420, DROP_NEW.pair)
DROP_SORT_HALT = SizeMap(8, 8, 272, 180, DROP_SORT.pair)
DROP_VIEW_HALT = SizeMap(8, 8, 272, 180, DROP_VIEW.pair)

# ITEMS
ITEMVIEW_COZY = SizeMap(0, 0, 408, 84, CONT.pair)
ITEMVIEW_NORM = SizeMap(0, 0, 408, 24, CONT.pair)
ITEMVIEW_CARD = SizeMap(0, 0, 408, 156, CONT.pair)
IV_COZY_ICON = SizeMap(8, 8, 68, 68, ITEMVIEW_COZY.pair)
IV_COZY_NAME = SizeMap(84, 40, 316, 30, ITEMVIEW_COZY.pair)
IV_COZY_MISC = SizeMap(84, 10, 316, 24, ITEMVIEW_COZY.pair)
IV_NORM_ICON = SizeMap(4, 4, 16, 16, ITEMVIEW_NORM.pair)
IV_NORM_NAME = SizeMap(24, 2, 204, 24, ITEMVIEW_NORM.pair)
IV_NORM_MISC = SizeMap(232, 2, 172, 24, ITEMVIEW_NORM.pair)
IV_CARD_ICON = SizeMap(8, 80, 68, 68, ITEMVIEW_CARD.pair)
IV_CARD_NAME = SizeMap(84, 112, 316, 30, ITEMVIEW_CARD.pair)
IV_CARD_MISC = SizeMap(84, 82, 316, 24, ITEMVIEW_CARD.pair)
IV_CARD_DESC = SizeMap(8, 8, 392, 64, ITEMVIEW_CARD.pair)

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

# SORT
SORT_TYPE = SizeMap(16, 72, 124, 92, DROP_SORT.pair)
SORT_TYPE_L = SizeMap(16, 166, 124, 30, DROP_SORT.pair)
SORT_TYPE_BTN = SizeMap(0, 0, 124, 22, SORT_TYPE.pair)
SORT_ORDER = SizeMap(148, 120, 124, 46, DROP_SORT.pair)
SORT_ORDER_L = SizeMap(148, 164, 124, 30, DROP_SORT.pair)
SORT_ORDER_BTN = SizeMap(0, 0, 124, 22, SORT_ORDER.pair)
SORT_CANCEL = SizeMap(16, 16, 124, 36, DROP_SORT.pair)
SORT_SAVE = SizeMap(148, 16, 124, 36, DROP_SORT.pair)

# VIEW
VIEW_NORM = SizeMap(16, 132, 256, 48, DROP_VIEW.pair)
VIEW_NORM_L = SizeMap(184, 144, 49, 24, DROP_VIEW.pair)
VIEW_NORM_CHECK = SizeMap(245, 153, 13, 12, DROP_VIEW.pair)
VIEW_COZY = SizeMap(16, 74, 256, 48, DROP_VIEW.pair)
VIEW_COZY_L = SizeMap(184, 86, 49, 24, DROP_VIEW.pair)
VIEW_COZY_CHECK = SizeMap(245, 95, 13, 12, DROP_VIEW.pair)
VIEW_CARD = SizeMap(16, 16, 256, 48, DROP_VIEW.pair)
VIEW_CARD_L = SizeMap(184, 28, 49, 24, DROP_VIEW.pair)
VIEW_CARD_CHECK = SizeMap(245, 37, 13, 12, DROP_VIEW.pair)

# Positions =========================================================================
# SCREENS
SCREEN_POS_ON = ZEROS
SCREEN_POS_OFF = (APP_W, APP_H)
SCREEN_POS_FAR_OFF = (APP_W*2, APP_H*2)



# FRAME
BG = Image(size_hint = FILLS, source = 'images/IMG_MAIN.png', allow_stretch = True,
    keep_ratio = False)


# SCREENS
screenMain = RelativeLayout(pos = SCREEN_POS_ON, size_hint = FILLS)
screenSettings = RelativeLayout(pos = SCREEN_POS_OFF, size_hint = FILLS)


# Menu
menu = RelativeLayout(pos = MENU.pos, size_hint = MENU.hpair)
menuTitle = Label(size_hint = MENU_TITLE.hpair, pos = MENU_TITLE.pos,
    font_name = FONT_BASK, font_size = FONT_SIZE_A, color = WHITE)
menuBag = Image(size_hint = MENU_BTN_BAG.hpair, pos = MENU_BTN_BAG.pos,
    source = 'images/IMG_BAGS.png', keep_ratio = False, allow_stretch = True)
menuBagBtn = Button(size_hint = MENU_BTN_BAG.hpair, pos = MENU_BTN_BAG.pos,
    background_color = CLEAR)
menuOpts = Image(size_hint = MENU_BTN_OPTS.hpair, pos = MENU_BTN_OPTS.pos,
    source = 'images/IMG_SETTINGS.png', keep_ratio = False, allow_stretch = True)
menuOptsBtn = Button(size_hint = MENU_BTN_OPTS.hpair, pos = MENU_BTN_OPTS.pos,
    background_color = CLEAR)


# Tabs
tabs = BoxLayout(size_hint = TABS.hpair, pos = TABS.pos, orientation = 'horizontal')
tabsNew = Button(size_hint = TABS_BTN.hpair, text = 'NEW', color = WHITE,
    font_name = FONT_BASK, font_size = FONT_SIZE_A, background_color = CLEAR)
tabsSort = Button(size_hint = TABS_BTN.hpair, text = 'SORT', color = WHITE,
    font_name = FONT_BASK, font_size = FONT_SIZE_A, background_color = CLEAR)
tabsView = Button(size_hint = TABS_BTN.hpair, text = 'VIEW', color = WHITE,
    font_name = FONT_BASK, font_size = FONT_SIZE_A, background_color = CLEAR)

# Search
search = RelativeLayout(size_hint = SEARCH.hpair, pos = SEARCH.pos)
searchBG = Image(size_hint = FILLS, source = 'images/IMG_SEARCH.png',
    allow_stretch = True, keep_ratio = False)
searchInput = TextInput(size_hint = SEARCH_INPUT.hpair, pos = SEARCH_INPUT.pos,
    hint_text = 'Search for an item...', font_name = FONT_BASK,
    font_size = FONT_SIZE_C, foreground_color = BLACK, write_tab = False,
    multiline = False, cursor_color = BLACK, background_normal = '',
    background_active = '', background_color = CLEAR)


# Content
cont = RelativeLayout(size_hint = CONT.hpair, pos = CONT.pos)
contScroll = ScrollView(size_hint = FILLS, do_scroll_x = False,
    bar_width = CONT_SCROLL.x)
contList = GridLayout(size_hint = (1.0, None), cols = 1,
    padding = list(CONT_PAD.pair), spacing = list(CONT_SPACE.pair),
    row_force_default = True)


# Selected Item
pick = RelativeLayout(size_hint = PICK.hpair, pos = SCREEN_POS_OFF)
pickHalt = Button(pos = PICK_HALT.pos, size_hint = PICK_HALT.hpair,
    background_disabled_normal = IMG_BLACK, opacity = 0.5, disabled = True)
pickBG = Image(size_hint = FILLS, source = 'images/IMG_PICK.png',
    allow_stretch = True, keep_ratio = False)
pickWidges = RelativeLayout(size_hint = FILLS, pos = ZEROS)
pickName = TextInput(size_hint = PICK_NAME.hpair, pos = PICK_NAME.pos,
    font_name = FONT_BASK, font_size = FONT_SIZE_A, foreground_color = BLACK,
    border = [2,2,2,2], write_tab = False, multiline = False, cursor_color = BLACK,
    background_normal = 'images/IMG_1x1BORDER.png', hint_text = 'Item Name',
    background_active = 'images/IMG_1x1BORDER.png')
pickIcon = Button(size_hint = PICK_ICON.hpair, pos = PICK_ICON.pos,
    background_normal = 'images/blankIcon.png', background_down = 'images/blankIcon.png',
    border = [0,0,0,0])
pickMisc = BoxLayout(size_hint = PICK_MISC.hpair, pos = PICK_MISC.pos,
    orientation = 'horizontal')
pickQty_L = AnchorLabel(pos = PICK_QTY.pos, font_name = FONT_BASK,
    font_size = FONT_SIZE_C, color = BLACK, text = 'Quantity: ', anchor_x = 'right',
    halign = 'right', valign = 'bottom')
pickQty_I = TextInput(font_name = FONT_BASK, font_size = FONT_SIZE_C,
    foreground_color = BLACK, background_normal = 'images/IMG_1x1BORDER.png',
    background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
    write_tab = False, multiline = False, cursor_color = BLACK)
pickWeight_L = AnchorLabel(font_name = FONT_BASK, font_size = FONT_SIZE_C,
    color = BLACK, text = 'Weight: ', anchor_x = 'right', halign = 'right',
    valign = 'bottom')
pickWeight_I = TextInput(font_name = FONT_BASK, font_size = FONT_SIZE_C,
    foreground_color = BLACK, background_normal = 'images/IMG_1x1BORDER.png',
    background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
    write_tab = False, multiline = False, cursor_color = BLACK)
pickVal_L = AnchorLabel(font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK,
    text = 'Value: ', anchor_x = 'right', halign = 'right', valign = 'bottom')
pickVal_I = TextInput(font_name = FONT_BASK, font_size = FONT_SIZE_C,
    foreground_color = BLACK, background_normal = 'images/IMG_1x1BORDER.png',
    background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
    write_tab = False, multiline = False, cursor_color = BLACK)
pickTags = TextInput(size_hint = PICK_TAGS.hpair, pos = PICK_TAGS.pos,
    font_name = FONT_BASK, font_size = FONT_SIZE_C, foreground_color = BLACK,
    background_normal = 'images/IMG_1x1BORDER.png',
    background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
    cursor_color = BLACK)
pickDesc = TextInput(size_hint = PICK_DESC.hpair, pos = PICK_DESC.pos,
    font_name = FONT_BASK, font_size = FONT_SIZE_C, foreground_color = BLACK,
    background_normal = 'images/IMG_1x1BORDER.png',
    background_active = 'images/IMG_1x1BORDER.png', border = [2,2,2,2],
    cursor_color = BLACK)
pickOpts = AnchorButton(size_hint = PICK_OPTS.hpair, pos = PICK_OPTS.pos,
    source = 'images/IMG_SETTINGS.png', keep_ratio = True, allow_stretch = False,
    background_img = None)
pickX = AnchorButton(size_hint = PICK_X.hpair, pos = PICK_X.pos,
    text = 'X', font_name = FONT_BASK, font_size = FONT_SIZE_D, color = WHITE,
    background_img = None, valign = 'bottom')


# Icon selection
icon = RelativeLayout(size_hint = ICON.hpair, pos = SCREEN_POS_FAR_OFF)
iconHalt = Button(pos = ICON_HALT.pos, size_hint = ICON_HALT.hpair,
    background_disabled_normal = IMG_BLACK, opacity = 0.5, disabled = True)
iconBG = Image(size_hint = FILLS, source = 'images/IMG_PICK.png',
    allow_stretch = True, keep_ratio = False)
iconScroll = ScrollView(size_hint = ICON_SCROLL.hpair, pos = ICON_SCROLL.pos,
    do_scroll_x = False, bar_width = ICON_BAR.w)
iconGrid = GridLayout(size_hint = (1.0, None), cols = 4,
    row_default_height = ICON_HEIGHT.h, row_force_default = True,
    col_default_width = ICON_HEIGHT.w, col_force_default = True)
iconCancel = Button(size_hint = ICON_CANCEL.hpair, pos = ICON_CANCEL.pos,
    text = 'Cancel', font_name = FONT_BASK, font_size = FONT_SIZE_D, color = WHITE)
iconSave = Button(size_hint = ICON_SAVE.hpair, pos = ICON_SAVE.pos,
    text = 'Save', font_name = FONT_BASK, font_size = FONT_SIZE_D, color = WHITE)


# Tab drops
dropNew = RelativeLayout(size_hint = DROP_NEW.hpair, pos = SCREEN_POS_OFF)
dropNewHalt = Button(size_hint = DROP_NEW_HALT.hpair, pos = DROP_NEW_HALT.pos,
    opacity = 0)
dropNewBG = Image(size_hint = FILLS, source = 'images/IMG_DROP_NEW.png',
    allow_stretch = True, keep_ratio = False)

dropSort = RelativeLayout(size_hint = DROP_SORT.hpair, pos = SCREEN_POS_OFF)
dropSortHalt = Button(size_hint = DROP_SORT_HALT.hpair, pos = DROP_SORT_HALT.pos,
    opacity = 0)
dropSortBG = Image(size_hint = FILLS, source = 'images/IMG_DROP_SORT.png',
    allow_stretch = True, keep_ratio = False)

dropView = RelativeLayout(size_hint = DROP_VIEW.hpair, pos = SCREEN_POS_OFF)
dropViewHalt = Button(size_hint = DROP_VIEW_HALT.hpair, pos = DROP_VIEW_HALT.pos,
    opacity = 0)
dropViewBG = Image(size_hint = FILLS, source = 'images/IMG_DROP_VIEW.png',
    allow_stretch = True, keep_ratio = False)


# Tab drop: New
newName = TextInput(size_hint = NEW_NAME.hpair, hint_text = 'Name',
    pos = NEW_NAME.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
    write_tab = False, multiline = False)
newIcon = Button(size_hint = NEW_ICON.hpair, pos = NEW_ICON.pos,
    background_normal = 'images/blankIcon.png', background_down = 'images/blankIcon.png')
newQty = TextInput(size_hint = NEW_QTY.hpair, hint_text = 'Quantity',
    pos = NEW_QTY.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
    write_tab = False, multiline = False)
newQty_L = AnchorLabel(size_hint = NEW_QTY_L.hpair, text = 'Quantity',
    pos = NEW_QTY_L.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
    anchor_x = 'right', color = BLACK, halign = 'right')
newWeight = TextInput(size_hint = NEW_WEIGHT.hpair, hint_text = 'Weight',
    pos = NEW_WEIGHT.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
    write_tab = False, multiline = False)
newWeight_L = AnchorLabel(size_hint = NEW_WEIGHT_L.hpair, text = 'Weight',
    pos = NEW_WEIGHT_L.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
    anchor_x = 'right', color = BLACK, halign = 'right')
newVal = TextInput(size_hint = NEW_VAL.hpair, hint_text = 'Value',
    pos = NEW_VAL.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
    write_tab = False, multiline = False)
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


# Tab drop: Sort
sortType_L = AnchorLabel(size_hint = SORT_TYPE_L.hpair, text = 'Sort by',
    pos = SORT_TYPE_L.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
    anchor_x = 'left', anchor_y = 'bottom', color = BLACK, halign = 'left')
sortType = BoxLayout(size_hint = SORT_TYPE.hpair, pos = SORT_TYPE.pos,
    orientation = 'vertical')
sortType_name = AnchorButton(size_hint = SORT_TYPE_BTN.hpair, text = 'Name',
    font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK, anchor_x = 'left',
    halign = 'left')
sortType_qty = AnchorButton(size_hint = SORT_TYPE_BTN.hpair, text = 'Quantity',
    font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK, anchor_x = 'left',
    halign = 'left')
sortType_weight = AnchorButton(size_hint = SORT_TYPE_BTN.hpair, text = 'Weight',
    font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK, anchor_x = 'left',
    halign = 'left')
sortType_val = AnchorButton(size_hint = SORT_TYPE_BTN.hpair, text = 'Value',
    font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK, anchor_x = 'left',
    halign = 'left')
sortOrder_L = AnchorLabel(size_hint = SORT_ORDER_L.hpair, text = 'Sort order',
    pos = SORT_ORDER_L.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C,
    anchor_x = 'left', anchor_y = 'bottom', color = BLACK, halign = 'left')
sortOrder = BoxLayout(size_hint = SORT_ORDER.hpair, pos = SORT_ORDER.pos,
    orientation = 'vertical')
sortOrder_asc = AnchorButton(size_hint = SORT_ORDER_BTN.hpair, text = 'Ascending',
    font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK, anchor_x = 'left',
    halign = 'left')
sortOrder_desc = AnchorButton(size_hint = SORT_ORDER_BTN.hpair, text = 'Descending',
    font_name = FONT_BASK, font_size = FONT_SIZE_C, color = BLACK, anchor_x = 'left',
    halign = 'left')
sortCancel = Button(size_hint = SORT_CANCEL.hpair, text = 'CANCEL',
    pos = SORT_CANCEL.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C)
sortSave = Button(size_hint = SORT_SAVE.hpair, text = 'SAVE',
    pos = SORT_SAVE.pos, font_name = FONT_BASK, font_size = FONT_SIZE_C)

# Tab drop: View
viewNorm = Button(size_hint = VIEW_NORM.hpair, pos = VIEW_NORM.pos, opacity = 0)
viewNorm_L = AnchorLabel(size_hint = VIEW_NORM_L.hpair, pos = VIEW_NORM_L.pos,
    text = 'Normal', font_name = FONT_BASK, font_size = FONT_SIZE_B, color = WHITE,
    anchor_x = 'right', halign = 'right')
viewNorm_Check = Image(size_hint = VIEW_NORM_CHECK.hpair, pos = VIEW_NORM_CHECK.pos,
    source = VIEW_CHECK_INACTIVE)
viewCozy = Button(size_hint = VIEW_COZY.hpair, pos = VIEW_COZY.pos, opacity = 0)
viewCozy_L = AnchorLabel(size_hint = VIEW_COZY_L.hpair, pos = VIEW_COZY_L.pos,
    text = 'Cozy', font_name = FONT_BASK, font_size = FONT_SIZE_B, color = WHITE,
    anchor_x = 'right', halign = 'right')
viewCozy_Check = Image(size_hint = VIEW_COZY_CHECK.hpair, pos = VIEW_COZY_CHECK.pos,
    source = VIEW_CHECK_INACTIVE)
viewCard = Button(size_hint = VIEW_CARD.hpair, pos = VIEW_CARD.pos, opacity = 0)
viewCard_L = AnchorLabel(size_hint = VIEW_CARD_L.hpair, pos = VIEW_CARD_L.pos,
    text = 'Cards', font_name = FONT_BASK, font_size = FONT_SIZE_B, color = WHITE,
    anchor_x = 'right', halign = 'right')
viewCard_Check = Image(size_hint = VIEW_CARD_CHECK.hpair, pos = VIEW_CARD_CHECK.pos,
    source = VIEW_CHECK_INACTIVE)
