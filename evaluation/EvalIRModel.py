# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:46:23 2020

@author: mouha
"""

import numpy as np
from numpy import unravel_index
from scipy import stats
from model.ModeleLangue import ModeleLangue
from model.Okapi import Okapi
from evaluation.EvalAvgP import EvalAvgP
from sklearn.model_selection import train_test_split



class EvalIRModel():
    
    def score(self, model, mesure, queries):
        return [mesure.evalQuery(list(model.getRanking(q.W).keys()),q) for q in queries]
    
    def evalModel(self, models, measures, queries):
        res = []
        for model in models:
            avg_std = []
            for measure in measures:
                score = self.score(model, measure, queries)
                avg_std.append([np.mean(score),np.std(score)])
            res.append(avg_std)
        
        return res
    
    def t_test(self, model1, model2, mesure, queries):
        score1 = self.score(model1, mesure, queries)
        score2 = self.score(model2, mesure, queries)      
        return stats.ttest_rel(score1, score2)
        
    def learnModelLangue_grid(self, indexer, queries):
        X_train, X_test = train_test_split(queries, test_size=0.20, random_state=42)
        means = []
        for lbda in np.arange(0, 1, 0.1):
            m = ModeleLangue(indexer, lbda)
            mAP = np.mean(self.score(m, EvalAvgP(), X_train))
            means.append(mAP)
            print("Pour lambda = " + str(lbda) + ", on obtient une mAP de " + str(means[-1]))
        print(means)
        
        
    def learnOkapi_grid(self, indexer, queries) :
        X_train, X_test = train_test_split(queries, test_size=0.20, random_state=42)
        
        values_k1 = np.arange(0, 3.2, 0.2)
        values_b = np.arange(0,1.1,0.1)
        
        gridsearch = np.zeros((len(values_k1),len(values_b)))
        
        for i in range(len(values_k1)):
            k1 = values_k1[i]
            for j in range(len(values_b)):
                b = values_b[j]
                o = Okapi(indexer, k1, b)
                mAP = np.mean(self.score(o, EvalAvgP(), X_train))
                gridsearch[i,j] = mAP
        
        #retourne les indices x,y du max dans la matrice gridsearch            
        x,y = unravel_index(gridsearch.argmax(), gridsearch.shape)
                
        best_k1 = values_k1[x]
        best_b = values_b[y]
        print("mAP max = ",gridsearch[x,y])
        print("les meilleurs paramètres","k1",best_k1,"b",best_b)
        
        #on applique les params sur le test
        o = Okapi(indexer, best_k1, best_b)
        mAP = np.mean(self.score(o, EvalAvgP(), X_test))
        print("Calcul du mAP sur le test =", mAP)
        print("AvgP : ", self.score(o, EvalAvgP(), X_test))
        
        return values_k1[x],values_b[y], gridsearch
        