# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:46:23 2020

@author: mouha
"""

from abc import ABC, abstractmethod 


class EvalMesure(ABC):
    
    @abstractmethod
    def evalQuery(self, liste, query):
        pass