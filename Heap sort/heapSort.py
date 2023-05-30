import sys
import os

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *

### algoritmo abaixo
def heapify(vetor, n, i, comparações, trocas):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and vetor[i] < vetor[esquerda]:
        comparações += 1
        maior = esquerda

    if direita < n and vetor[maior] < vetor[direita]:
        comparações += 1
        maior = direita

    if maior != i:
        trocas += 1
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        trocas, comparações = heapify(vetor, n, maior, comparações, trocas)

    return trocas, comparações


def heap_sort(vetor):
    comparações = 0
    trocas = 0

    n = len(vetor)

    for i in range(n, -1, -1):
        trocas, comparações = heapify(vetor, n, i, comparações, trocas)

    for i in range(n - 1, 0, -1):
        trocas += 1
        vetor[i], vetor[0] = vetor[0], vetor[i]
        trocas, comparações = heapify(vetor, i, 0, comparações, trocas)

    return trocas, comparações

nome_algoritmo = "Heap sort"
analisa_algoritmo('1000.txt', heap_sort, nome_algoritmo)
analisa_algoritmo('10000.txt', heap_sort, nome_algoritmo)

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
