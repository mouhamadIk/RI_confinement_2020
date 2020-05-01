#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:19:20 2020

@author: 3870476
"""

from weighter.Weighter3 import Weighter3
from utils.TextRepresenter import PorterStemmer
import numpy as np

class Weighter4(Weighter3):
        
    def getWeightsForDoc(self, idDoc):
        results = {}
        for token, tf in self.indexer.getTfsForDoc(idDoc).items():
            results[token] = 1 + np.log(tf)
        return results
    
    def getWeightsForStem(self, stem):
        results = {}
        for doc, tf in self.indexer.getTfsForStem(stem).items():
            results[doc] = 1 + np.log(tf)
        return results
