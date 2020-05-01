#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:19:20 2020

@author: 3870476
"""

from weighter.Weighter import Weighter
from utils.TextRepresenter import PorterStemmer
import numpy as np

class Weighter5(Weighter):
        
    def getWeightsForDoc(self, idDoc):
        results = {}
        for token, tf in self.indexer.getTfsForDoc(idDoc).items():
            results[token] = (1 + np.log(tf)) * ( np.log((1 + len(self.indexer.index)) / (1 + len(self.indexer.index_inv[token]))) )
        return results
    
    def getWeightsForStem(self, stem):
        results = {}
        for doc, tf in self.indexer.getTfsForStem(stem).items():
            results[doc] = (1 + np.log(tf)) * ( np.log((1 + len(self.indexer.index)) / (1 + len(self.indexer.index_inv[stem]))) )
        return results
    
    def getWeightsForQuery(self,query):
        result = {}
        for token, tf in PorterStemmer().getTextRepresentation(query).items():
            if token in self.indexer.index_inv:
                result[token] =  ( 1 + np.log(tf) ) * ( np.log((1 + len(self.indexer.index)) / (1 + len(self.indexer.index_inv[token]))) )
        return result
