import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *
from gerarchart import *

### algoritmo abaixo
def shell_sort(arr):
    n = len(arr)
    gap = 1
    comparisons = 0
    swaps = 0
    
    while gap < n//3:
        gap = 3*gap + 1

    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                comparisons += 1
                swaps += 1
            
            arr[j] = temp
            swaps += 1
        
        gap //= 3

    return comparisons, swaps

nome_algoritmo = "Shell Sort"
folder_path = './Vetores desordenados'
metricas = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        metricas.append(analisa_algoritmo(file_name, shell_sort, nome_algoritmo))

cria_json(metricas)       
geraCharts()