# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:46:23 2020

@author: mouha
"""

import numpy as np

class EvalIRModel():
    
    def evalModel(self, models, measures, queries, ):
        res = []
        for model in models:
            avg_std = []
            for measure in measures:
                scores = []
                for query in queries:
                    scores.append(measure.evalQuery(list(model.getRanking(query.W).keys()),query))
                avg_std.append((np.mean(scores),np.std(scores)))
            res.append(avg_std)
        
        return res
                    