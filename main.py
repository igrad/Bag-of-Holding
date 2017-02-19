import kivy
kivy.require('1.9.1')

from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *
from modules.DropBtn import *

from BTN_New import *
from BTN_FILTERS import *
from BTN_ITEMS import *


class BagOfHolding(RelativeLayout):
    def __init__(self, **kwargs):
        '''Initialize the necessary elements for the app.'''
        super(BagOfHolding, self).__init__(**kwargs)

        # Load all saved configurations and item/bag data
        LoadData()

        self.SetBinds()
        self.AddChildren()

        OpenBag(LAST_BAG_OPENED)

        cont_List.bind(minimum_height = cont_List.setter('height'))

    def SetBinds(self):
        # SCREEN MAIN ===================================================================
        # MAIN

        # TABS
        #tabs_Sort.bind(on_press = OpenDropSort)
        #tabs_Filt.bind(on_press = OpenDropFilt)
        #tabs_View.bind(on_press = OpenDropView)

        # CONTENTPANES
        # Items
        # self.bindItemViews()

        # Filters
        filt_cat.bind(on_press = OpenFilt_Cat)

        # New
        new_cancel.bind(on_press = OpenContPane_New)
        new_save.bind(on_press = InputItem)

    def AddChildren(self):
        # SCREEN MAIN ===================================================================
        # Background
        screen_main.add_widget(BG)

        # Menu
        for widge in [menu_Title, menu_Btn_Bag, menu_Btn_Opts]:
            menu.add_widget(widge)

        # Tabs
        for widge in [tabs_Sort, tabs_Filt, tabs_View]:
            tabs.add_widget(widge)


        # Contpane Items
        cont_Scroll.add_widget(cont_List)
        contpane_items.add_widget(cont_Scroll)

        # Contpane Filters
        # for widge in [filt_cat_name, filt_cat_qty, filt_cat_weight, filt_cat_val]:
        #     filt_cat.add_widget(widge)

        filt_sort.add_widget(filt_sort_asc)
        filt_sort.add_widget(filt_sort_des)

        filt_tags_scroll.add_widget(filt_tags)

        for widge in [filt_name, filt_catlbl, filt_cat, filt_sortlbl, filt_sort_pick, filt_sort, filt_tagslbl, filt_tags_scroll]:
            contpane_filters.add_widget(widge)

        # Contpane New
        for widge in [new_name, new_icon, new_qty, new_weight, new_val, new_tags, new_desc, new_cancel, new_save]:
            contpane_new.add_widget(widge)

        # Contpane
        for widge in [contpane_items, contpane_filters, contpane_new]:
            contpane.add_widget(widge)

        # Render
        for widge in [contpane, menu, tabs]:
            screen_main.add_widget(widge)

        self.add_widget(screen_main)

        # SCREEN SETTINGS ===============================================================
        # do a flip


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
