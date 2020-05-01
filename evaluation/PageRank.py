# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:33:54 2019

@author: Dorian
@author: Mouhamad
"""

import numpy as np
import random

class PageRank:
    
    def __init__(self, index):
        self.index = index
    
    def getSubGraph(self, candidates, n, k) :
        """ determiner le sous graphe G_Q = (V_Q,E_Q)"""
        #k = nb lien entrant à considerer pour chaque doc seed (PREV)
        #n = nb doc seeds à considerer ()
        #tous les docs pointé par chaque seed (NEXT)
        
        #si len(candidates) < n alors on prend seulement len(candidates) seeds
        seeds = candidates[:min(n,len(candidates))]
        #print("seeds",seeds)
        #print("len seeds",len(seeds))
        #noeuds considérés pour le sous graphes
        V_Q = []        

        #Pour chaque doc D dans S
        #ajout dans V_Q de tous les docs pointés par D et 
        #de k documents choisis random parmis ceux pointant vers D
        
        for d in seeds :
            #docs pointés par d
            #{id:nb liens}
            #print("seed:",d)
            doc_next = self.index.getHyperlinksTo(d)
            doc_id_next = list(doc_next.keys())
            #print("doc_next",doc_next)
            #docs qui pointent vers d
            doc_prev = self.index.getHyperlinksFrom(d)
            doc_id_prev = list(doc_prev.keys())
            #print("doc_prev",doc_prev)
            
            k_random_doc_prev = []
            
            #print("k =",k)
            if len(doc_id_prev) <= k :
                #print("len(doc_id_prev)<=k")
                k_random_doc_prev = doc_id_prev
                
            else :
                id_random = list(random.sample(range(len(doc_id_prev)), k))
                #print("id_random",id_random)
                #print("len id_random",len(id_random))
                k_random_doc_prev = [doc_id_prev[i] for i in id_random]
                
            #print("krandom",k_random_doc_prev)
            
        
            V_Q += doc_id_next + k_random_doc_prev
    

        return self.reconstituationLinksSubgraph(set(V_Q))
 
    def reconstituationLinksSubgraph(self, nodes):
    
        ################################################
        ############ RECONSTITUTION GRAPHE #############
        ################################################
        """nodes = set()
        for noeud, noeuds in V_Q.items():
            nodes |= set(noeud) | set(noeuds)
        """
        #on construit un set (valeurs uniques) qui contiendra tous les noeuds
        #considérés pour le sous graphes
        list_nodes = list(nodes)
        #print("set node",nodes)
        n = len(nodes)
        #print("n = ",n)
        
        
        subgraph_indexHyperlinksFrom = {}
        subgraph_indexHyperlinksTo = {}
        
        for node_sub in list_nodes :
            
            #docs pointés par d
            #{id:nb liens}
            doc_next = self.index.getHyperlinksTo(node_sub)
            doc_id_next = list(doc_next.keys())
            #print("doc_next",doc_next)
            #docs qui pointent vers d
            doc_prev = self.index.getHyperlinksFrom(node_sub)
            doc_id_prev = list(doc_prev.keys())
            #print("doc_prev",doc_prev)
            
            
            nodes_prev_in_set = list(nodes.intersection(set(doc_id_prev)))
            #intersection1 = nodes.intersection(set(doc_id_prev))
            #print("nodes prev in set",intersection1)
            linksFrom = {}
            for n_p in nodes_prev_in_set :
                linksFrom[n_p] = doc_prev[n_p]
            subgraph_indexHyperlinksFrom[node_sub] = linksFrom
            
            
            nodes_next_in_set = list(nodes.intersection(set(doc_id_next)))
            #intersection2 = nodes.intersection(set(doc_id_next))
            #print("nodes next in set",intersection2)
            linksTo = {}
            for n_n in nodes_next_in_set :
                linksTo[n_n] = doc_next[n_n]
            subgraph_indexHyperlinksTo[node_sub] = linksTo

        return subgraph_indexHyperlinksTo,subgraph_indexHyperlinksFrom, nodes
        
        
    def pageRank(self,candidates, n, k, max_iter=100, d = 0.85, a = 1, e = 0.0001) :
        
        #correspond à la matrice A
        # A B C D
        #A1 0 1 0    A pointe vers A et C
        #B1 5 3 1
        #C7 8 0 1    C pointe vers A (7 fois)
        #D1 1 1 0
        #
        
        #prev, next, noeuds
        linkFrom, linkTo, nodes = self.getSubGraph(candidates,n,k)
              
        #print("linkFrom",linkFrom)
        #print("linkTo",linkTo)
        
        # D correspond aux nombres de liens sortants du noeud considéré
        # donc on regarde que dans linkTo (sum des values d'un noeud)
        
        # P correspond A[i,j] / D[]
        
        ite = 0
        
        #ancien
        St = {node : 1/n for node in nodes}
        #courant
        Stplus1 = {node : 0 for node in nodes}
        
        diff = 1
        
        #a revoir condition de la boucle
        #pour juste s'occuper de la convergence
        while diff >= e and max_iter > ite:
            for j in nodes:
                #sj = d * sum(pijsi) + (1-d)*a
                #on recupere tous les noeuds qui pointent vers j 
                #tous les sommets i vers j
                s = 0
                for i,aij in linkFrom[j].items() :
                    
                    di = sum(linkTo[i].values())
                    sti = St[i]
                    
                    if di == 0 :
                        s += 0
                    else :
                        s += sti * (aij / di)
                
                Stplus1[j] = d * s + (1-d)*a
                  
            #normalisation
            somme = sum(Stplus1.values())
            for i in nodes:
                Stplus1[i] /= somme
                
            #convergence
            diff = sum([np.abs(Stplus1[node] - St[node]) for node in nodes])
            
            St = Stplus1.copy()
            ite += 1
            
            
        #print("iteration",ite)
        
        return sorted(Stplus1.items(), key = lambda score : score[1], reverse = True)