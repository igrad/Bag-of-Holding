#!usr/bin/python3
import kivy
kivy.require('1.9.1')

from SysFuncs import *

from LoadSaves import *

from AppInit import *
from Tabs import *
from ContPane import *
from Icon import LoadAllIcons, OpenIconMenu, SaveIcon
from BagPick import *
from BagOpts import *
from ItemOpts import *



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
        LogMsg('Setting widget binds')

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


        # SELECT
        pick.X.bind(on_press = SelectItem)
        pick.opts.bind(on_press = OpenItemOpts)
        pick.icon.bind(on_press = OpenIconMenu)
        SetItemViewsOnPress(SelectItem)

        # ITEMOPTS
        itemOpts.halt.bind(on_press = OpenItemOpts)
        itemOpts.move.bind(on_press = OpenItemMove)
        itemOpts.cancel.bind(on_press = OpenItemOpts)

        itemMove.halt.bind(on_press = OpenItemMove)
        itemMove.cancel.bind(on_press = OpenItemMove)


        # BAGPICK
        menu.bagBtn.bind(on_press = OpenBagPickMenu)
        bagPick.back.bind(on_press = OpenBagPickMenu)

        # BAGOPTS
        bagOpts.halt.bind(on_press = PreviewBagMenu)

        # BAGDELETE
        bagDelete.halt.bind(on_press = OnBagDeleteSelected)

        # ICON
        icon.cancel.bind(on_press = OpenIconMenu)
        icon.save.bind(on_press = SaveIcon)
        LogMsg('Widget binds set!')


    def AddChildren(self):
        LogMsg('Creating widget hierarchy')

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

        for widge in [bagPick.back, bagPick.halt, bagPick.BG, bagPick.name, bagPick.scroll, bagPick.newBag]:
            bagPick.base.add_widget(widge)


        # Bag preview menu
        for widge in (bagOpts.weight, bagOpts.currency, bagOpts.delete, bagOpts.done):
            bagOpts.btns.add_widget(widge)

        for widge in (bagOpts.halt, bagOpts.back, bagOpts.BG, bagOpts.name, bagOpts.btns):
            bagOpts.base.add_widget(widge)

        for widge in (bagDelete.halt, bagDelete.back, bagDelete.BG, bagDelete.lbl):
            bagDelete.base.add_widget(widge)


        # Selected Item
        for widge in [pick.qty_L, pick.qty_I, pick.weight_L, pick.weight_I, pick.val_L, pick.val_I]:
            pick.misc.add_widget(widge)

        for widge in [pick.name, pick.icon, pick.misc, pick.tags, pick.desc, pick.opts, pick.X]:
            pick.widges.add_widget(widge)

        for widge in [pick.halt, pick.BG, pick.widges]:
            pick.base.add_widget(widge)


        # Item Options
        for widge in [itemOpts.move, itemOpts.delete, itemOpts.cancel]:
            itemOpts.btns.add_widget(widge)

        for widge in [itemOpts.halt, itemOpts.back, itemOpts.BG, itemOpts.lbl, itemOpts.btns]:
            itemOpts.base.add_widget(widge)

        for widge in [itemMove.halt, itemMove.back, itemMove.BG, itemMove.lbl, itemMove.scroll, itemMove.cancel]:
            itemMove.base.add_widget(widge)


        # Icon selection screen
        icon.scroll.add_widget(icon.grid)

        for widge in [icon.halt, icon.BG, icon.scroll, icon.cancel, icon.save]:
            icon.base.add_widget(widge)


        # Render
        for widge in [cont.base, menu.base, search.base, tabs.base]:
            base.screenMain.add_widget(widge)

        self.add_widget(base.screenMain)



class Builder(App):
    #mode = "PROD"
    mode = "DEV"
    res = "normal"

    def build_config(self, config):
        LogMsg('Building Configurations...')

        self.title = "Bag of Holding"

        if Builder.res == "small":
            scale.Y = 1
            scale.X = 1

        height = int(768/scale.Y)
        width = int(432/scale.X)

        Config.set('graphics', 'borderless', 1)
        Config.set('graphics', 'resizable', 0)
        Config.set('graphics', 'max_fps', 60)
        Config.set('graphics', 'height', height)
        Config.set('graphics', 'width', width)
        Config.set('graphics', 'show_cursor', '1')

        if Builder.mode == "DEV":
            LogMsg('Opening App in Dev mode.')
            Config.set('graphics', 'fullscreen', 0)
            Window.left = 3072
            Window.top = 28
            if Builder.res == "small":
                Window.left = 1366 - width
                Window.top = 768 - height
            Config.set('graphics', 'rotation', 0)
        else:
            LogMsg('Opening App in Prod mode.')
            Config.set('graphics', 'rotation', 0)
            Config.set('graphics', 'fullscreen', 'auto')


        LogMsg("Building scales. Window dimensions: ({}, {})".format(Window.size[0], Window.size[1]))
        LogMsg("w = 432/" + str(Window.size[0]) + " = " + str(float(432)/float(Window.size[0])))
        LogMsg("h = 768/" + str(Window.size[1]) + " = " + str(float(768)/float(Window.size[1])))
        scale.X = float(432)/float(Window.size[0])
        scale.Y = float(768)/float(Window.size[1])
        LogMsg("Scales set to ({}, {})".format(scale.X, scale.Y))

        Config.set('kivy', 'window_icon', 'images/icon.png')
        Config.write()

        LogMsg('Window size found: {}'.format(Window.size))

        # Build widgets
        LogMsg('Resizing widget groups')

        global size, base, menu, tabs, search, cont, bagPick, bagOpts, pick, icon, dnew, dsort, dview, FONT_SIZE_A, FONT_SIZE_B, FONT_SIZE_C, FONT_SIZE_D, FONT_SIZE_HEAD
        size.__init__()
        base.__init__(size)
        menu.__init__(size)
        tabs.__init__(size)
        search.__init__(size)
        cont.__init__(size)
        bagPick.__init__(size)
        bagOpts.__init__(size)
        bagDelete.__init__(size)
        itemOpts.__init__(size)
        itemMove.__init__(size)
        pick.__init__(size)
        icon.__init__(size)
        dnew.__init__(size)
        dsort.__init__(size)
        dview.__init__(size)


    def build(self):
        config = self.config
        Window.clearcolor = (1,1,1,1)

        return BagOfHolding()

if __name__ == '__main__':
    LogMsg('Starting up')
    Builder().run()
