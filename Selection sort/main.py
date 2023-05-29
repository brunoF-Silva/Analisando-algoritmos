
import time
import json
import os
import matplotlib.pyplot as plt


def selection_sort(vetor):
    comparações = 0
    trocas = 0

    for i in range(len(vetor)):
        indice_menor = i
        for j in range(i + 1, len(vetor)):
            comparações += 1
            if vetor[j] < vetor[indice_menor]:
                indice_menor = j

        if indice_menor != i:
            vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]
            trocas += 1

    return trocas, comparações


def ler_vetor_do_arquivo(nome_arquivo):
    vetor = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            elemento = int(linha.strip())
            vetor.append(elemento)
    return vetor


def salvar_vetor_em_arquivo(vetor, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for elemento in vetor:
            arquivo.write(str(elemento) + '\n')


def ler_resultados(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        resultados = json.load(arquivo)
    return resultados


def plotar_grafico(resultados):
    tamanhos = []
    tempos = []

    for tamanho, tempo in resultados.items():
        tamanhos.append(int(tamanho))
        tempos.append(tempo)

    plt.plot(tamanhos, tempos, 'b-')
    plt.title('Tempo de execução em relação ao tamanho da entrada')
    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Tempo de execução (s)')
    plt.show()


# Leitura do vetor gerado anteriormente

arquivo = os.path.join("Vetores desordenados", "1000.txt")
vetor = ler_vetor_do_arquivo(arquivo)

# Ordenação do vetor e contagem de tempo, trocas e comparações
inicio = time.time()
trocas, comparações = selection_sort(vetor)
fim = time.time()
tempo_execucao = fim - inicio

print("Tempo de execução: {:.6f} segundos".format(tempo_execucao))
print("Quantidade de trocas: {}".format(trocas))
print("Quantidade de comparações: {}".format(comparações))

# Salvando o vetor ordenado em outro arquivo
salvar_vetor_em_arquivo(vetor, 'vetor_ordenado.txt')

# Criação dos resultados no formato JSON
resultados = {str(len(vetor)): tempo_execucao}

# Salvando os resultados em um arquivo JSON
with open('resultados.json', 'w') as arquivo:
    json.dump(resultados, arquivo)

# Plotando o gráfico com os resultados
resultados_lidos = ler_resultados('resultados.json')
print(resultados_lidos)
plotar_grafico(resultados_lidos)
