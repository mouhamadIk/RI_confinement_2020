#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:56:02 2020

@author: 3870476
"""

from model.IRModel import IRModel
from utils.TextRepresenter import PorterStemmer
import numpy as np 
  
class Okapi(IRModel):
    def __init__(self, indexer, k1 = 1.2, b = 0.75):
        super().__init__(indexer)
        self.k1 = k1
        self.b = b
    
    def getScores(self,query):            
        score = {}
        pt = PorterStemmer().getTextRepresentation(query)
        avgdl = np.mean([sum(doc.values()) for doc in self.indexer.index.values()])
        
        for stem in pt:
            if stem in self.indexer.index_inv:
                idf = np.log((1+len(self.indexer.index))/(1+len(self.indexer.index_inv[stem])))
                for doc in self.indexer.index_inv[stem]:
                    tf = self.indexer.index_inv[stem][doc]
                    if doc in score:
                        score[doc] += idf*tf/(tf+self.k1*(1+self.b*(-1+sum(self.indexer.index[doc].values())/avgdl)))
                    else:
                        score[doc] = idf*tf/(tf+self.k1*(1+self.b*(-1+sum(self.indexer.index[doc].values())/avgdl)))
                        
        return score
        
        
        
        
            
    