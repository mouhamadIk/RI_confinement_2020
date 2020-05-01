#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:19:20 2020

@author: 3870476
"""

from weighter.Weighter1 import Weighter1
from utils.TextRepresenter import PorterStemmer
import numpy as np

class Weighter3(Weighter1):
     
    def getWeightsForQuery(self,query):
        result = {}
        for token in PorterStemmer().getTextRepresentation(query):
            if token in self.indexer.index_inv:
                result[token] = np.log((1 + len(self.indexer.index)) / (1 + len(self.indexer.index_inv[token]))) 
        return result
