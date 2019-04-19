#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:52:43 2019

@author: RicardoChCz
"""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from numpy.random import randint
import imageio
from utiles import draw_pretty_graph

def generate(G):
    """
    Simula una caminata aleatoría simple en G, y obtiene un árbol usando el
    algoritmo generate.
    Input: Gráfica G (objeto en python de networkX)
    Output: Árbol T (objeto en python de networkX)
    """
    #punto inicial
    u = randint(len(G.nodes))
    visited = [u]
    T = nx.empty_graph(n)
    
    while len(visited) != len(G.nodes):
        #Obtener v vecino aleatorio de u
        N=list(G.neighbors(u))
        v = N[randint(len(N))]
        if v not in visited:
            visited.append(v)
            T.add_edge(u,v)
        #Actualiza a nuevo punto
        u=v
        
    print(T)    
    
    return T  

if __name__ == "__main__":
    """
    Generar gráfica aleatoria con ER y graficar un árbol maximal con el algorit-
    mo Generate.
    """
    n = 10
    p = 0.5
    m = 25

    G = nx.gnm_random_graph(n, m)    
    
    filenames = []
    k=15
    for i in range(0,k):
        draw_pretty_graph(G, generate(G), colors.to_hex(plt.cm.viridis(i/float(k))))
        plt.savefig('figures/RandomTree'+str(i)+'.png')
        filenames.append('figures/RandomTree'+str(i)+'.png')
        plt.show()
        
    images = []
    
    for filename in filenames:
        images.append(imageio.imread(filename))
        imageio.mimsave('figures/sample.gif', images, duration=1)