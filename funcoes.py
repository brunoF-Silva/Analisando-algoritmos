import time
import json
import os
import matplotlib.pyplot as plt
import mmap
import json

class Metricas:
    def __init__(self, trocas, comparacoes, tempo_execucao, nome_algoritmo, nome_vetor):
        self.trocas = trocas
        self.comparacoes = comparacoes
        self.tempo_execucao = tempo_execucao
        self.nome_algoritmo = nome_algoritmo
        self.nome_vetor = nome_vetor


def ler_vetor_do_arquivo(nome_arquivo):
    print("Lendo vetor do arquivo", nome_arquivo)
    values = []
    with open(nome_arquivo, 'r') as file:
        # Obter o tamanho do arquivo
        file_size = os.fstat(file.fileno()).st_size
        # Mapear o arquivo na memória
        file_map = mmap.mmap(file.fileno(), length=file_size, access=mmap.ACCESS_READ)
        # Decodificar o conteúdo mapeado como uma string
        content = file_map[:].decode()
        # Converter as linhas lidas para inteiros
        values = [int(line.strip()) for line in content.split('\n') if line.strip()]
        # Fechar o mapeamento do arquivo
        file_map.close()
    return values


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


def plotar_grafico(resultados, legenda):
    tamanhos = []
    tempos = []

    for elemento in resultados:
        for tamanho, tempo in elemento.items():
            tamanhos.append(int(tamanho))
            tempos.append(tempo)

    plt.plot(tamanhos, tempos, 'b-')
    plt.title(legenda + ' em relação ao tamanho da entrada')
    plt.xlabel('Tamanho da entrada')
    plt.ylabel(legenda)
    plt.show()


def cria_json(resultados):
    # Criação dos resultados no formato JSON
    dados = []
    for result in resultados:
        dados.append(result.__dict__)

    with open("resultados.json", 'w') as arquivo:
        json.dump(dados, arquivo)
        arquivo.write("\n")

def analisa_algoritmo(nome_vetor, algoritmo_ordenacao, nome_algoritmo): #nome do arquivo do vetor escolhido, funçao do alogoritmo, nome em maiúsculo da pasta
    caminho = os.path.join("Vetores desordenados", nome_vetor)
    vetor = ler_vetor_do_arquivo(caminho)

    inicio = time.time()
    trocas, comparacoes = algoritmo_ordenacao(vetor)
    fim = time.time()

    tempo_execucao = fim - inicio  # tempo de execução

    print(tempo_execucao, "seg &", trocas,"trocas &", comparacoes, "comparações \n")
    return Metricas(trocas, comparacoes, tempo_execucao, nome_algoritmo, nome_vetor)



def analisa_quick_sort(nome_vetor, algoritmo_ordenacao, nome_algoritmo): #vetor escolhido, funçao do alogoritmo, nome em maiúsculo da pasta
    caminho = os.path.join("Vetores desordenados", nome_vetor)
    vetor = ler_vetor_do_arquivo(caminho)

    inicio = time.time()
    trocas, comparacoes = algoritmo_ordenacao(vetor, 0, len(vetor)-1)
    fim = time.time()

    tempo_execucao = fim - inicio  # tempo de execução

    print(tempo_execucao, "seg &", trocas,"trocas &", comparacoes, "comparações \n")
    return Metricas(trocas, comparacoes, tempo_execucao, nome_algoritmo, nome_vetor)
