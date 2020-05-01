# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:51:25 2020

@author: mouha
"""

from evaluation.EvalMesure import EvalMesure

class EvalFmeasure(EvalMesure):
    
    def evalQuery(self, liste, query, k = 10, b = 1):
        P = len(set(liste[:k]) & set(query.P)) / k
        R = len(set(liste[:k]) & set(query.P)) / len(query.P)
        return (1 + b**2)*P*R / (b**2 * P + R) if P*R != 0 else 0
        