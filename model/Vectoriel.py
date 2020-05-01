#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:56:02 2020

@author: 3870476
"""

from model.IRModel import IRModel
import numpy as np 
  
class Vectoriel(IRModel): 
    
    def __init__(self, indexer, weighter, normalized = False):
        '''
        Constructor
        '''
        self.indexer = indexer
        self.weighter = weighter
        self.normalized = normalized
        self.X = {}
        self.normeX = {}  
        for idDoc in indexer.index:
            self.X[idDoc] = weighter.getWeightsForDoc(idDoc)
            self.normeX[idDoc] = sum(self.X[idDoc].values())
            
    def getScores(self,query):
        Y = self.weighter.getWeightsForQuery(query)
        normeY = sum(Y.values())
        score = {}
        
        if self.normalized:
            for stem in Y:
                for idDoc in self.indexer.index_inv[stem]:
                    if idDoc in score:
                        score[idDoc] += Y[stem]*self.X[idDoc][stem]/(np.sqrt(self.normeX[idDoc]) + np.sqrt(normeY))
                    else:
                        score[idDoc] = Y[stem]*self.X[idDoc][stem]/(np.sqrt(self.normeX[idDoc]) + np.sqrt(normeY))
        
        else:
            for stem in Y:
                    for idDoc in self.indexer.index_inv[stem]:
                        if idDoc in score:
                            score[idDoc] += Y[stem]*self.X[idDoc][stem]
                        else:
                            score[idDoc] = Y[stem]*self.X[idDoc][stem]
        
        return score
            
        
        
            
    