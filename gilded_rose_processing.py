# -*- coding: utf-8 -*-
import pytest

from processing import *

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_item(item)

def update_item(item):
    process_standard(item)

    if itemIsConjuredCheck(item):
        item.quality = process_conjured(item)

    if itemIsBackstagePassCheck(item):
        item.quality = process_backstagepasses(item)

    if itemIsBrieCheck(item):
        item.quality = process_brie(item)

    if itemNotSulfurasCheck(item):
        item.sell_in = decreaseSellIn(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
