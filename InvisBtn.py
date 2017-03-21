from SysFuncs import *

class InvisBtn(Button):
    '''Create an invisible button that otherwise behaves like a regular button.'''
    def __init__(self, **kwargs):
        self.background_normal = ''
        self.background_disabled_normal = ''
        self.background_down = ''
        self.background_disabled_down = ''

        super(InvisBtn, self).__init__(**kwargs)
