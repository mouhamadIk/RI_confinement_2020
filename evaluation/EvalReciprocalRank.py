# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:51:25 2020

@author: mouha
"""

from evaluation.EvalMesure import EvalMesure

class EvalReciprocalRank(EvalMesure):
    
    def evalQuery(self, liste, query):
        if not query.P or not liste:
            return 0
        for k in range(len(liste)):
            if liste[k] in query.P:
                return 1/(k+1)
        return 0
        
