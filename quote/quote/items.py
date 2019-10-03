# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class jurnalData(Item):
    title = Field()
    url = Field()


class Index(Item):
    index_by = Field()


class sintaScore(Item):
    score = Field()
    total = Field()


class scopusScore(Item):
    score = Field()
    total = Field()


class Nav(Item):
    title = Field()
    url = Field()


class Title(Item):
    title = Field()
