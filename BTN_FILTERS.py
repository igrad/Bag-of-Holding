from SysFuncs import *
from LoadSaves import *
from AppInit import *
from Bag import *
from BagItem import *

def OpenContPane_Filters(obj):
    # Do not reset any fields
    anim = Animation(pos = CONT_POS_FILTERS, duration = T_SCREENSHIFT, t = ANIMTYPE)
    anim.start(contpane)

    SaveFilters(None)

def OpenFilt_Cat(obj):
    filt_cat.open(filt_cat_pick)

def SetCat(obj):
    print('SetCat called: ' + str(obj))

    if obj == filt_cat_name:
        filt_cat.head_text = 'name'
    elif obj == filt_cat_qty:
        filt_cat.head_text = 'quantity'
    elif obj == filt_cat_weight:
        filt_cat.head_text = 'weight'
    elif obj == filt_cat_val:
        filt_cat.head_text = 'value'
    else:
        print('SetCat() did not recognize object: ' + str(obj))

def SaveFilters(obj):
    #FILTERS['name'] = filt_name.text
    #FILTERS['cat'] = filt_cat_pick
    #FILTERS['sort'] = filt_sort_pick
    #FILTERS['tags'] = []

    # TODO: Check this when applying filters to the loaded bag
    #for i in filt_tags.children: FILTERS['tags'].append(i.text)
    pass
