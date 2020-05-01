# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:04:58 2019

@author: Dorian
@author: Mouhamad
"""

from .Weighter import Weighter
from indexation.TextRepresenter import PorterStemmer

class Weighter1(Weighter):
    
    def __init__(self, indexerSimple) :
        super().__init__(indexerSimple)
        
    def getWeightsForDoc(self,idDoc):
        weights = self.indexerSimple.index[idDoc].copy() if idDoc in self.indexerSimple.index else {}
        return weights        
 
    def getWeightsForStem(self,stem):
        weights = self.indexerSimple.index_inv[stem].copy() if stem in self.indexerSimple.index_inv else {}
        return weights

    def getWeightsForQuery(self,query):
        porterStemmer = PorterStemmer() 
        weights = porterStemmer.getTextRepresentation(query)
        #wt,q = 1 si t∈q , O sinon 
        for t,v in weights.items():
            if v > 1:
                weights[t] = 1
                
        return weights