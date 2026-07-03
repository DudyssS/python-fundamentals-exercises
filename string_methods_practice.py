# =========================================
# AÇÃO 1 - Verificação de números em string
# =========================================

temp = "A temperatura média anual em Região Bahia é de: ⅛ graus Celsius"
for numero in temp.split(): # separei a variável 'temp' e criei uma variável que se enquadre
    if numero.isnumeric(): # o enquadramento é numéros, números romanos, frações, etc.).
        print(numero) # ele aparece no console caso haja número

temp = "A temperatura média anual em Região Bahia é de: 25 graus Celsius"
for numero in temp.split(): # separei a variável 'temp' e crei uma variável que se enquadre
    if numero.isdecimal(): # o enquadramento é numéros.
        print(numero) # ele aparece no console caso haja decimal



# =========================================
# AÇÃO 2 - Verificação de prefixo e sufixo
# =========================================

print("-60".startswith('-')) #Checar se a string inicia com tal caracteres.
print("60 C".endswith('C')) #Checar se a string termina com tal caracteres.




# =========================================
# AÇÃO 3 - Split de strings
# =========================================

cores = "azul amarelo vermelho rosa"
lista_de_cores = cores.split() #posso usar \n pra separar 
print(lista_de_cores)
# .slip() dividir as posições

temp = "A temperatura média anual em Região Bahia é de: 25 graus Celsius"
partes = temp.split(':') 
print(partes)
print(partes[-1])
# -2 = caracteres antes do slip
# -1 = caracteres depois do slip



# =========================================
# AÇÃO 4 - Operadores de busca em string
# =========================================

print("palavra" in "frase que contém ou não a palavra")
# in (False ou True)

clima = "hoje o clima está ensolarado, mas houveram várias chuvas esses dias."
print(clima.find("dias"))
# .find() encontra a posição da palavra (caso não tenha, ele retorna -1)

clima = "hoje o clima está ensolarado, mas houveram muitas muitas chuvas esses dias."
print(clima.count("dias"))
print(clima.count("muitas"))
# .count() retorna o número total de ocorrências de uma palavra



# =========================================
# AÇÃO 5 - Formatação de texto
# =========================================

título = str(input("Qual sua frase em minúscula: "))
título_de_cima = título.title()
print(título_de_cima)
# .title() deixa em maiúsculo a letra inicial de cada palavra

print(título_de_cima.lower())
# .lower() todas as letras minúsculas

print(título_de_cima.upper())
# .upper() todas as letras maiúsculas