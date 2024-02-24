<h1>RENOMEAR PDF'S EM MASSA</h1>

> ATENÇÃO PARA AS BIBLIOTECAS DO PYTHON

```
pip install pdfplumber
```
```
pip install openpyxl
```
Utilize o main.py

O objetivo desse codigo é renomear grande massa de PDF's de notas fiscais e salva informaçoes do documento em uma planilha em excel.
EXEMPLO DO NOME: NF - 10.526 - CASTANHO II 18012024

O pdfplumber utilizamos para ler o PDF e puxas informaçoes de NOTA, DATA DE EMISSAO, LOCALIDADE para renomeação. 

E o proximo passo é armazenar os dados em uma planilha em excel.

O openpyxl é utilizado para editar A PLANILHA DE EXCEL, após rodar o leitura_p_excel.py o programa puxa as informaçoes:
NOTAS, DATA DE EMISSAO, VALOR, VALOR TOTAL, PRODUTO E QUANTIDADE.

Dependendo de que informações você vai precisa precisa editar o que você precisa na leitura_p_excel.py e leitura.py
