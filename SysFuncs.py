import kivy
kivy.require('1.9.1')

# Core
from collections import deque as Deque
from collections import namedtuple
import datetime

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
SCALE = 2

#GLOBAL VARIABLES
bagsStore = JsonStore('bags_data.json')
itemStore = JsonStore('item_data.json')
optsStore = JsonStore('user_settings.json')

BAGS = dict()
ITEMS = dict()
ITEMVIEWS = dict()

CURRENTBAG = 0

MAX_BAGS = 10
MAX_ITEMS = 5000
LAST_BAG_OPENED = 0
NOOBIE_TIPS = True

# GLOBAL CLASSES
class SizeMap():
    def __init__(self, x, y, w, h, parentPair):
        self.x = x / SCALE
        self.y = y / SCALE
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

    def set(self, **kwargs):
        for arg in kwargs:
            if arg == 'x': self.x = kwargs.pop('x') / SCALE
            elif arg == 'x': self.y = kwargs.pop('y') / SCALE
            elif arg == 'x': self.w = kwargs.pop('w')
            elif arg == 'x': self.h = kwargs.pop('h')
            elif arg == 'x': self.pos = kwargs.pop('pos')
            elif arg == 'x': self.pair = kwargs.pop('pair')
            elif arg == 'x': self.hw = kwargs.pop('hw')
            elif arg == 'x': self.hh = kwargs.pop('hh')
            elif arg == 'x': self.hpair = kwargs.pop('hpair')
            elif arg == 'x': self.parentW = kwargs.pop('parentW')
            elif arg == 'x': self.parentH = kwargs.pop('parentH')
            elif arg == 'x': self.parentPair = kwargs.pop('parentPair')

def PostErrorMessage(err):
    print(err)
