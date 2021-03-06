#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:55:45 2020

@author: 3870476
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
from evaluation.QueryParser import QueryParser
from evaluation.EvalPrecision import EvalPrecision
from evaluation.EvalRappel import EvalRappel
from evaluation.EvalFmeasure import EvalFmeasure
from evaluation.EvalAvgP import EvalAvgP
from evaluation.EvalReciprocalRank import EvalReciprocalRank
from evaluation.EvalNDCG import EvalNDCG
from evaluation.EvalIRModel import EvalIRModel


text_file = open("data/cacm/cacm.txt").read()
p = Parser()
p.buildDocCollectionRegex(text_file)

indexer = IndexerSimple()
indexer.indexation(p.collection)

w = Weighter5(indexer)

m = ModeleLangue(indexer)
#print(m.getRanking("maman computation programming"))
o = Okapi(indexer)
v = Vectoriel(indexer, w)


qry = open("data/cacm/cacm.qry").read()
rel = open("data/cacm/cacm.rel").readlines()
qp = QueryParser()
qp.buildQueryCollectionRegex(qry, rel)

query = qp.collection[40]
ranking = o.getRanking(query.W)
liste = list(ranking.keys())

e_p = EvalPrecision()
e_r = EvalRappel()
e_f = EvalFmeasure()
e_a = EvalAvgP()
e_rr = EvalReciprocalRank()
e_n = EvalNDCG()
print(e_n.evalQuery(liste, query))

models = [m, o, v]
measures = [e_p, e_r, e_f, e_a, e_rr, e_n]
queries = list(qp.collection.values())
e = EvalIRModel()
res = e.evalModel(models, measures, queries)

t_test = e.t_test(o, v, e_f, queries)

#e.learnModelLangue(indexer, queries)

best_k1, best_b, grid_okapi = e.learnOkapi_grid(indexer, queries)
# k1 = 3 et b = 0.6


