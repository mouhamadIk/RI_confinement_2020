# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:51:25 2020

@author: mouha
"""

from evaluation.EvalMesure import EvalMesure
import numpy as np

class EvalNDCG(EvalMesure):
    
    def evalQuery(self, liste, query, p = 10):
        if p > len(liste):
            p = len(liste)
        dcgp = 0
        idcgp = 0
        i = 0
        for k in range(p):
            if liste[k] in query.P:
                dcgp += 1 / np.log2(k+2)
                idcgp += 1 / np.log2(i+2)
                i += 1
        for k in range(i,p):
            idcgp += 1 / np.log2(i+2)
            
        return dcgp/idcgp 
        
