import sys
import os

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *

def bubble_sort(vetor):
    comparações = 0
    trocas = 0

    for i in range(len(vetor) - 1):
        for j in range(len(vetor) - 1 - i):
            comparações += 1
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocas += 1

    return trocas, comparações


analisa_algoritmo('1000.txt', bubble_sort, "Bubble sort")
analisa_algoritmo('10000.txt', bubble_sort, "Bubble sort")

#Plotando o gráfico com os resultados
caminho = os.path.join("Bubble sort", "resultados.json")
resultados_lidos = ler_resultados(caminho)

print(resultados_lidos)

plotar_grafico(resultados_lidos)
