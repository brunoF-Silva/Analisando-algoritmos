import sys
import os

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *

def insertion_sort(vetor):
    comparações = 0
    trocas = 0

    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        while j >= 0 and vetor[j] > chave:
            comparações += 1
            vetor[j + 1] = vetor[j]
            trocas += 1
            j -= 1

        vetor[j + 1] = chave

    return trocas, comparações

analisa_algoritmo('1000.txt', insertion_sort, "Insertion sort")
analisa_algoritmo('10000.txt', insertion_sort, "Insertion sort")

#Plotando o gráfico com os resultados
caminho = os.path.join("Insertion sort", "resultados.json")
resultados_lidos = ler_resultados(caminho)

print(resultados_lidos)

plotar_grafico(resultados_lidos)
