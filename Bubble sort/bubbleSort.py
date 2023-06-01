import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *
from gerarchart import *

def bubbleSort(array):
    comparacoes = 0
    trocas = 0
    for i in range(len(array)):
        
        swapped = False
    
        for j in range(0, len(array) - i - 1):
            comparacoes += 1
            if array[j] > array[j + 1]:
                trocas += 1
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swapped = True
                
        if not swapped:
            break
    return trocas, comparacoes

nome_algoritmo = "Bubble sort"
folder_path = './Vetores desordenados'
metricas = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        metricas.append(analisa_algoritmo(file_name, bubbleSort, nome_algoritmo))

cria_json(metricas)
geraCharts()
     
