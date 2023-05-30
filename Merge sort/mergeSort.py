import sys
import os

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *

### algoritmo abaixo


def merge_sort(vetor):
    comparações = 0
    trocas = 0

    if len(vetor) > 1:
        meio = len(vetor) // 2
        esquerda = vetor[:meio]
        direita = vetor[meio:]

        comparações += 1
        trocas, comparações = merge_sort(esquerda)
        trocas, comparações = merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            comparações += 1
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
                trocas += 1
            k += 1

        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1

    return trocas, comparações

nome_algoritmo = "Merge sort"
analisa_algoritmo('1000.txt', merge_sort, nome_algoritmo)
analisa_algoritmo('10000.txt', merge_sort, nome_algoritmo)

#Plotando o gráfico com os resultados
caminho = os.path.join(nome_algoritmo, "resultados_tempo.json")
resultados_lidos = ler_resultados(caminho)
plotar_grafico(resultados_lidos, "Tempo de execução (s)")

caminho = os.path.join(nome_algoritmo, "resultados_trocas.json")
resultados_lidos = ler_resultados(caminho)
plotar_grafico(resultados_lidos, "Trocas")

caminho = os.path.join(nome_algoritmo, "resultados_comparacoes.json")
resultados_lidos = ler_resultados(caminho)
plotar_grafico(resultados_lidos, "Comparações")
