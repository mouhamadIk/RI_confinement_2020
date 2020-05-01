# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:51:25 2020

@author: mouha
"""

from evaluation.EvalMesure import EvalMesure

class EvalAvgP(EvalMesure):
    
    def evalQuery(self, liste, query):
        # nb docs pertinents retournés
        n = len(set(liste) & set(query.P))
        # nb résultats retournés
        N = len(liste)
        precisions = []
        
        for k in range(1,N):
            if liste[k] in query.P :
                precisions.append(len(set(liste[:k]) & set(query.P)) / k)        
        
        return sum(precisions)/n
        
