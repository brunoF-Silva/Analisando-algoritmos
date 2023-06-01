import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *
from gerarchart import *

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
folder_path = './Vetores desordenados'
metricas = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        metricas.append(analisa_algoritmo(file_name, merge_sort, nome_algoritmo))


cria_json(metricas) 
geraCharts()
