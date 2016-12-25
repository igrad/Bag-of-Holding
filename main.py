import kivy
kivy.require('1.9.1')

from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *

from BTN_New import *
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
        tabs_Items.bind(on_press = OpenContPane_Items)
        tabs_New.bind(on_press = OpenContPane_New)

        # CONTENTPANES
        # Items
        # self.bindItemViews()

        # Filters

        # New
        new_cancel.bind(on_press = OpenContPane_New)
        new_save.bind(on_press = InputItem)

    def AddChildren(self):
        # SCREEN MAIN ===================================================================
        # Background
        screen_main.add_widget(BG)

        # Menu
        menu.add_widget(menu_Title)
        menu.add_widget(menu_Btn_Bag)
        menu.add_widget(menu_Btn_Opts)


        # Tabs
        tabs.add_widget(tabs_Items)
        tabs.add_widget(tabs_Filter)
        tabs.add_widget(tabs_New)
        tabs.add_widget(tabs_Pick)


        # Contpane Items
        cont_Scroll.add_widget(cont_List)
        contpane_items.add_widget(cont_Scroll)


        # Contpane New
        contpane_new.add_widget(new_name)
        contpane_new.add_widget(new_icon)
        contpane_new.add_widget(new_qty)
        contpane_new.add_widget(new_weight)
        contpane_new.add_widget(new_val)
        contpane_new.add_widget(new_tags)
        contpane_new.add_widget(new_desc)
        contpane_new.add_widget(new_cancel)
        contpane_new.add_widget(new_save)


        # Render
        screen_main.add_widget(contpane_items)
        screen_main.add_widget(contpane_new)
        screen_main.add_widget(Border)
        screen_main.add_widget(menu)
        screen_main.add_widget(tabs)

        self.add_widget(screen_main)

        # SCREEN SETTINGS ===============================================================
        # do a flip


class Builder(App):
    title = "Bag of Holding"

    def build_config(self, config):
        Config.set('graphics', 'borderless', '0')
        Config.set('graphics', 'max_fps', '60')
        Config.set('graphics', 'height', '960')
        Config.set('graphics', 'width', '540')
        Config.set('graphics', 'rotation', '00')
        Config.set('graphics', 'show_cursor', '1')
        Config.set('graphics', 'fullscreen', '0')

        Config.set('kivy', 'window_icon', 'images/icon.png')
        Config.write()

    def build(self):
        config = self.config
        Window.clearcolor = (1,1,1,1)

        return BagOfHolding()

if __name__ == '__main__':
    Builder().run()
