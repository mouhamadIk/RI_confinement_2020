#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:19:20 2020

@author: 3870476
"""

from weighter.Weighter1 import Weighter1
from utils.TextRepresenter import PorterStemmer

class Weighter2(Weighter1):
     
    def getWeightsForQuery(self,query):
        return PorterStemmer().getTextRepresentation(query)
        
