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

        self._lbl = Label(size_hint = NONES, size = self.size, **kwargs)
        if self.anchor_x != 'center': self._lbl.text_size[0] = self._lbl.size[0]
        if self.anchor_y != 'center': self._lbl.text_size[1] = self._lbl.size[1]

        self.add_widget(self._lbl)


    @property
    def text(self):
        return self._lbl.text


    @text.setter
    def text(self, text):
        self._lbl.text = text



class AnchorButton(AnchorLayout):
    '''Create a button from the data passed in, wrap it in a AnchorLayout, so that it
    quickly aligns without having to hassle with the textsize parameter.'''

    def __init__(self, **kwargs):
        if 'anchor_x' in kwargs:
            self.anchor_x = kwargs.pop('anchor_x')
        else:
            self.anchor_x = 'center'

        if 'anchor_y' in kwargs:
            self.anchor_y = kwargs.pop('anchor_y')
        else:
            self.anchor_y = 'center'

        if 'pos' in kwargs:
            self.pos = kwargs.pop('pos')
        else:
            self.pos = (0, 0)

        if 'size_hint' in kwargs:
            self.size_hint = kwargs.pop('size_hint')
        else:
            self.size_hint = FILLS

        if 'size' in kwargs:
            self.size = kwargs.pop('size')
        else:
            self.size = (100, 100)

        if 'image' in kwargs:
            self._image = kwargs.pop('image')
        elif 'source' in kwargs:
            self._image = Image(source = kwargs.pop('source'))
        else:
            self._image = None

        if ('allow_stretch' in kwargs) and (self._image != None):
            self._image.allow_stretch = kwargs.pop('allow_stretch')

        if ('keep_ratio' in kwargs) and (self._image != None):
            self._image.keep_ratio = kwargs.pop('keep_ratio')

        if 'background_img' in kwargs:
            self._img = kwargs.pop('background_img')
            if self._img == None:
                self._img = 'images/IMG_CLEAR.png'
        else:
            self._img = None

        super(AnchorButton, self).__init__(size_hint = self.size_hint, size = self.size,
            pos = self.pos, anchor_x = self.anchor_x, anchor_y = self.anchor_y)

        self._btn = Button(size_hint = FILLS, **kwargs)
        if self.anchor_x != 'center': self._btn.text_size[0] = self._btn.size[0]
        if self.anchor_y != 'center': self._btn.text_size[1] = self._btn.size[1]

        if self._img != None:
            self._btn.background_normal = self._btn.background_down = self._btn.background_disabled_normal = self._btn.background_disabled_down = self._img

        self.add_widget(self._btn)
        if self._image != None: self.add_widget(self._image)

    def bind(self, **kwargs):
        if 'on_press' in kwargs and len(kwargs) == 1:
            return self._btn.bind(on_press = kwargs.pop('on_press'))
        else:
            super(AnchorButton, self).bind()


    @property
    def text(self):
        return self._btn.text


    @text.setter
    def text(self, text):
        self._btn.text = text


    @property
    def image(self):
        return self._image


    @image.setter
    def image(self, newImage):
        self._image = newImage


    @property
    def itemID(self):
        return self._btn.itemID


    @itemID.setter
    def itemID(self, newID):
        self._btn.itemID = newID


class AnchorToggleButton(AnchorLayout):
    '''Create a button from the data passed in, wrap it in a AnchorLayout, so that it
    quickly aligns without having to hassle with the textsize parameter.'''

    def __init__(self, **kwargs):
        if 'anchor_x' in kwargs:
            self.anchor_x = kwargs.pop('anchor_x')
        else:
            self.anchor_x = 'center'

        if 'anchor_y' in kwargs:
            self.anchor_y = kwargs.pop('anchor_y')
        else:
            self.anchor_y = 'center'

        if 'pos' in kwargs:
            self.pos = kwargs.pop('pos')
        else:
            self.pos = (0, 0)

        if 'size_hint' in kwargs:
            self.size_hint = kwargs.pop('size_hint')
        else:
            self.size_hint = FILLS

        if 'size' in kwargs:
            self.size = kwargs.pop('size')
        else:
            self.size = (100, 100)

        if 'image' in kwargs:
            self._image = kwargs.pop('image')
        elif 'source' in kwargs:
            self._image = Image(source = kwargs.pop('source'))
        else: self._image = None

        if ('allow_stretch' in kwargs) and (self._image != None):
            self._image.allow_stretch = kwargs.pop('allow_stretch')

        if ('keep_ratio' in kwargs) and (self._image != None):
            self._image.keep_ratio = kwargs.pop('keep_ratio')

        if 'background_img' in kwargs:
            self._img = kwargs.pop('background_img')
            if self._img == None:
                self._img = 'images/IMG_CLEAR.png'
        else: self._img = None

        if 'group' in kwargs:
            self._group = kwargs.pop('group')
        else:
            self._group = None

        super(AnchorToggleButton, self).__init__(size_hint = self.size_hint, size = self.size,
            pos = self.pos, anchor_x = self.anchor_x, anchor_y = self.anchor_y)

        self._btn = ToggleButton(size_hint = FILLS, group = self._group, **kwargs)
        if self.anchor_x != 'center': self._btn.text_size[0] = self._btn.size[0]
        if self.anchor_y != 'center': self._btn.text_size[1] = self._btn.size[1]

        if self._img != None:
            self._btn.background_normal = self._btn.background_down = self._btn.background_disabled_normal = self._btn.background_disabled_down = self._img

        self.add_widget(self._btn)
        if self._image != None: self.add_widget(self._image)

    def bind(self, **kwargs):
        if 'on_press' in kwargs and len(kwargs) == 1:
            return self._btn.bind(on_press = kwargs.pop('on_press'))
        else:
            super(AnchorButton, self).bind()


    @property
    def text(self):
        return self._btn.text


    @text.setter
    def text(self, text):
        self._btn.text = text


    @property
    def image(self):
        return self._image


    @image.setter
    def image(self, newImage):
        self._image = newImage


    @property
    def group(self):
        return self._btn.group

    @group.setter
    def group(self, new_group):
        self._btn.group = new_group
