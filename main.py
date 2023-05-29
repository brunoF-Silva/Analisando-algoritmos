from funcoes import *
import sys
import os

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

### algoritmo abaixo



analisa_algoritmo('1000.txt', _sort, " sort")
analisa_algoritmo('10000.txt', _sort, " sort")

#Plotando o gráfico com os resultados
caminho = os.path.join(" sort", "resultados.json")
resultados_lidos = ler_resultados(caminho)

print(resultados_lidos)

plotar_grafico(resultados_lidos)
