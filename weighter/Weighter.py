#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:19:20 2020

@author: 3870476
"""

from abc import ABC, abstractmethod 
  
class Weighter(ABC): 
    
    def __init__(self, indexer):
        '''
        Constructor
        '''
        self.indexer = indexer
  
    @abstractmethod 
    def getWeightsForDoc(self,idDoc): 
        pass
    
    @abstractmethod 
    def getWeightsForStem(self,stem): 
        pass
    
    @abstractmethod 
    def getWeightsForQuery(self,query): 
        pass