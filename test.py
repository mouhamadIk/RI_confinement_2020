#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:55:45 2020

@author: 3870476
"""

from utils.TextRepresenter import PorterStemmer
from indexation.Parser import Parser
from indexation.IndexerSimple import IndexerSimple
from weighter.Weighter1 import Weighter1
from weighter.Weighter2 import Weighter2
from weighter.Weighter3 import Weighter3
from weighter.Weighter4 import Weighter4
from weighter.Weighter5 import Weighter5
from model.Vectoriel import Vectoriel
from model.ModeleLangue import ModeleLangue
from model.Okapi import Okapi
from sklearn.model_selection import train_test_split


docs = ["the new home has been saled on top forecasts",
        "the home sales rise in july",
        "there is an increase in home sales in july",
        "july encounter a new home sales rise"]





pt = PorterStemmer()

d = pt.getTextRepresentation(docs[0])

text_file = open("data/cacm/cacmShort-good.txt").read()



p = Parser()
p.buildDocCollectionRegex(text_file)

indexer = IndexerSimple()
indexer.indexation(p.collection)
stem_tfidf = indexer.getTfIDFsForDoc(2)
doc_tfidf = indexer.getTfIDFsForStem("comput")


w = Weighter5(indexer)

m = ModeleLangue(indexer)
print(m.getRanking("maman computation programming"))
