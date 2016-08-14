VERSION_INFO = 'A_01 August 07, 2016'
DEBUGMODE = True

#==============================================================================#
# GLOBAL: IMPORTS                                                              #
#==============================================================================#
import kivy
kivy.require('1.9.1')

# Core
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.core.text import Text
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore

from collections import deque as Deque
import time as Time

# Kivy
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.listview import ListView
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

#==============================================================================#
# GLOBAL: CONSTANTS                                                            #
#==============================================================================#
# Sizes
BASE_H = 960
BASE_W = 540

MENU_H = 0.10 * BASE_H
MENU_W = 1.00 * BASE_W
MENU_SIZE = (MENU_W, MENU_H)
MENU_BTN_SIZE = (MENU_H, MENU_H)

TABS_H = 0.10
TABS_W = 1.00
TABS_SIZE = (TABS_W * BASE_W, TABS_H * BASE_H)
TABS_BTN_H = 1.00
TABS_BTN_W = 0.50
TABS_BTN_SIZE_HINT = (TABS_BTN_W, TABS_BTN_H)

CONT_H = 0.80
CONT_W = 1.00
CONT_SIZE = (CONT_W * BASE_W, CONT_H * BASE_H)
CONT_LIST_H = 0.10
CONT_LIST_W = 1.00
CONT_LIST_SIZE_HINT = (CONT_LIST_W, CONT_LIST_H)
CONT_GRID_H = CONT_W * 0.20
CONT_GRID_W = 0.20
CONT_GRID_SIZE = (CONT_GRID_W, CONT_GRID_H)

# Stylization
ANIMTIME = 0.35
ANIMSTYLE = 'out_cubic'
USEFONT = 'fonts/BASKVILL.TTF'

# System
NONES = (None, None)

# Art paths
if True:
    COLOR_HEAD = 'images/COLOR_HEAD.png'
    COLOR_BODY = 'images/COLOR_BODY.png'
    COLOR_MISC = 'images/COLOR_MISC.png'

    ICON_BAG = 'images/bag_icon.png'
    ICON_OPTS = 'images/opts_icon.png'

#=======================================================================================#
# CLASSES                                                                               #
#=======================================================================================#

class MainMenu(RelativeLayout):
    #===================================================================================#
    # CLASS: VARIABLES                                                                  #
    #===================================================================================#
    if(True):
        # Base Menu =====================================================================
        baseLayout = BoxLayout(size_hint = (1.0, 1.0), orientation = 'vertical',
                               spacing = 2)
        baseBG = Image(allow_stretch = True, keep_ratio = False, source = COLOR_MISC,
                       size_hint = (1.0, 1.0))

        # Menu Bar ======================================================================
        menuBar = RelativeLayout(size = MENU_SIZE, size_hint = NONES)
        menuBG = Image(allow_stretch = True, keep_ratio = False, source = COLOR_HEAD,
                       size_hint = (1.0, 1.0))
        menuBagsBtn = Button(size_hint = NONES, background_normal = ICON_BAG,
                             background_down = ICON_BAG, size = MENU_BTN_SIZE)
        menuOptsBtn = Button(size_hint = NONES, background_normal = ICON_OPTS,
                             background_down = ICON_OPTS, pos_hint = {'right': 1.0},
                             size = MENU_BTN_SIZE)

        # Tabs Bar ======================================================================
        tabsBar = BoxLayout(size = TABS_SIZE, size_hint = NONES,
                            orientation = 'horizontal')
        tabsBG = Image(allow_stretch = True, keep_ratio = False, source = COLOR_BODY)

        # Content Pane ==================================================================
        contentPane = RelativeLayout(size = CONT_SIZE, size_hint = NONES)
        contBG = Image(allow_stretch = True, keep_ratio = False, source = COLOR_BODY,
                       size_hint = (1.0, 1.0))

    #===================================================================================#
    # CLASS: METHODS                                                                    #
    #===================================================================================#
    def __init__(self, **kwargs):
        '''__init__(self, **kwargs): Initializes all components of app. Individual
        components will call events after being binded in this method, and they will
        handle all user input.'''
        super(MainMenu, self).__init__(**kwargs)
        print('\tINFO || DEBUG MODE == ' + str(DEBUGMODE))

        if(DEBUGMODE): print('\tINIT || Initializing...')

        # Set Button Binds
        self.SetBtnBinds()

        self.AddWidgets()

        if(DEBUGMODE): print('\tINIT || Initialization done!')

    # METHOD: Misc Methods
    #====================================================================================
    def SetBtnBinds(self):
        '''SetBtnBinds(self): Binds all button functionalities.'''
        pass

    def AddWidgets(self):
        '''AddWidgets(self): Adds all widgets to their respective parents.'''
        # Base Menu =====================================================================
        self.add_widget(self.baseBG)

        # Menu Bar ======================================================================
        self.menuBar.add_widget(self.menuBG)
        self.menuBar.add_widget(self.menuBagsBtn)
        self.menuBar.add_widget(self.menuOptsBtn)

        self.baseLayout.add_widget(self.menuBar)

        # Tabs Bar ======================================================================
        self.tabsBar.add_widget(self.tabsBG)
        #self.tabsBar.add_widget(self.tabsBG)
        #self.tabsBar.add_widget(self.tabsBG)
        #self.tabsBar.add_widget(self.tabsBG)

        self.baseLayout.add_widget(self.tabsBar)

        # Content Pane ==================================================================
        self.contentPane.add_widget(self.contBG)

        self.baseLayout.add_widget(self.contentPane)

        # Add all to core widget ========================================================
        self.add_widget(self.baseLayout)

class Builder(App):
    title = "Bag of Holding"

    def build_config(self, config):
        Config.set('graphics', 'borderless', '0')
        Config.set('graphics', 'max_fps', '42')
        Config.set('graphics', 'height', 960)
        Config.set('graphics', 'width', 540)
        Config.set('graphics', 'show_cursor', '1')
        Config.set('graphics', 'fullscreen', '0')

        Config.set('kivy', 'keyboard_mode', 'systemanddock')
        Config.set('kivy', 'window_icon', 'images/icon.png')
        Config.write()

    def build(self):
        config = self.config
        Window.clearcolor = (1,1,1,1)

        return MainMenu()

if __name__ == '__main__':
    Builder().run()
