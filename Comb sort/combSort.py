import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *
from gerarchart import *

### algoritmo abaixo
def comb_sort(vetor):
    comparações = 0
    trocas = 0
    tamanho = len(vetor)
    lacuna = tamanho
    fator_encolhimento = 1.3
    troca_realizada = True

    while lacuna > 1 or troca_realizada:
        lacuna = int(lacuna / fator_encolhimento)
        if lacuna < 1:
            lacuna = 1

        troca_realizada = False

        for i in range(tamanho - lacuna):
            comparações += 1
            if vetor[i] > vetor[i + lacuna]:
                vetor[i], vetor[i + lacuna] = vetor[i + lacuna], vetor[i]
                trocas += 1
                troca_realizada = True

    return trocas, comparações

nome_algoritmo = "Comb sort"
folder_path = './Vetores desordenados'
metricas = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        metricas.append(analisa_algoritmo(file_name, comb_sort, nome_algoritmo))

cria_json(metricas)       
geraCharts()