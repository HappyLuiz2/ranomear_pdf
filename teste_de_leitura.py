import pdfplumber
import ast

locais_file = 'nomes_localidade.txt'

class extracao():
    """Inicio do programa"""
    def __init__(self, arquivo):
        """armazenamento do dados iniciais"""
        self.arquivo = arquivo
        self.texto = ''
        self.locais = ''
        self.dados_pdf = []
        self.excel = []
        self.leitura_arquivos()
        self.extracao_dados()

    def leitura_arquivos(self):
        """leitura de pdf e bloco"""
        with pdfplumber.open(self.arquivo) as pdf:
            page = pdf.pages[0]
            texto = page.extract_text()
            self.texto = texto.split('\n')
            print(self.texto)
