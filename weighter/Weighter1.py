#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:19:20 2020

@author: 3870476
"""

from weighter.Weighter import Weighter
from utils.TextRepresenter import PorterStemmer

class Weighter1(Weighter):
   
    def getWeightsForDoc(self,idDoc):
        return self.indexer.getTfsForDoc(idDoc)
     
    def getWeightsForStem(self,stem): 
        return self.indexer.getTfsForStem(stem)
     
    def getWeightsForQuery(self,query):
        pt = PorterStemmer().getTextRepresentation(query)
        for token in pt:
            pt[token] = 1
        return pt
        
