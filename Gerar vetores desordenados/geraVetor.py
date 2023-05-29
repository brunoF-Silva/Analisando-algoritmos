import random
import os
from pathlib import Path

def gerar_vetor_tamanho_mil():
    vetor = [random.randint(0, 100) for _ in range(1000)]
    return vetor

def gerar_vetor_tamanho_dez_mil():
    vetor = [random.randint(0, 100) for _ in range(10000)]
    return vetor

def gerar_vetor_tamanho_cem_mil():
    vetor = [random.randint(0, 100) for _ in range(100000)]
    return vetor
def gerar_vetor_tamanho_duzentos_mil():
    vetor = [random.randint(0, 100) for _ in range(200000)]
    return vetor
def gerar_vetor_tamanho_trezentos_mil():
    vetor = [random.randint(0, 100) for _ in range(300000)]
    return vetor
def gerar_vetor_tamanho_quatrocentos_mil():
    vetor = [random.randint(0, 100) for _ in range(400000)]
    return vetor
def gerar_vetor_tamanho_quinhentos_mil():
    vetor = [random.randint(0, 100) for _ in range(500000)]
    return vetor
def gerar_vetor_tamanho_seiscentos_mil():
    vetor = [random.randint(0, 100) for _ in range(600000)]
    return vetor
def gerar_vetor_tamanho_setecentos_mil():
    vetor = [random.randint(0, 100) for _ in range(700000)]
    return vetor
def gerar_vetor_tamanho_oitocentos_mil():
    vetor = [random.randint(0, 100) for _ in range(800000)]
    return vetor
def gerar_vetor_tamanho_novecentos_mil():
    vetor = [random.randint(0, 100) for _ in range(900000)]
    return vetor

def gerar_vetor_tamanho_milhao():
    vetor = [random.randint(0, 100) for _ in range(1000000)]
    return vetor


diretorio = "Vetores desordenados"
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

def salvar_vetor_em_arquivo(vetor, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for elemento in vetor:
            arquivo.write(str(elemento) + '\n')

''''''
vetor = gerar_vetor_tamanho_mil()
arquivo = os.path.join(diretorio, "1000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_dez_mil()
arquivo = os.path.join(diretorio, "10000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_cem_mil()
arquivo = os.path.join(diretorio, "100000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_duzentos_mil()
arquivo = os.path.join(diretorio, "200000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_trezentos_mil()
arquivo = os.path.join(diretorio, "300000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_quatrocentos_mil()
arquivo = os.path.join(diretorio, "400000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_quinhentos_mil()
arquivo = os.path.join(diretorio, "500000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_seiscentos_mil()
arquivo = os.path.join(diretorio, "600000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_setecentos_mil()
arquivo = os.path.join(diretorio, "700000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_oitocentos_mil()
arquivo = os.path.join(diretorio, "800000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_novecentos_mil()
arquivo = os.path.join(diretorio, "900000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)

vetor = gerar_vetor_tamanho_milhao()
arquivo = os.path.join(diretorio, "1000000.txt")
salvar_vetor_em_arquivo(vetor, arquivo)
