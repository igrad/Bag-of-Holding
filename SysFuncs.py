import kivy
kivy.require('1.9.1')

# Core
from collections import deque as Deque
import datetime

# Kivy
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.core.text import Text
from kivy.animation import Animation
from kivy.storage.jsonstore import JsonStore

from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.listview import ListView
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

NONES = (None, None)
ZEROS = (0, 0)
FILLS = (1, 1)

class SizeMap():
    def __init__(self, iw, ih, parentPair):
        self.w = iw
        self.h = ih
        self.sizePair = (self.w, self.h)
        self.hw = self.w/parentPair[0]
        self.hh = self.h/parentPair[1]
        self.hSizePair = (self.hw, self.hh)

class PosMap():
    def __init__(self, ix, iy, iw, ih, parentPair):
        self.x = ix
        self.y = iy

def PostErrorMessage(err):
    print(err)
