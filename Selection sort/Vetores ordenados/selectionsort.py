import time


def selection_sort(vetor):
    comparacoes = 0
    trocas = 0

    for i in range(len(vetor)):
        indice_menor = i
        for j in range(i + 1, len(vetor)):
            comparacoes += 1
            if vetor[j] < vetor[indice_menor]:
                indice_menor = j

        if indice_menor != i:
            vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]
            trocas += 1

    return trocas, comparacoes


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


vetor = ler_vetor_do_arquivo('mil.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio #tempo de execução

print("Mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

arquivo = os.path.join("Vetores desordenados", "1000.txt")
vetor = ler_vetor_do_arquivo(arquivo)

arquivo = os.path.join("Selection Sort/Vetores ordenados", "1000.txt")
salvar_vetor_em_arquivo(vetor, 'vetor_ordenado_selectionSort.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Dez mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

vetor = ler_vetor_do_arquivo('cem_mil.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Cem mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

'''
vetor = ler_vetor_do_arquivo('duzentos_mil.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Duzentos mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

vetor = ler_vetor_do_arquivo('trezentos_mil.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Trezentos mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

vetor = ler_vetor_do_arquivo('quatrocentos_mil.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Quatrocentos mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

vetor = ler_vetor_do_arquivo('quinhentos_mil.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Quinhentos mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

vetor = ler_vetor_do_arquivo('seiscentos_mil.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Seiscentos mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

vetor = ler_vetor_do_arquivo('setecentos_mil.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Setecentos mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

vetor = ler_vetor_do_arquivo('oitocentos_mil.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Oitocentos mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

vetor = ler_vetor_do_arquivo('novecentos_mil.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Novecentos mil")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")

vetor = ler_vetor_do_arquivo('milhao.txt')

inicio = time.time()
trocas, comparacoes = selection_sort(vetor)
fim = time.time()

tempo_execucao = fim - inicio  # tempo de execução
print("Um milhao")
print(tempo_execucao, "seg &", trocas, "trocas &", comparacoes, "comparações \n")'''
