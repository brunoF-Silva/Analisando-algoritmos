import sys
import os

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from funcoes import *

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
analisa_algoritmo('1000.txt', comb_sort, nome_algoritmo)
analisa_algoritmo('10000.txt', comb_sort, nome_algoritmo)

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
