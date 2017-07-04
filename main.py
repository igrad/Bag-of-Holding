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

        dnew.is_open = False
        dsort.is_open = False
        dview.is_open = False

        dnew.icon.selected = None

        # Set view types
        dview.norm.view_type = 'norm'
        dview.cozy.view_type = 'cozy'
        dview.card.view_type = 'card'

        # Load up data for bagPick menu
        bagPick.grid.bind(minimum_height = bagPick.grid.setter('height'))

        # Load up data needed for the ContPane
        OpenBag(LAST_BAG_OPENED)
        GenerateComparisonPhrases()

        cont.list.bind(minimum_height = cont.list.setter('height'))

        # Load up auxilliary windows
        LoadAllIcons()

        icon.grid.bind(minimum_height = icon.grid.setter('height'))

        LogMsg('App initialization complete.')


    def SetBinds(self):
        # TABS
        tabs.new.bind(on_press = OpenNew)
        tabs.sort.bind(on_press = OpenSort)
        tabs.view.bind(on_press = OpenView)

        # New
        dnew.cancel.bind(on_press = OpenNew)
        dnew.save.bind(on_press = InputItem)
        dnew.icon.bind(on_press = OpenIconMenu)

        # View
        dview.norm.bind(on_press = SetView)
        dview.cozy.bind(on_press = SetView)
        dview.card.bind(on_press = SetView)

        # SORT
        dsort.type_name.bind(on_press = UpdateSort)
        dsort.type_qty.bind(on_press = UpdateSort)
        dsort.type_weight.bind(on_press = UpdateSort)
        dsort.type_val.bind(on_press = UpdateSort)

        dsort.order_asc.bind(on_press = UpdateSort)
        dsort.order_desc.bind(on_press = UpdateSort)

        # SEARCH
        search.input.bind(text = ScheduleSearch)

        # BAGPICK
        menu.bagBtn.bind(on_press = OpenBagPickMenu)
        bagPick.halt.bind(on_press = OpenBagPickMenu)

        # SELECT
        pick.X.bind(on_press = SelectItem)
        pick.icon.bind(on_press = OpenIconMenu)
        SetItemViewsOnPress(SelectItem)

        # ICON
        icon.cancel.bind(on_press = OpenIconMenu)
        icon.save.bind(on_press = SaveIcon)


    def AddChildren(self):
        # Background
        base.screenMain.add_widget(base.BG)

        # Menu
        for widge in [menu.title, menu.bag, menu.bagBtn, menu.opts, menu.optsBtn]:
            menu.base.add_widget(widge)

        # Tabs
        for widge in [tabs.new, tabs.sort, tabs.view]:
            tabs.base.add_widget(widge)

        # New Drop Menu
        for widge in [dnew.halt, dnew.BG, dnew.name, dnew.icon, dnew.qty_L, dnew.qty, dnew.weight_L, dnew.weight, dnew.val_L, dnew.val, dnew.tags, dnew.desc, dnew.cancel, dnew.save]:
            dnew.base.add_widget(widge)

        # Sort Drop Menu
        for widge in [dsort.type_name, dsort.type_qty, dsort.type_weight, dsort.type_val]:
            dsort.type.add_widget(widge)

        for widge in [dsort.order_asc, dsort.order_desc]:
            dsort.order.add_widget(widge)

        for widge in [dsort.halt, dsort.BG, dsort.type_L, dsort.type, dsort.order_L, dsort.order]:
            dsort.base.add_widget(widge)

        # View Drop Menu
        for widge in [dview.halt, dview.BG, dview.norm, dview.norm_L, dview.norm_Check, dview.cozy, dview.cozy_L, dview.cozy_Check, dview.card, dview.card_L, dview.card_Check]:
            dview.base.add_widget(widge)

        # Search
        search.base.add_widget(search.BG)
        search.base.add_widget(search.input)

        # Contpane
        cont.scroll.add_widget(cont.list)
        cont.base.add_widget(cont.scroll)

        # Bags menu
        bagPick.scroll.add_widget(bagPick.grid)

        for widge in [bagPick.halt, bagPick.BG, bagPick.name, bagPick.scroll]:
            bagPick.base.add_widget(widge)

        # Selected Item
        for widge in [pick.qty_L, pick.qty_I, pick.weight_L, pick.weight_I, pick.val_L, pick.val_I]:
            pick.misc.add_widget(widge)

        for widge in [pick.name, pick.icon, pick.misc, pick.tags, pick.desc, pick.opts, pick.X]:
            pick.widges.add_widget(widge)

        for widge in [pick.halt, pick.BG, pick.widges]:
            pick.base.add_widget(widge)

        icon.scroll.add_widget(icon.grid)

        for widge in [icon.halt, icon.BG, icon.scroll, icon.cancel, icon.save]:
            icon.base.add_widget(widge)

        # Render
        for widge in [cont.base, menu.base, search.base, dnew.base, dsort.base, dview.base, tabs.base, bagPick.base, pick.base, icon.base]:
            base.screenMain.add_widget(widge)

        self.add_widget(base.screenMain)


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
