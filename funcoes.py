import time
import json
import os
import matplotlib.pyplot as plt


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
    resultados = []
    with open(nome_arquivo, 'r') as arquivo:
        for line in arquivo:
            objeto_json = json.loads(line.strip())
            resultados.append(objeto_json)
    return resultados


def plotar_grafico(resultados):
    tamanhos = []
    tempos = []

    for elemento in resultados:
        for tamanho, tempo in elemento.items():
            tamanhos.append(int(tamanho))
            tempos.append(tempo)

    plt.plot(tamanhos, tempos, 'b-')
    plt.title('Tempo de execução em relação ao tamanho da entrada')
    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Tempo de execução (s)')
    plt.show()


def analisa_algoritmo(nome_vetor, algoritmo_ordenacao, nome_algoritmo): #vetor escolhido, funçao do alogoritmo, nome em maiúsculo da pasta
    caminho = os.path.join("Vetores desordenados", nome_vetor)
    vetor = ler_vetor_do_arquivo(caminho)

    inicio = time.time()
    trocas, comparacoes = algoritmo_ordenacao(vetor)
    fim = time.time()

    tempo_execucao = fim - inicio  # tempo de execução

    print(tempo_execucao, "seg &", trocas,"trocas &", comparacoes, "comparações \n")

    caminho = os.path.join(nome_algoritmo, "Vetores ordenados", nome_vetor)
    salvar_vetor_em_arquivo(vetor, caminho)
    
    # Criação dos resultados no formato JSON
    resultados = {str(len(vetor)): tempo_execucao}

    # Salvando os resultados em um arquivo JSON
    caminho = os.path.join(nome_algoritmo, "resultados.json")

    if (nome_vetor == '1000.txt'):
        modo = 'w'
    else:
        modo = 'a'

    with open(caminho, modo) as arquivo:
        json.dump(resultados, arquivo)
        arquivo.write("\n")

def printa():
    print("abc")