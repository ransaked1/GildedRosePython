from logic_checks import *

def process_conjured(item):
    #degrading twice as fast
    if sellInPositiveCheck(item):
        return decreaseQuality(item)
    else:
        return decreaseQualityBy2(item)

def process_backstagepasses(item):
    #quality increses by 2 10 days before the show
    if sellInLessThan11Check(item):
        item.quality = increaseQualityIfLessThanMaxQuality(item)

    #quality increses by 3 5 days before the show
    if sellInLessThan6Check(item):
        item.quality = increaseQualityIfLessThanMaxQuality(item)

    #quality zero after the show
    if sellInNegativeCheck(item):
        item.quality = zeroQuality(item)

    return item.quality

def process_brie(item):
    #quality increases if sellin passed
    if sellInNegativeCheck(item):
        item.quality = increaseQualityIfLessThanMaxQuality(item)

    return item.quality

def process_standard(item):
    # decrease by one if quality positive or increase it
    if itemNotSpecialCheck(item) and qualityPositiveCheck(item):
        item.quality = decreaseQuality(item)
    else:
        item.quality = increaseQualityIfLessThanMaxQuality(item)

    # decrease by two if sellin passed
    if itemNotSpecialCheck(item) and qualityPositiveCheck(item) and sellInNegativeCheck(item):
        item.quality = decreaseQuality(item)

    return item.quality
