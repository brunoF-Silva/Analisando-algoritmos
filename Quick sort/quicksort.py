import sys
import os

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *


def partition(vetor, low, high):
    i = low - 1
    pivot = vetor[high]
    comparacoes = 0
    trocas = 0

    for j in range(low, high):
        comparacoes += 1
        if vetor[j] <= pivot:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
            trocas += 1

    vetor[i + 1], vetor[high] = vetor[high], vetor[i + 1]
    trocas += 1

    return i + 1, trocas, comparacoes


def quick_sort(vetor, low, high):
    trocas = 0
    comparacoes = 0

    if low < high:
        pivot_index, trocas_part, comparacoes_part = partition(
            vetor, low, high)
        trocas += trocas_part
        comparacoes += comparacoes_part

        trocas_left, comparacoes_left = quick_sort(vetor, low, pivot_index - 1)
        trocas_right, comparacoes_right = quick_sort(
            vetor, pivot_index + 1, high)

        trocas += trocas_left + trocas_right
        comparacoes += comparacoes_left + comparacoes_right

    return trocas, comparacoes


# referência para o quick_sort(vetor, 0, len(vetor) - 1)
analisa_quick_sort('1000.txt', quick_sort, "Quick sort", 0, 999) #Substitui
analisa_quick_sort('10000.txt', quick_sort, "Quick sort", 0, 9999) #Substitui

#Plotando o gráfico com os resultados
caminho = os.path.join("Quick sort", "resultados.json") # Substitui
resultados_lidos = ler_resultados(caminho)

print(resultados_lidos)

plotar_grafico(resultados_lidos)
