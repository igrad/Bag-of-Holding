# Core
from collections import deque as Deque
from collections import namedtuple
from time import clock
from traceback import format_exc

# Kivy
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.core.text import Text
from kivy.animation import Animation
from kivy.storage.jsonstore import JsonStore

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.listview import ListView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stencilview import StencilView
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget

from StencilLayout import StencilLayout


# GLOBAL CONSTANTS
NONES = (None, None)
ZEROS = (0, 0)
FILLS = (1, 1)
XSCALE = 0.75
YSCALE = 0.75

#GLOBAL VARIABLES
bagsStore = JsonStore('bags_data.json')
itemStore = JsonStore('item_data.json')
optsStore = JsonStore('user_settings.json')

BAGS = dict()
ITEMS = dict()
ITEMVIEWS = dict()
FILTERS = dict()

CURRENTBAG = "0"

MAX_BAGS = 10
MAX_ITEMS = 5000
LAST_BAG_OPENED = 0
VIEW_TYPE = 'cozy'
NOOBIE_TIPS = True


# GLOBAL CLASSES
class SizeMap():
    def __init__(self, x, y, w, h, parentPair):
        self.x = int(x / XSCALE)
        self.y = int(y / YSCALE)
        self.w = int(w / XSCALE)
        self.h = int(h / YSCALE)

        self.pos = (self.x, self.y)
        self.pair = (self.w, self.h)

        self.hw = self.w/parentPair[0]
        self.hh = self.h/parentPair[1]
        self.hpair = (self.hw, self.hh)

        self.parentW = parentPair[0]
        self.parentH = parentPair[1]
        self.parentPair = parentPair


# GLOBAL METHODS
def ExtractNumber(string):
    number = ''
    for x in str(string):
        if x in '0123456789,.':
            number += x

    if number != '':
        if '.' in number: return float(number)
        return int(number)
    else:
        return string


def LogMsg(arg1):
    print('[LOG_MSG] [:::' + str(clock())[0:6] + ':::] ' + str(arg1))


def LogErr(arg1):
    print('[LOG_ERR] [:::' + str(clock())[0:6] + ':::] ' + str(arg1))


def LogExc(arg1):
    print('\n[LOG_EXC] [:::' + str(clock())[0:6] + ':::] EXCEPTION in ' + str(arg1) + '\n' + str(format_exc()))
