import kivy
kivy.require('1.9.1')

from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *

from BTN_New import *


class BagOfHolding(RelativeLayout):
    def __init__(self, **kwargs):
        '''Initialize the necessary elements for the app.'''
        super(BagOfHolding, self).__init__(**kwargs)

        # Load all saved configurations and item/bag data
        LoadData()

        self.SetBinds()
        self.AddChildren()

        self.OpenBag(LAST_BAG_OPENED)

        cont_List.bind(minimum_height = cont_List.setter('height'))

    def SetBinds(self):
        # SCREEN MAIN ===================================================================
        # MAIN

        # TABS
        tabs_New.bind(on_press = OpenContPane_New)

        # CONTENTPANES
        # Items
        # self.bindItemViews()

        # Filters

        # New
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



    def OpenBag(self, openBagID):
        b = 0
        found = False
        bag = 0

        bagIDs = BAGS.keys()

        for ID in bagIDs:
            if ID == openBagID:
                b = ID
                found = True

        # Specified bag could not be found. Open the first bag listed instead and send a
        # notification to the user.
        if found:
            bag = BAGS[b]
        elif not found and len(bagIDs) > 0:
            # TODO Notify user that the bag they've selected could not be found
            bag = BAGS[0]
            print('BAG NOT FOUND, BAGS AVAILABLE')
        # User does not have any bags created
        elif not found and len(bagIDs) == 0:
            print('BAG NOT FOUND, NONE')
            bag = Bag()

        # Update the bag title on-screen
        # TODO Update loaded bag's title at the top of screen

        # Update the contents of the contPane GridLayout by creating individual ItemViews
        ITEMVIEWS.clear()
        cont_List.clear_widgets()
        i = 0

        print('INFO || Number of items to load: ' + str(len(bag.items)))

        LoadItems(bag.items)

        for itemID in bag.items:
            ITEMVIEWS.append(ItemView(itemID = itemID))

            # Filters still need to be applied after opening a new bag
            # TODO Apply filters after opening new bag

            # Add the remaining ItemViews to the grid
            # NOTE This will need to be made a function of the filter. IE, if the item
            # NOTE passes through the filter, post it to the grid.
            print("TROUBLESHOOTING || ITEMVIEWS entries: " + str([x.itemID for x in ITEMVIEWS]))
            print("TROUBLESHOOTING || ITEMVIEWS[0]: " + str(ITEMVIEWS[0]))

            cont_List.add_widget(ITEMVIEWS[i])

            i += 1

        # After all items have been posted to the grid for display, update the scroller's
        # height to reflect the size of the new grid.
        self.UpdateItemList()

    def UpdateItemList(self):
        cont_Scroll.clear_widgets()

        cont_List.bind(minimum_height = cont_List.setter('height'))
        cont_Scroll.add_widget(cont_List)

        contpane_items.clear_widgets()
        contpane_items.add_widget(cont_Scroll)


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
