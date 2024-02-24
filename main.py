import os

from leitura import *
from leitura_p_excel import *
from salva_planilha import *

caminho_10 = r'10_doc'
caminho_20 = r'20_doc'
caminho_30 = r'30_doc'
caminho_40 = r'40_doc'

dados_coletados = []

arquivo_pdf = [arquivo for arquivo in os.listdir(caminho_10) if arquivo.endswith('.pdf')]

print("rename PDF's")
for i in range(len(arquivo_pdf)):
    nome_antigo = os.path.join(caminho_10, arquivo_pdf[i])
    coletado = extracao(os.path.join(caminho_10, arquivo_pdf[i]))
    nome_renomeado = os.path.join(caminho_10, f'{coletado.renomear_pdf()}.pdf')
    os.rename(nome_antigo, nome_renomeado)

print('data collection')
for i in range(len(arquivo_pdf)):
    leitura = extracao_leitura(os.path.join(caminho_10, arquivo_pdf[i]))
    dados_excel = leitura.coletando_dados()
    dados_coletados.append(dados_excel)

print('Saving data in Excel')
print('Wait for completion')
carregando = excel_load(dados_coletados)
print('concluded')
