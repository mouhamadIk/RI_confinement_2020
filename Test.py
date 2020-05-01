# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 11:27:58 2019

@author: Dorian
@author: Mouhamad
"""

from indexation.Document import Document
from indexation.Parser import Parser
from indexation.IndexerSimple import IndexerSimple
from ordonnancement.Weighter1 import Weighter1
from ordonnancement.Weighter2 import Weighter2
from ordonnancement.Weighter3 import Weighter3
from ordonnancement.Weighter4 import Weighter4
from ordonnancement.Weighter5 import Weighter5
from ordonnancement.IRModel import IRModel
from ordonnancement.Okapi import Okapi
from ordonnancement.ModeleLangue import ModeleLangue
from ordonnancement.Vectoriel import Vectoriel
from evaluation.QueryParser import QueryParser
from evaluation.Query import Query
from evaluation.EvalMesurePrecision import EvalMesurePrecision
from evaluation.EvalMesurePrecisionMoyenne import EvalMesurePrecisionMoyenne
from evaluation.EvalMesureReciprocalRank import EvalMesureReciprocalRank
from evaluation.EvalMesureRappel import EvalMesureRappel
from evaluation.EvalMesureFMeasure import EvalMesureFMeasure
from evaluation.EvalMesureNDCG import EvalMesureNDCG
from evaluation.EvalIRModel import EvalIRModel
from evaluation.PageRank import PageRank

###############################################################################

file_cacm = open("data/cacm/cacm.txt","r")
content_cacm = file_cacm.read()
#file_cisi = open("data/cisi/cisi.txt","r")
#content_cisi = file_cisi.read()

parse_cacm = Parser(content_cacm)
documents_cacm = parse_cacm.parse()
#parse_cisi = Parser(content_cisi)
#documents_cisi = parse_cisi.parse()
          
index_cacm = IndexerSimple("cacm")
index_cacm.indexation(documents_cacm)
index_cacm_dict = index_cacm.index
indinv_cacm_dict = index_cacm.index_inv
#index_cisi = IndexerSimple("cisi")
#index_cisi.indexation(documents_cisi)

query_cacm = open("data/cacm/cacm.qry","r")
pertinence_cacm = open("data/cacm/cacm.rel","r")

content_cacm_q = query_cacm.read()
content_cacm_pert = pertinence_cacm.read()

parse_cacm_q = QueryParser(content_cacm_q,content_cacm_pert)
requetes_cacm = parse_cacm_q.parse()

#modèles
ml = ModeleLangue(index_cacm)
oka = Okapi(index_cacm)
w = Weighter1(index_cacm)
v = Vectoriel(index_cacm,w,False)

#métriques
precision = EvalMesurePrecision() 
rappel = EvalMesureRappel()
fmeasure = EvalMesureFMeasure()
reciprocal_rank = EvalMesureReciprocalRank()
ndcg = EvalMesureNDCG()
precision_moy = EvalMesurePrecisionMoyenne()

#comparaison modèles avec métriques
pRank = PageRank(index_cacm)
#scores_pr = pRank.pageRank([doc_id for doc_id,score in v.getRanking(requetes_cacm['1'].W)],3,3)
#eval_queries,eval_moyecart = EvalIRModel(requetes_cacm,[oka,v],[precision,rappel,fmeasure,ndcg],["Okapi-BM25","Vectoriel_W1"],["Precision","Rappel","FMeasure","NDCG"]).eval()
eval_queries_pr,eval_moyecart_pr = EvalIRModel(requetes_cacm,[ml,v],[precision,rappel,fmeasure,ndcg],["Modele Langue","Vectoriel_W1"],["Precision","Rappel","FMeasure","NDCG"]).evalWithPageRank(pRank)