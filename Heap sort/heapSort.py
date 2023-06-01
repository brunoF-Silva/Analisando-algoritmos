import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *
from gerarchart import *

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
folder_path = '../Vetores desordenados'
metricas = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        metricas.append(analisa_algoritmo(file_name, heap_sort, nome_algoritmo))
        
cria_json(metricas)
geraCharts()
