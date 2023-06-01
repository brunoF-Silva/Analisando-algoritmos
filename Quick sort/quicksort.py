import sys

sys.setrecursionlimit(1000000)

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *
from gerarchart import *

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    comparacoes = 0
    trocas = 0

    while True:
        while low <= high and array[high] >= pivot:
            comparacoes += 1
            high = high - 1

        while low <= high and array[low] <= pivot:
            comparacoes += 1
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
            trocas += 1

        else:

            break

    array[start], array[high] = array[high], array[start]
    trocas += 1

    return high, trocas, comparacoes

def quick_sort(array, start, end):
    trocas = 0
    comparacoes = 0
    if start >= end:
        comparacoes += 1
        return

    p, trocas_part, comparacoes_part = partition(array, start, end)
    trocas += trocas_part
    comparacoes += comparacoes_part
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

    trocas += 2*trocas
    comparacoes +=  2*comparacoes
    
    return trocas, comparacoes


nome_algoritmo = "Quick sort"
folder_path = './Vetores desordenados'
metricas = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        metricas.append(analisa_quick_sort(file_name, quick_sort, nome_algoritmo))
        
cria_json(metricas)
geraCharts()