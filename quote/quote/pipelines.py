    # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from .items import sintaScore, scopusScore, Index, jurnalData, Nav, Title

mapping = {
            scopusScore,
            sintaScore,
            Index,
            Title,
            jurnalData,
            Nav,
        }


class Titles(object):

    def __init__(self):

        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['Sinta_Website_Data']
        self.collection = db['Website']

    def process_item(self, item, spider):
        if not isinstance(item, Title):
            return item
        self.collection.insert(dict(item))



class AllData(object):

    def __init__(self):

        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['Sinta_Website_Data']
        self.collection = db['Jurnal_Data']

    def process_item(self, item, spider):
        if not isinstance(item, jurnalData):
            return item
        self.collection.insert(dict(item))


class indexPipelines(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['Sinta_Website_Data']
        self.collection = db['Jurnal_Index']

    def process_item(self, item, spider):
        if not isinstance(item, Index):
            return item
        self.collection.insert(dict(item))


class sintaScorePipelines(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['Sinta_Website_Data']
        self.collection = db['Sinta_Score']

    def process_item(self, item, spider):
        if not isinstance(item, sintaScore):
            return item
        self.collection.insert(dict(item))


class scopusScorePipelines(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['Sinta_Website_Data']
        self.collection = db['Scopus_Score']

    def process_item(self, item, spider):
        if not isinstance(item, scopusScore):
            return item
        self.collection.insert(dict(item))


class navPipelines(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['Sinta_Website_Data']
        self.collection = db['Nav']

    def process_item(self, item, spider):
        if not isinstance(item, Nav):
            return item
        self.collection.insert(dict(item))

