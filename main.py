import kivy
kivy.require('1.9.1')

from SysFuncs import *
from AppInit import *
from Bag import *
from BagItem import *
from ItemView import *
from SaveStores import *

class BagOfHolding(RelativeLayout):
    def __init__(self, **kwargs):
        '''Initialize the necessary elements for the app.'''
        super(BagOfHolding, self).__init__(**kwargs)

        # Load all saved configurations and item/bag data
        LoadData()

        self.AddChildren()

        self.OpenBag(LAST_BAG_OPENED)

        cont_List.bind(minimum_height = cont_List.setter('height'))

    def AddChildren(self):
        # Background
        self.add_widget(BG)

        # SCREEN MAIN
        # Menu
        menu.add_widget(menu_Title)
        menu.add_widget(menu_Btn_Bag)
        menu.add_widget(menu_Btn_Opts)

        self.add_widget(menu)

        # Tabs
        tabs.add_widget(tabs_Items)
        tabs.add_widget(tabs_Filter)
        tabs.add_widget(tabs_New)
        tabs.add_widget(tabs_Pick)

        self.add_widget(tabs)

        # Cont
        cont_Scroll.add_widget(cont_List)
        cont.add_widget(cont_Scroll)

        screen_main.add_widget(cont)

        self.add_widget(screen_main)


        # SCREEN NEW



        # Frame
        self.add_widget(Border)



    def OpenBag(self, openBagID):
        b = 0

        found = False
        for bag in BAGS:
            if bag.ID == openBagID:
                b = bag.ID
                found = True

        # Specified bag could not be found. Open the first bag listed instead and send a
        # notification to the user.
        if not found and len(BAGS) > 0:
            # TODO Notify user that the bag they've selected could not be found
            bag = BAGS[0]
        # User does not have any bags created
        elif not found and len(BAGS) == 0:
            bag = Bag()

        # Update the bag title on-screen
        # TODO Update loaded bag's title at the top of screen

        # Update the contents of the contPane GridLayout by creating individual ItemViews
        ITEMVIEWS.clear()
        cont_List.clear_widgets()
        i = 0

        for item in bag.items:
            ITEMVIEWS.append(ItemView(item))
            i += 1

            # Filters still need to be applied after opening a new bag
            # TODO Apply filters after opening new bag

            # Add the remaining ItemViews to the grid
            # NOTE This will need to be made a function of the filter. IE, if the item
            # NOTE passes through the filter, post it to the grid.
            cont_List.add_widget(ITEMVIEWS[i])

        # After all items have been posted to the grid for display, update the scroller's
        # height to reflect the size of the new grid.
        self.UpdateLiveGrid()

    def UpdateLiveGrid(self):
        cont_Scroll.clear_widgets()

        cont_List.bind(minimum_height = cont_List.setter('height'))
        cont_Scroll.add_widget(cont_List)

        cont.clear_widgets()
        cont.add_widget(cont_Scroll)

class Builder(App):
    title = "Bag of Holding"

    def build_config(self, config):
        Config.set('graphics', 'borderless', '1')
        Config.set('graphics', 'max_fps', '60')
        Config.set('graphics', 'height', '1080')
        Config.set('graphics', 'width', '1920')
        Config.set('graphics', 'rotation', '90')
        Config.set('graphics', 'show_cursor', '1')
        Config.set('graphics', 'fullscreen', '1')

        Config.set('kivy', 'window_icon', 'images/icon.png')
        Config.write()

    def build(self):
        config = self.config
        Window.clearcolor = (1,1,1,1)

        return BagOfHolding()

if __name__ == '__main__':
    Builder().run()
