#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:09:13 2019

@author: RicardoChCz
"""
import networkx as nx
import matplotlib.pyplot as plt

def draw_pretty_graph(G, subgraph = nx.empty_graph(0), e_color='orange'):
        #Position of vertices
        pos=nx.circular_layout(G)
        #Size
        fig = plt.figure(figsize=(8, 8))
        #Background
        fig.set_facecolor('white')
        #Edges
        nx.draw_networkx_edges(G, pos, alpha=0.8, edge_color='#020a18')

        #Vertices
        nx.draw_networkx_nodes(G, pos,
                               node_size=80, #Tamaño de nodos
                               node_color='#ffc000') #Define los colores
        
        plt.xlim(-1.05, 1.2)
        plt.ylim(-1.05, 1.05)
        plt.axis('off')
        nx.draw_networkx_edges(subgraph, pos, alpha=0.8, edge_color=e_color, width=2)
