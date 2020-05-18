# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:47:25 2020

@author: mouha
"""
from utils.TextRepresenter import PorterStemmer
from indexation.Parser import Parser
from indexation.IndexerSimple import IndexerSimple
from weighter.Weighter1 import Weighter1
from weighter.Weighter2 import Weighter2
from weighter.Weighter3 import Weighter3
from weighter.Weighter4 import Weighter4
from weighter.Weighter5 import Weighter5
from model.Vectoriel import Vectoriel
from model.ModeleLangue import ModeleLangue
from model.Okapi import Okapi
from sklearn.model_selection import train_test_split
from evaluation.QueryParser import QueryParser
from evaluation.EvalPrecision import EvalPrecision
from evaluation.EvalRappel import EvalRappel
from evaluation.EvalFmeasure import EvalFmeasure
from evaluation.EvalAvgP import EvalAvgP
from evaluation.EvalReciprocalRank import EvalReciprocalRank
from evaluation.EvalNDCG import EvalNDCG
from evaluation.EvalIRModel import EvalIRModel

#Heike test

text_file = open("data/cacm/cacmShort_eike.txt").read()
p = Parser()
p.buildDocCollectionRegex(text_file)

indexer = IndexerSimple()
indexer.indexation(p.collection)

qry = open("data/cacm/cacmShort_eike.qry").read()
rel = open("data/cacm/cacmShort_eike.rel").readlines()
qp = QueryParser()
qp.buildQueryCollectionRegex(qry, rel)

w = Weighter1(indexer)

m = ModeleLangue(indexer)
#print(m.getRanking("maman computation programming"))
o = Okapi(indexer)
v = Vectoriel(indexer, w, True)

e_p = EvalPrecision(-1)
e_r = EvalRappel(-1)
e_f = EvalFmeasure(-1)
e_a = EvalAvgP()
e_rr = EvalReciprocalRank()
e_n = EvalNDCG(-1)
measures = [e_p, e_r, e_f, e_a, e_rr, e_n]

models = [v, o, m]
measures = [e_p, e_r, e_f, e_a, e_rr, e_n]
queries = list(qp.collection.values())
e = EvalIRModel()
res = e.evalModel(models, measures, [qp.collection[1]])