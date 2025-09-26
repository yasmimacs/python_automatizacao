

# Pacote: pyautogui -> Fazer automações no computador com o Python

import pyautogui as pyag
import time

pyag.PAUSE = 0.7 #Entre todos os comando irá ter uma pausa de 0.7 segundos. Esse passo é essencial para o computador ter tempo de carregar cada comando

### Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
## Abrir o Google Chrome
pyag.press("win") #Pressionar a tecla windows
pyag.write("chrome") #Escrever "chrome"
pyag.press("enter") #Pressionar a tecla enter

## Digitar site
pyag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #Especificar o site da web que deseja entrar
pyag.press("enter") #Pressionar a tecla enter
time.sleep(3) #Esperar 3 segundo para dar tempo do site carregar completamente


### Passo 2: Fazer login
## Para que o computador saiba onde exatamente clicar para ser possível digitar o email do login é preciso identificar a posição do mouse. As próximas linhas de código que estão como comentários seria o passo a passo de como se obter essa informação.
#import pyautogui as pyag
#import time
#time.sleep(5)
#print(pyag.position()) #Após rodar o código é preciso posicionar o mouse onde se quer clicar e esperar o tempo que se definiu na linha anterior.

## Preencher as informações para login
pyag.click(x=737, y=509) # Definir a posição específica do mouse na tela para clicar onde deseja.
pyag.write("email123@gmail.com") # Preencher email
pyag.press("tab") # Pressionar a tecla tab para mudar para a próxima informação a ser preenchida
pyag.write("senhapython123") #Preencher senha
pyag.press("tab") # Pressionar a tecla tab para mudar para o botão de login
pyag.press("enter") # Pressionar a tecla enter para efetivar o login
time.sleep(3) # Tempo de espera para o site terminar de carregar

### Passo 3: Importar a base de dados
import pandas as pd
tab = pd.read_csv("produtos.csv") # Criar uma variável com o DataFrame contendo os produtos


### Passo 4: Cadastrar os produtos em repetição

for linha in tab.index:
    pyag.click(x=683, y=366) # Novamente é preciso especificar a posição do mouse para selecionar a primeira caixa de texto.

    ## Adicionar as informações dos produtos
    codigo = tab.loc[linha, "codigo"]
    pyag.write(codigo)

    pyag.press("tab")
    marca = tab.loc[linha, "marca"]
    pyag.write(marca)

    pyag.press("tab")
    tipo = tab.loc[linha, "tipo"]
    pyag.write(tipo)

    pyag.press("tab")
    # É preciso transformar todas as informações numéricas do DataFrame para texto com a função str(), para que o computador consiga escrever a informação.
    categoria = str(tab.loc[linha, "categoria"])
    pyag.write(categoria)

    pyag.press("tab")
    preco_unitario = str(tab.loc[linha, "preco_unitario"])
    pyag.write(preco_unitario)

    pyag.press("tab")
    custo = str(tab.loc[linha, "custo"])
    pyag.write(custo)

    pyag.press("tab")
    obs = str(tab.loc[linha, "obs"])

    if obs != "nan":     # Especificar que na informação obs, o computador só escreva as informações diferentes de NaN
        pyag.write(obs)

    pyag.press("tab")
    pyag.press("enter")

    pyag.scroll(10000) # Dar um scroll para o início da página