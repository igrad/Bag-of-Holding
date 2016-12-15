from SysFuncs import *
from BagItem import *
from SaveStores import *
from AppInit import *

IV_ICON = SizeMap(120, 120, (1030, 130))
IV_NAME = SizeMap(895, 70, (1030, 130))
IV_DESC = SizeMap(895, 50, (1030, 130))

class ItemView(Button):
    view = RelativeLayout(size_hint = FILLS)
    item = None
    dicon = Image(size = IV_ICON.sizePair, size_hint = NONES, source = 'images/none.png',
                  pos = (5, 5), allow_stretch = True, keep_ratio = False)
    dname = Label(text = 'Item Name', font_name = FONT_BASK, font_size = FONT_SIZE_A,
                  color = [0,0,0,1], size = IV_NAME.sizePair)

    def __init__(self, **kwargs):
        if 'item' in kwargs: self.item = BagItem(kwargs['item'])

        self.dicon.source = self.item.icon
        self.dname.text = self.item.name

        view.add_widget(self.dicon)
        view.add_widget(self.dname)
        
