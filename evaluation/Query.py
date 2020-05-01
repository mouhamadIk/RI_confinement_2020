#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:40:30 2020

@author: 3870476
"""

class Query(object):

    def __init__(self, I, W, A, N):
        '''
        Constructor
        '''
        self.I = I
        self.W = W
        self.A = A
        self.N = N
        # List des id des docs pertinents
        self.P = []

    
    