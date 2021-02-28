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

    if itemNotBrieCheck(item) and itemNotBackstagePassCheck(item):
        if quaityPositiveyCheck(item):
            if itemNotSulfurasCheck(item):
                item.quality = decreaseQuality(item)

    else:
        if qualityLessThanMaxQuality(item):
            item.quality = increaseQuality(item)
            if itemIsBackstagePassCheck(item):
                if sellInLessThan11Check(item):
                    if qualityLessThanMaxQuality(item):
                        item.quality = increaseQuality(item)
                if sellInLessThan6Check(item):
                    if qualityLessThanMaxQuality(item):
                        item.quality = increaseQuality(item)

    if itemNotSulfurasCheck(item):
        item.sell_in = decreaseSellIn(item)

    if sellInNegativeCheck(item):
        if itemNotBrieCheck(item):
            if itemNotBackstagePassCheck(item):
                if quaityPositiveyCheck(item):
                    if itemNotSulfurasCheck(item):
                        item.quality = decreaseQuality(item)
            else:
                item.quality = zeroQuality(item)
        else:
            if qualityLessThanMaxQuality(item):
                item.quality = increaseQuality(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
