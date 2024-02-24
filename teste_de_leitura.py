import pdfplumber
import ast

file_test = r'pdf_test.pdf'
locais_file = 'nomes_localidade.txt'

class extracao():
    """Inicio do programa"""
    def __init__(self, arquivo):
        """armazenamento do dados iniciais"""
        self.arquivo = arquivo
        self.leitura_arquivos()

    def leitura_arquivos(self):
        """leitura de pdf e bloco"""
        with pdfplumber.open(self.arquivo) as pdf:
            page = pdf.pages[0]
            texto = page.extract_text()
            texto = texto.split('\n')
            print(texto)
            data = texto[7]
            print('\nData:', data)
            nota = texto[2]
            nota = nota[2:]
            nota = nota.replace(' ', '') + '°'
            print('\nNF -',nota)


test = extracao(file_test)
