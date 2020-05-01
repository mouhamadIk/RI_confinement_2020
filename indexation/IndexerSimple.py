#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:35:45 2020

@author: 3870476
"""

from utils.TextRepresenter import PorterStemmer
import numpy as np
import json

class IndexerSimple(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.index = {}
        self.index_inv = {}
        
    def indexation(self, collection):        
        for k,d in collection.items():
            self.index[k] = PorterStemmer().getTextRepresentation(d.T + d.W)
            
            for token, tf in self.index[k].items():
                if token not in self.index_inv:
                    self.index_inv[token] = {k: tf}
                else:
                    self.index_inv[token][k] = tf
                    
        with open('index.txt', 'w') as file:
            file.write(json.dumps(self.index))
            
        with open('index_inv.txt', 'w') as file:
            file.write(json.dumps(self.index_inv))
    
    def getTfsForDoc(self, idDoc):
        return self.index[idDoc] if idDoc in self.index else {}
    
    def getTfIDFsForDoc(self, idDoc):
        stem_tfidf = self.getTfsForDoc(idDoc).copy()
        N = len(self.index)
        
        for token in stem_tfidf:
            df = len(self.index_inv[token])
            stem_tfidf[token] *= np.log((1+N) / (1+df))
        
        return stem_tfidf
    
    def getTfsForStem(self, stem) :
        return self.index_inv[stem] if stem in self.index_inv else {}
    
    def getTfIDFsForStem(self, stem):
        doc_tfidf = self.getTfsForStem(stem).copy()
        N = len(self.index)
        df = len(doc_tfidf)
        
        for doc in doc_tfidf:
            doc_tfidf[doc] *= np.log((1+N) / (1+df))
        
        return doc_tfidf
    
    def getStrDoc(doc):
        return doc.W
    

    
    
            
            
        
    
    
        
    