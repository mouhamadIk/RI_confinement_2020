#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:53:24 2020

@author: 3870476
"""

import re
from indexation.Document import Document

class Parser(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.collection = {}
        
        
    def buildDocCollectionRegex(self, text):
        corpus = re.split(r'\.I ', text)
        corpus.pop(0)
        for doc in corpus:
            contents = re.split(r'\.[TBANKWX]', doc)
            balises = re.findall(r'\.[TBANKWX]', doc)            
            I = int(contents.pop(0))
            T = B = A = N = K = W = X = ""
            for i in range(len(balises)):
                if balises[i] == ".T":
                    T = contents[i]
                if balises[i] == ".B":
                    B = contents[i]
                if balises[i] == ".A":
                    A = contents[i]
                if balises[i] == ".N":
                    N = contents[i]
                if balises[i] == ".K":
                    K = contents[i]
                if balises[i] == ".W":
                    W = contents[i]
                if balises[i] == ".X":
                    X = contents[i]
                
            self.collection[I] = Document(I, T, B, A, N, K, W, X)
        
        
        
        