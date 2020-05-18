#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:56:02 2020

@author: 3870476
"""

from model.IRModel import IRModel
from utils.TextRepresenter import PorterStemmer
  
class ModeleLangue(IRModel):
    def __init__(self, indexer, lbda):
        self.indexer = indexer
        self.lbda = lbda 
        
    def __init__(self, indexer):
        self.indexer = indexer
    
    def getScores(self,query):            
        score = {}
        pt = PorterStemmer().getTextRepresentation(query)
        lbda = 0.8 if len(pt) < 10 else 0.2
        tfc = sum([sum(x.values()) for x in self.indexer.index.values()])
        
        for t in pt:
            if t in self.indexer.index_inv:
                for idDoc in self.indexer.index_inv[t]:  
                    ptd = (1-lbda) * (self.indexer.index[idDoc][t]/sum(self.indexer.index[idDoc].values()))
                    + lbda * (sum(self.indexer.index_inv[t].values())/tfc)
                    if idDoc in score:
                        score[idDoc] *= ptd
                    else:
                        score[idDoc] = ptd
                    
        return score
            
        
        
            
    