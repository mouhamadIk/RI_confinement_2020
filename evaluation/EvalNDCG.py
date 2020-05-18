# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:51:25 2020

@author: mouha
"""

from evaluation.EvalMesure import EvalMesure
import numpy as np

class EvalNDCG(EvalMesure):
    def __init__(self, p = 10):
        self.p = p
    
    def evalQuery(self, liste, query):
        if not query.P or not liste:
            return 0
        p = self.p
        if self.p > len(liste) or self.p < 1:
            p = len(liste)
        
        dcgp = 0
        idcgp = 0        
        i = 0
        
        for k in range(p):
            if liste[k] in query.P:
                dcgp += 1 / np.log2(k+2)
                idcgp += 1 / np.log2(i+2)
                i += 1
        
        if idcgp == 0:
            return 0
        
        return dcgp/idcgp
