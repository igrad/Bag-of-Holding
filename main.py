#!usr/bin/python3
import kivy
kivy.require('1.10.0')

from SysFuncs import *

from LoadSaves import *

from AppInit import *
from Tabs import *
from ContPane import *
from Icon import LoadAllIcons, OpenIconMenu, SaveIcon
from BagPick import *

class BagOfHolding(RelativeLayout):
    def __init__(self, **kwargs):
        '''Initialize the necessary elements for the app.'''
        LogMsg('Beginning app initialization.')

        super(BagOfHolding, self).__init__(**kwargs)

        # Load all saved configurations and item/bag data
        LoadData()

        # Build widgets hierarchy
        self.SetBinds()
        self.AddChildren()

        # Set window statuses
        bagPick.is_open = False

        pick.is_open = False
        icon.is_open = False

        dropNew.is_open = False
        dropSort.is_open = False
        dropView.is_open = False

        newIcon.selected = None

        # Set view types
        viewNorm.view_type = 'norm'
        viewCozy.view_type = 'cozy'
        viewCard.view_type = 'card'

        # Load up data needed for the ContPane
        OpenBag(LAST_BAG_OPENED)
        GenerateComparisonPhrases()

        contList.bind(minimum_height = contList.setter('height'))

        # Load up auxilliary windows
        LoadAllIcons()

        iconGrid.bind(minimum_height = iconGrid.setter('height'))

        LogMsg('App initialization complete.')


    def SetBinds(self):
        # TABS
        tabsNew.bind(on_press = OpenNew)
        tabsSort.bind(on_press = OpenSort)
        tabsView.bind(on_press = OpenView)

        # New
        newCancel.bind(on_press = OpenNew)
        newSave.bind(on_press = InputItem)
        newIcon.bind(on_press = OpenIconMenu)

        # View
        viewNorm.bind(on_press = SetView)
        viewCozy.bind(on_press = SetView)
        viewCard.bind(on_press = SetView)

        # SORT
        sortType_name.bind(on_press = UpdateSort)
        sortType_qty.bind(on_press = UpdateSort)
        sortType_weight.bind(on_press = UpdateSort)
        sortType_val.bind(on_press = UpdateSort)

        sortOrder_asc.bind(on_press = UpdateSort)
        sortOrder_desc.bind(on_press = UpdateSort)

        # SEARCH
        searchInput.bind(text = ScheduleSearch)

        # BAGPICK
        menuBagBtn.bind(on_press = OpenBagPickMenu)
        bagPickHalt.bind(on_press = OpenBagPickMenu)

        # SELECT
        pickX.bind(on_press = SelectItem)
        pickIcon.bind(on_press = OpenIconMenu)
        SetItemViewsOnPress(SelectItem)

        # ICON
        iconCancel.bind(on_press = OpenIconMenu)
        iconSave.bind(on_press = SaveIcon)


    def AddChildren(self):
        # Background
        screenMain.add_widget(BG)

        # Menu
        for widge in [menuTitle, menuBag, menuBagBtn, menuOpts, menuOptsBtn]:
            menu.add_widget(widge)

        # Tabs
        for widge in [tabsNew, tabsSort, tabsView]:
            tabs.add_widget(widge)

        # Tab menus
        for widge in [dropNewHalt, dropNewBG, newName, newIcon, newQty_L, newQty, newWeight_L, newWeight, newVal_L, newVal, newTags, newDesc, newCancel, newSave]:
            dropNew.add_widget(widge)

        for widge in [sortType_name, sortType_qty, sortType_weight, sortType_val]:
            sortType.add_widget(widge)

        for widge in [sortOrder_asc, sortOrder_desc]:
            sortOrder.add_widget(widge)

        for widge in [dropSortHalt, dropSortBG, sortType_L, sortType, sortOrder_L, sortOrder]:
            dropSort.add_widget(widge)

        for widge in [dropViewHalt, dropViewBG, viewNorm, viewNorm_L, viewNorm_Check, viewCozy, viewCozy_L, viewCozy_Check, viewCard, viewCard_L, viewCard_Check]:
            dropView.add_widget(widge)

        # Search
        search.add_widget(searchBG)
        search.add_widget(searchInput)

        # Contpane
        contScroll.add_widget(contList)
        cont.add_widget(contScroll)

        # Bags menu
        bagPickScroll.add_widget(bagPickGrid)

        for widge in [bagPickHalt, bagPickBG, bagPickName, bagPickScroll]:
            bagPick.add_widget(widge)

        # Selected Item
        for widge in [pickQty_L, pickQty_I, pickWeight_L, pickWeight_I, pickVal_L, pickVal_I]:
            pickMisc.add_widget(widge)

        for widge in [pickName, pickIcon, pickMisc, pickTags, pickDesc, pickOpts, pickX]:
            pickWidges.add_widget(widge)

        for widge in [pickHalt, pickBG, pickWidges]:
            pick.add_widget(widge)

        iconScroll.add_widget(iconGrid)

        for widge in [iconHalt, iconBG, iconScroll, iconCancel, iconSave]:
            icon.add_widget(widge)

        # Render
        for widge in [cont, menu, search, dropNew, dropSort, dropView, tabs, bagPick, pick, icon]:
            screenMain.add_widget(widge)

        self.add_widget(screenMain)


class Builder(App):
    #mode = "PROD"
    mode = "DEV"


    def build_config(self, config):
        self.title = "Bag of Holding"

        global XSCALE, YSCALE

        height = int(768 / YSCALE)
        width = int(432 / XSCALE)

        Config.set('graphics', 'borderless', 1)
        Config.set('graphics', 'resizable', 0)
        Config.set('graphics', 'max_fps', 60)
        Config.set('graphics', 'height', height)
        Config.set('graphics', 'width', width)
        Config.set('graphics', 'show_cursor', '1')

        LogMsg('Getting app launch mode...')
        if Builder.mode == "DEV":
            LogMsg('Opening App in Dev mode.')
            Config.set('graphics', 'fullscreen', 0)
            Window.left = 3072
            Window.top = 28
            Config.set('graphics', 'rotation', 0)
        else:
            LogMsg('Opening App in Prod mode.')
            Config.set('graphics', 'rotation', 90)
            Config.set('graphics', 'fullscreen', 'auto')

        Config.set('kivy', 'window_icon', 'images/icon.png')
        Config.write()

        LogMsg('Window size found: {}'.format(Window.size))

    def build(self):
        config = self.config
        Window.clearcolor = (1,1,1,1)

        return BagOfHolding()

if __name__ == '__main__':
    Builder().run()
