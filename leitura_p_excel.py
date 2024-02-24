import pdfplumber
import ast

locais_file = 'nomes_localidade.txt'

class extracao_leitura():
    """leitura para salva dados"""

    def __init__(self, caminho):
        self.caminho = caminho
        self.texto = ''
        self.excel = []
        self.leitura_arq()

    def leitura_arq(self):
        """coletando dados"""
        with pdfplumber.open(self.caminho) as pdf:
            page = pdf.pages[0]
            texto_letra = page.extract_text()
            texto_linha = texto_letra.split('\n')
            self.texto = texto_linha

        with open(locais_file, 'r', encoding='utf-8') as lista:
            conteudo = lista.read()
            self.locais = ast.literal_eval(conteudo)

    def coletando_dados(self):
        """separando dados"""
        nota = self.texto[2]
        nota = nota.split(' ')
        nota = nota[1]
        self.excel.append(nota)

        data = self.texto[7]
        data_exel = data
        self.excel.append(data_exel)

        separa = self.texto[14]
        separa = separa.replace('.', '')
        separa = separa.split(' ')
        local = ''
        for palavra in separa:
            if palavra in self.locais:
                local += palavra + ' '
        self.excel.append(local)

        produto = self.texto[12]
        produto = produto.split(' ')
        produto = produto[1]
        self.excel.append(produto)

        qnd = self.texto[12]
        qnd = qnd.split(' ')
        qnd = qnd[2]
        self.excel.append(qnd)

        preco = self.texto[12]
        preco = preco.split(' ')
        preco = preco[3]
        preco = preco[2:]
        self.excel.append(preco)

        total = self.texto[12]
        total = total.split(' ')
        total = total[4]
        total = total[2:]
        self.excel.append(total)

        return self.excel
