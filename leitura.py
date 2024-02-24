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

        with open(locais_file, 'r', encoding='utf-8') as lista:
            conteudo = lista.read()
            self.locais = ast.literal_eval(conteudo)

    def extracao_dados(self):
        """extracao dos dados"""
        nota = self.texto[2]
        nota = nota.split(' ')
        nota = nota[1]
        self.excel.append(nota)
        self.dados_pdf.append(nota)

        data = self.texto[7]
        data_pdf = data.replace('/', '')
        self.dados_pdf.append(data_pdf)

        separa = self.texto[14]
        separa = separa.replace('.', '')
        separa = separa.split(' ')
        local = ''
        for palavra in separa:
            if palavra in self.locais:
                local += palavra + ' '
        self.dados_pdf.append(local)

        produto = self.texto[12]
        produto = produto.split(' ')
        produto = produto[1]

        qnd = self.texto[12]
        qnd = qnd.split(' ')
        qnd = qnd[2]
        self.dados_pdf.append(qnd)

    def renomear_pdf(self):
        """renomeacao do doc.pdf"""
        nome = 'NF - ' + self.dados_pdf[0] + ' - ' + self.dados_pdf[2] + ' ' + self.dados_pdf[1]
        print(nome)
        return nome

