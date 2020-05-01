# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:51:25 2020

@author: mouha
"""

from evaluation.EvalMesure import EvalMesure

class EvalPrecision(EvalMesure):
    
    def evalQuery(self, liste, query, k):
        return len(set(liste[:k]) & set(query.P)) / k
        
