from dis import dis
import heapq as hq
import random
import math
from calcularDistancia import calcularDistancia
from Leer import leerDataSet

def prim(G, agenciaViajes, inicio = 0):
    resultado = []

    dist = {}
    for viajes in agenciaViajes:
        dist[viajes.travelCode] = math.inf
    padres = {}
    for viajes in agenciaViajes:
        padres[viajes.travelCode] = ''
    visitados = {}
    for viajes in agenciaViajes:
        visitados[viajes.travelCode] = False
    q = []
    hq.heappush(q, (0, agenciaViajes[inicio].travelCode))
    while len(q) > 0:
        _,u = hq.heappop[q]
        if not visitados[u]:
            visitados[u] = True
            for w, v in G[u]:
                if not visitados[v] and w < dist[v]:
                    dist[v] = w
                    padres[v] = u
                    resultado.append((u,v))
                    hq.heappush(q, (w,v))
    return padres,dist,resultado

def generarGrafo(agenciaViajes):
    grafo = {}
    for viajes in agenciaViajes:
        grafo[viajes.travelCode] = []
    for viajes in agenciaViajes:
        copia = agenciaViajes[:]
        copia.remove(viajes)
        destinosPorViaje = random.randint(3,5)
    for _ in range(destinosPorViaje):
        destino = random.choice(copia)
        copia.remove(viajes)
        distancia = calcu
