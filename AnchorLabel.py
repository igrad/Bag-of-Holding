from SysFuncs import *

class AnchorLabel(AnchorLayout):
    '''Create a label from the data passed in, wrap it in a AnchorLayout, so that it
    quickly aligns without having to hassle with the textsize parameter.'''

    def __init__(self, **kwargs):
        if 'anchor_x' in kwargs: self.anchor_x = kwargs.pop('anchor_x')
        else: self.anchor_x = 'left'
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

        self.lbl = Label(size_hint = NONES, **kwargs)
        self.lbl.text_size[0] = self.lbl.size[0]

        self.add_widget(self.lbl)