from gilded_rose import *

QUALITY_MAX = 50
SELLIN_1 = 11
SELLIN_2 = 6

def increaseQualityIfLessThanMaxQuality(item):
    if qualityLessThanMaxQuality(item):
        return increaseQuality(item)
    else:
        return item.quality

def itemNotSpecialCheck(item):
    return itemNotBrieCheck(item) and itemNotBackstagePassCheck(item) and itemNotSulfurasCheck(item)

def itemIsBrieCheck(item):
    return item.name == "Aged Brie"

def itemIsConjuredCheck(item):
    return item.name == "Conjured Mana Cake"

def itemIsBackstagePassCheck(item):
    return item.name == "Backstage passes to a TAFKAL80ETC concert"

def sellInPositiveCheck(item):
    return item.sell_in > 0

def qualityPositiveCheck(item):
    return item.quality > 0

def qualityNegativeCheck(item):
    return item.quality < 0

def qualityLessThanMaxQuality(item):
    return item.quality < QUALITY_MAX

def sellInNegativeCheck(item):
    return item.sell_in < 0

def itemNotBrieCheck(item):
    return item.name != "Aged Brie"

def itemNotBackstagePassCheck(item):
    return item.name != "Backstage passes to a TAFKAL80ETC concert"

def itemNotSulfurasCheck(item):
    return item.name != "Sulfuras, Hand of Ragnaros"

def sellInLessThan11Check(item):
    return item.sell_in < SELLIN_1

def sellInLessThan6Check(item):
    return item.sell_in < SELLIN_2

def decreaseQuality(item):
    return item.quality - 1

def decreaseQualityBy2(item):
    return item.quality - 2

def increaseQuality(item):
    return item.quality + 1

def decreaseSellIn(item):
    return item.sell_in - 1

def zeroQuality(item):
    return 0
