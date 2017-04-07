from SysFuncs import *

class AnchorLabel(AnchorLayout):
    '''Create a label from the data passed in, wrap it in a AnchorLayout, so that it
    quickly aligns without having to hassle with the textsize parameter.'''

    def __init__(self, **kwargs):
        if 'anchor_x' in kwargs: self.anchor_x = kwargs.pop('anchor_x')
        else: self.anchor_x = 'center'
        if 'anchor_y' in kwargs: self.anchor_y = kwargs.pop('anchor_y')
        else: self.anchor_y = 'center'
        if 'pos' in kwargs: self.pos = kwargs.pop('pos')
        else: self.pos = (0, 0)
        if 'size_hint' in kwargs: self.size_hint = kwargs.pop('size_hint')
        else: self.size_hint = FILLS
        if 'size' in kwargs: self.size = kwargs.pop('size')
        else: self.size = (100, 100)

        super(AnchorLabel, self).__init__(size_hint = self.size_hint, size = self.size,
            pos = self.pos, anchor_x = self.anchor_x, anchor_y = self.anchor_y)

        self._lbl = Label(size_hint = NONES, **kwargs)
        if self.anchor_x != 'center': self._lbl.text_size[0] = self._lbl.size[0]
        if self.anchor_y != 'center': self._lbl.text_size[1] = self._lbl.size[1]

        self.add_widget(self._lbl)

    @property
    def text(self):
        return self._lbl.text

    @text.setter
    def text(self, text):
        self._lbl.text = text

class AnchorButton(ButtonBehavior, AnchorLayout):
    '''Create a button from the data passed in, wrap it in a AnchorLayout, so that it
    quickly aligns without having to hassle with the textsize parameter.'''

    def __init__(self, **kwargs):
        if 'anchor_x' in kwargs: self.anchor_x = kwargs.pop('anchor_x')
        else: self.anchor_x = 'center'
        if 'anchor_y' in kwargs: self.anchor_y = kwargs.pop('anchor_y')
        else: self.anchor_y = 'center'
        if 'pos' in kwargs: self.pos = kwargs.pop('pos')
        else: self.pos = (0, 0)
        if 'size_hint' in kwargs: self.size_hint = kwargs.pop('size_hint')
        else: self.size_hint = FILLS
        if 'size' in kwargs: self.size = kwargs.pop('size')
        else: self.size = (100, 100)

        super(AnchorButton, self).__init__(size_hint = self.size_hint, size = self.size,
            pos = self.pos, anchor_x = self.anchor_x, anchor_y = self.anchor_y)

        self._btn = Button(size_hint = FILLS, **kwargs)
        if self.anchor_x != 'center': self._btn.text_size[0] = self._btn.size[0]
        if self.anchor_y != 'center': self._btn.text_size[1] = self._btn.size[1]

        self.add_widget(self._btn)

    @property
    def text(self):
        return self._btn.text

    @text.setter
    def text(self, text):
        self._btn.text = text
