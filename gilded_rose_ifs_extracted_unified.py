# -*- coding: utf-8 -*-
import pytest

from logic_checks import *

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_item(item)

def update_item(item):
    if itemIsConjuredCheck(item):
        if sellInPositiveCheck(item):
            item.quality = decreaseQuality(item)
        else:
            item.quality = decreaseQualityBy2(item)

    if itemNotSpecialCheck(item) and qualityPositiveCheck(item):
        item.quality = decreaseQuality(item)
    else:
        item.quality = increaseQualityIfLessThanMaxQuality(item)

    if itemIsBackstagePassCheck(item) or qualityNegativeCheck(item):
        if sellInLessThan11Check(item):
            item.quality = increaseQualityIfLessThanMaxQuality(item)
        if sellInLessThan6Check(item):
            item.quality = increaseQualityIfLessThanMaxQuality(item)

    if itemNotSulfurasCheck(item):
        item.sell_in = decreaseSellIn(item)

    if sellInNegativeCheck(item) and itemIsBrieCheck(item):
        item.quality = increaseQualityIfLessThanMaxQuality(item)

    if sellInNegativeCheck(item) and itemIsBackstagePassCheck(item):
        item.quality = zeroQuality(item)

    if sellInNegativeCheck(item) and itemNotSpecialCheck(item) and qualityPositiveCheck(item):
        item.quality = decreaseQuality(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
