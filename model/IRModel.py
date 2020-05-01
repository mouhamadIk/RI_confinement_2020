#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:56:02 2020

@author: 3870476
"""

from abc import ABC, abstractmethod 
  
class IRModel(ABC): 
    
    def __init__(self, indexer):
        '''
        Constructor
        '''
        self.indexer = indexer
  
    @abstractmethod
    def getScores(self,query): 
        pass
    
    def getRanking(self,query): 
        return {k:v for k,v in sorted(self.getScores(query).items(), key=lambda s: s[1], reverse = True)}
        