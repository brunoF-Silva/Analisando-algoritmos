import time


def partition(vetor, low, high):
    i = low - 1
    pivot = vetor[high]
    comparações = 0
    trocas = 0

    for j in range(low, high):
        comparações += 1
        if vetor[j] <= pivot:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
            trocas += 1

    vetor[i + 1], vetor[high] = vetor[high], vetor[i + 1]
    trocas += 1

    return i + 1, trocas, comparações


def quick_sort(vetor, low, high):
    trocas = 0
    comparações = 0

    if low < high:
        pivot_index, trocas_part, comparações_part = partition(
            vetor, low, high)
        trocas += trocas_part
        comparações += comparações_part

        trocas_left, comparações_left = quick_sort(vetor, low, pivot_index - 1)
        trocas_right, comparações_right = quick_sort(
            vetor, pivot_index + 1, high)

        trocas += trocas_left + trocas_right
        comparações += comparações_left + comparações_right

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


vetor = ler_vetor_do_arquivo('arquivo.txt')

inicio = time.time()
trocas, comparações = quick_sort(vetor, 0, len(vetor) - 1)
fim = time.time()

tempo_execucao = fim - inicio

print("Tempo de execução: {:.6f} segundos".format(tempo_execucao))
print("Quantidade de trocas: {}".format(trocas))
print("Quantidade de comparações: {}".format(comparações))

salvar_vetor_em_arquivo(vetor, 'vetor_ordenado_quickSort.txt')
