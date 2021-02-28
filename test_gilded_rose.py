# -*- coding: utf-8 -*-
import unittest
import pytest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    '''def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("bar", items[0].name)'''

    def test_StandardItemStandardBehaviourQualityDecreaseBy1(self):
        items = [Item("Elixir of the Mongoose", 6, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_StandardItemSellByDatePassedQualityDecreaseBy2(self):
        items = [Item("Elixir of the Mongoose", -1, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)

    def test_StandardItemQualityNeverLessThan0(self):
        items = [Item("Elixir of the Mongoose", 0, -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_AgedBrieSellByDatePositiveQualityIncreaseBy1(self):
        items = [Item("Aged Brie", 3, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_AgedBrieSellByDateNegativeQualityIncreaseBy2(self):
        items = [Item("Aged Brie", -1, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    def test_StandardItemQualityNeverMoreThan50(self):
        items = [Item("Aged Brie", 3, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_SulfurasNeverChange(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 3, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_BackstagePassesSellByDateMoreThan10QualityIncreaseBy1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)

    def test_BackstagePassesSellByDateLessThan10MoreThan5QualityIncreaseBy2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 7, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)

    def test_BackstagePassesSellByDateLessThan5QualityIncreaseBy3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)

    def test_BackstagePassesSellByDateLessThan0Quality0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_ConjuredItemStandardBehaviourQualityDecreaseBy2(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_ConjuredItemSellByDatePassedQualityDecreaseBy4(self):
        items = [Item("Conjured Mana Cake", -1, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

if __name__ == '__main__':
    unittest.main()
