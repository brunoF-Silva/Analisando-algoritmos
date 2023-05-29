from funcoes import *
import sys
import os

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)


def selection_sort(vetor):
    comparacoes = 0
    trocas = 0

    for i in range(len(vetor)):
        indice_menor = i
        for j in range(i + 1, len(vetor)):
            comparacoes += 1
            if vetor[j] < vetor[indice_menor]:
                indice_menor = j

        if indice_menor != i:
            vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]
            trocas += 1

    return trocas, comparacoes


analisa_algoritmo('1000.txt', selection_sort, "") #Substitui
analisa_algoritmo('10000.txt', selection_sort, "") #Substitui

#Plotando o gráfico com os resultados
caminho = os.path.join("", "resultados.json") # Substitui
resultados_lidos = ler_resultados(caminho)

print(resultados_lidos)

plotar_grafico(resultados_lidos)
