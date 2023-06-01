import sys

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

nome_algoritmo = "Insertion sort"
folder_path = './Vetores desordenados'
metricas = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        metricas.append(analisa_algoritmo(file_name, insertion_sort, nome_algoritmo))

cria_json(metricas)       
