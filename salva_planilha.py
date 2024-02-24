import openpyxl

class excel_load():
    """carregando dados"""
    def __init__(self, dados):
        self.dados = dados
        self.abri_arquivo()

    def abri_arquivo(self):
        """carregando arquivos"""
        workbook = openpyxl.load_workbook('notas_test_am.xlsx')
        worksheet = workbook['Plan1']

        #encontra proxima celula vazia
        if worksheet['A3'].value is None:
            linha = 3
        else:
            linha = 4
            while worksheet['A'+str(linha)].value is not None:
                linha += 1

        #preencher os dados
        coluna = 0
        for dados in self.dados:
            for dado in dados:
                celula = chr(ord('A')+coluna) + str(linha)
                worksheet[celula] = dado
                coluna +=1
            linha +=1
            coluna = 0

        workbook.save('notas_test_am.xlsx')