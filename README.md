# RENOMEAR PDF'S EM MASSA

## ATENÇÃO - BIBLIOTECAS DO PYTHON

```
pip install pdfplumber
```
```
pip install openpyxl
```
### PARA RODAR O PROGRAMA

Nesse repositorio deixei 4 pasta com varios pdf's para servi como exemplo quando rodar o programa.

Na variavel `caminho_selecionado` você pode escolher qual pasta vai utilizar para o codigo.

É utilizado o `os.lisdir` para deixar em formator de lsita os nomes do `arquivo.pdf`.
```
arquivo_pdf = [arquivo for arquivo in os.listdir(caminho_selecionado) if arquivo.endswith('.pdf')]
```
> AS NOTAS FISCAIS NÃO SÃO VALIDAS

Com os documentos em .pdf salvos em `arquivo.pdf` usamos a variavel no laço `for`.

O 1° laço for vai puxa as informações dos pdf's para renomear no doc `leitura.py`.

Já o 2° laço puxa  as informações necessarias para salva no excel no doc `leitura_p_excel.py`.

![laço_for](https://github.com/HappyLuiz2/ranomear_pdf/assets/106756797/4ebd09bf-0f5f-4114-974d-f5963f0ba655)

No `leitura.py` o programa acaba de receber os dados enviados pelo laço `for` para fazer a extração de dados do .pdf.
Utilizando o `pdfplumber` podemos a extração do texto presente no `.pdf`.

![Screenshot 2024-02-24 181355](https://github.com/HappyLuiz2/ranomear_pdf/assets/106756797/52a4bc58-b245-460c-a790-19c3042aeccf)

Informamos a paginas que deseja no `page = page.extract_text()` e utilizamos o `.split(\n)` para separa o texto em uma lista.
Utilize o `teste_de_leitura.py` para vocês verificarem como funciona a extração que o pdfdlumber faz.
> ATENÇÃO utilizando após utilizar o `split(\n)` tera esse resultado.
![imagem_2024-02-24_184442517](https://github.com/HappyLuiz2/ranomear_pdf/assets/106756797/bce3fa85-9aae-4dbd-8ed4-23aaa1d7a691)
>
Mesmo que o resultado da lista as frases, números e simbolos estejam junto em um item podemos fazer um tratamento em cada uma utilizando o `.split()` e `.replace()` após separa o item em uma variavel como o exemplo abaixo:

>TRATAMENTO
>
> ![tratamento](https://github.com/HappyLuiz2/ranomear_pdf/assets/106756797/26d7f935-8b1f-4164-94b2-ca82928fc02a)
>

>RESULTADO
>
> ![imagem_2024-02-24_190234986](https://github.com/HappyLuiz2/ranomear_pdf/assets/106756797/c9985edc-ecb6-4422-a79d-8ebedd3e36b3)
>

Agora voltando ao `leitura.py` vocês vão perceber que existe outro `with open() as pdf:` ele não é um pdf só um `documento.txt` onde esta salvo nomes de cidades, o codigo esta renomeando pdf's e os documentos são notas fiscais de materiais que seram entregues nessas cidades, ele faz a leitura do arquivo.txt e salva como lista `self.locais`,  vai puxa o item da lista `self.texto` onde esta o nome da cidade e por no laço `for` e em seguida o `if` para verificar se a `palavra` esta na lista `self.locais`.

![Screenshot 2024-02-24 191226](https://github.com/HappyLuiz2/ranomear_pdf/assets/106756797/8fc16061-dcaf-40f5-978b-a419eba5d01e)

O final desse codigo ele retorna as informações que precisamos para renomear o pdf com o codigo final `os.raname(nome_antigo, nome_renomeado)`.

O 2° faz novamente a leitura dos PDF'S para salva informações necessarias no excel.

#### CONTINUA DEPOIS :(...

