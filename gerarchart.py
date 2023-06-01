import matplotlib.pyplot as plt
import json

class Metricas:
    def __init__(self, trocas, comparacoes, tempo_execucao, nome_algoritmo, nome_vetor):
        self.trocas = trocas
        self.comparacoes = comparacoes
        self.tempo_execucao = tempo_execucao
        self.nome_algoritmo = nome_algoritmo
        self.nome_vetor = nome_vetor

# Abra o arquivo JSON e leia seu conteúdo
with open('resultados.json') as json_file:
    dados_json = json.load(json_file)

# Verifique se os dados são uma lista
if isinstance(dados_json, list):
    # Os dados são uma lista de objetos
    lista_metricas = []
    for objeto in dados_json:
        # Acesse os atributos do objeto JSON
        trocas = objeto['trocas']
        comparacoes = objeto['comparacoes']
        tempo_execucao = objeto['tempo_execucao']
        nome_algoritmo = objeto['nome_algoritmo']
        nome_vetor = objeto['nome_vetor']
        # Crie um objeto da classe Metricas com os atributos obtidos
        metricas = Metricas(trocas, comparacoes, tempo_execucao, nome_algoritmo, nome_vetor)
        # Adicione o objeto à lista de métricas
        lista_metricas.append(metricas)
    
    # Faça o processamento necessário com a lista de objetos Metricas
    for metrica in lista_metricas:
        # Acesse os atributos do objeto como desejado
        trocas = metrica.trocas
        comparacoes = metrica.comparacoes
        tempo_execucao = metrica.tempo_execucao
        nome_algoritmo = metrica.nome_algoritmo
        nome_vetor = metrica.nome_vetor
        # Faça algo com os atributos

else:
    # Os dados não são uma lista de objetos
    print("Os dados não são uma lista de objetos no formato JSON.")

lista_metricas.sort(key=lambda x: x.nome_vetor == '1000000.txt')

def tempoexecucaochart():
    # Crie o gráfico de linhas
    x = [1000, 10000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    y = [metrica.tempo_execucao for metrica in lista_metricas]
    plt.plot(x, y)
    plt.xlim(0, 1000000)
    plt.ylim(0, y[len(y)-1])
    # Personalize o gráfico
    plt.xlabel('tamanho da entrada')
    plt.ylabel('tempo de execução (s)')
    plt.title('Tempo de execução X Tamanho da entrada')

    # salva o gráfico
    plt.savefig('tempoexecucao.png')
    
def quantidadeTrocas():
    # Crie o gráfico de linhas
    x = [1000, 10000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    y = [metrica.trocas for metrica in lista_metricas]
    plt.plot(x, y)
    plt.xlim(0, 1000000)
    plt.ylim(0, y[len(y)-1])
    # Personalize o gráfico
    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Trocas realizadas')
    plt.title('Quantidade de trocas realizadas X Tamanho da entrada')

    # salva o gráfico
    plt.savefig('trocas.png')
    

def quantidadeComparacoes():
    # Crie o gráfico de linhas
    x = [1000, 10000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
    y = [metrica.comparacoes for metrica in lista_metricas]
    print([metrica.nome_vetor for metrica in lista_metricas])
    plt.plot(x, y)
    plt.xlim(0, 1000000)
    plt.ylim(0, max(y))
    # Personalize o gráfico
    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Comparações realizadas')
    plt.title('Quantidade de comparações realizadas X Tamanho da entrada')

    # salva o gráfico
    plt.savefig('comparacoes.png')

def geraCharts():
    quantidadeComparacoes()
    plt.clf()
    tempoexecucaochart()
    plt.clf()
    quantidadeTrocas()
