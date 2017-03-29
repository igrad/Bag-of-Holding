import kivy
kivy.require('1.9.1')

from SysFuncs import *
from LoadSaves import *
from AppInit import *

from Tabs import *
from ContPane import *


class BagOfHolding(RelativeLayout):
    def __init__(self, **kwargs):
        '''Initialize the necessary elements for the app.'''
        LogMsg('Beginning app initialization.')
        super(BagOfHolding, self).__init__(**kwargs)

        # Load all saved configurations and item/bag data
        LoadData()

        self.SetBinds()
        self.AddChildren()

        dropNew.is_open = False
        dropSort.is_open = False
        dropView.is_open = False

        viewNorm.view_type = 'norm'
        viewCozy.view_type = 'cozy'
        viewCard.view_type = 'card'

        OpenBag(LAST_BAG_OPENED)

        contList.bind(minimum_height = contList.setter('height'))

    def SetBinds(self):
        # TABS
        tabsNew.bind(on_press = OpenNew)
        tabsSort.bind(on_press = OpenSort)
        tabsView.bind(on_press = OpenView)

        # New
        newCancel.bind(on_press = OpenNew)
        newSave.bind(on_press = InputItem)

        # Sort
        sortCancel.bind(on_press = OpenSort)
        #sortSave.bind(on_press = ApplySort)

        # View
        viewNorm.bind(on_press = SetView)
        viewCozy.bind(on_press = SetView)
        viewCard.bind(on_press = SetView)

    def AddChildren(self):
        # Background
        screenMain.add_widget(BG)

        # Menu
        for widge in [menuTitle, menuBag, menuOpts]:
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

        for widge in [dropSortHalt, dropSortBG, sortType_L, sortType, sortOrder_L, sortOrder, sortCancel, sortSave]:
            dropSort.add_widget(widge)

        for widge in [dropViewHalt, dropViewBG, viewNorm, viewNorm_L, viewNorm_Check, viewCozy, viewCozy_L, viewCozy_Check, viewCard, viewCard_L, viewCard_Check]:
            dropView.add_widget(widge)

        # Contpane
        contScroll.add_widget(contList)
        cont.add_widget(contScroll)

        # Render
        for widge in [cont, menu, dropNew, dropSort, dropView, tabs]:
            screenMain.add_widget(widge)

        self.add_widget(screenMain)


class Builder(App):
    #mode = "PROD"
    mode = "DEV"

    def build_config(self, config):
        self.title = "Bag of Holding"

        height = str(int(768 / YSCALE))
        width = str(int(432 / XSCALE))

        Config.set('graphics', 'borderless', '0')
        Config.set('graphics', 'max_fps', '60')
        Config.set('graphics', 'height', height)
        Config.set('graphics', 'width', width)
        Config.set('graphics', 'show_cursor', '1')


        if Builder.mode == "DEV":
            Config.set('graphics', 'height', height)
            Config.set('graphics', 'width', width)
            Config.set('graphics', 'rotation', '00')
            Config.set('graphics', 'fullscreen', '0')
        else:
            Config.set('graphics', 'height', '1080')
            Config.set('graphics', 'width', '1920')
            Config.set('graphics', 'rotation', '90')
            Config.set('graphics', 'fullscreen', '1')


        Config.set('kivy', 'window_icon', 'images/icon.png')
        Config.write()

    def build(self):
        config = self.config
        Window.clearcolor = (1,1,1,1)

        return BagOfHolding()

if __name__ == '__main__':
    Builder().run()
