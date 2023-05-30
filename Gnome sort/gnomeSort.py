import sys
import os

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *

### algoritmo abaixo
def gnome_sort(vetor):
    comparações = 0
    trocas = 0
    tamanho = len(vetor)
    i = 0

    while i < tamanho:
        comparações += 1
        if i == 0 or vetor[i] >= vetor[i - 1]:
            i += 1
        else:
            vetor[i], vetor[i - 1] = vetor[i - 1], vetor[i]
            trocas += 1
            i -= 1
            if i == 0:
                i = 1

    return trocas, comparações

nome_algoritmo = "Gnome sort"
analisa_algoritmo('1000.txt', gnome_sort, nome_algoritmo)
analisa_algoritmo('10000.txt', gnome_sort, nome_algoritmo)

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
