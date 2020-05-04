# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:51:25 2020

@author: mouha
"""

from evaluation.EvalMesure import EvalMesure

class EvalPrecision(EvalMesure):
    def __init__(self, k = 10):
        self.k = k
    
    def evalQuery(self, liste, query):
        k = self.k
        if self.k > len(liste) or self.k < 1:
            k = len(liste)
        return len(set(liste[:k]) & set(query.P)) / len(query.P)
        
