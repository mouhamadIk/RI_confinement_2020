#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:53:24 2020

@author: 3870476
"""

import re
from evaluation.Query import Query

class QueryParser(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.collection = {}
        
        
    def buildQueryCollectionRegex(self, qry, rel):
        corpus = re.split(r'\.I ', qry)
        corpus.pop(0)
        for q in corpus:
            contents = re.split(r'\.[WAN]', q)
            balises = re.findall(r'\.[WAN]', q)            
            I = int(contents.pop(0))
            W = A = N = ""
            for i in range(len(balises)):
                if balises[i] == ".W":
                    W = contents[i]
                if balises[i] == ".A":
                    A = contents[i]
                if balises[i] == ".N":
                    N = contents[i]
        
            self.collection[I] = Query(I, W, A, N)
        
        for r in rel:
            r=r.split()
            self.collection[int(r[0])].P.append(int(r[1]))
        