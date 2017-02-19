import kivy
kivy.require('1.9.1')

# Core
from collections import deque as Deque
from collections import namedtuple
from time import clock

# Kivy
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.core.text import Text
from kivy.animation import Animation
from kivy.storage.jsonstore import JsonStore

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
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


# GLOBAL CONSTANTS
NONES = (None, None)
ZEROS = (0, 0)
FILLS = (1, 1)
XSCALE = 1
YSCALE = 1

ANIMTIME = 0.50
T_SCREENSHIFT = 0.25
ANIMTYPE = 'in_out_quart'

#GLOBAL VARIABLES
bagsStore = JsonStore('bags_data.json')
itemStore = JsonStore('item_data.json')
optsStore = JsonStore('user_settings.json')

BAGS = dict()
ITEMS = dict()
ITEMVIEWS = dict()
FILTERS = dict()

CURRENTBAG = 0

MAX_BAGS = 10
MAX_ITEMS = 5000
LAST_BAG_OPENED = 0
NOOBIE_TIPS = True

# GLOBAL CLASSES
class SizeMap():
    def __init__(self, x, y, w, h, parentPair):
        self.x = x / XSCALE
        self.y = y / YSCALE
        self.w = w
        self.h = h
        self.pos = (self.x, self.y)
        self.pair = (self.w, self.h)
        self.hw = self.w/parentPair[0]
        self.hh = self.h/parentPair[1]
        self.hpair = (self.hw, self.hh)
        self.parentW = parentPair[0]
        self.parentH = parentPair[1]
        self.parentPair = parentPair


# GLOBAL METHODS
def LogMsg(text):
    processTime = clock()
    print("[" + processTime + "] " + err)
