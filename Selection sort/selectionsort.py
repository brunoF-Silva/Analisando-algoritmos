import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *


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

nome_algoritmo = "Selection sort"
folder_path = './Vetores desordenados'
metricas = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        metricas.append(analisa_algoritmo(file_name, selection_sort, nome_algoritmo))

cria_json(metricas)       