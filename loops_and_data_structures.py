#AÇÃO 1

n = int(input("\nDigite um número: "))
impares = []
for i in range(1, n+1, 2):
    impares.append(str(i))
print(", ".join(impares))

#AÇÃO 2

n = int(input("\nDigite um número: "))
numeros_especiais = []
for num in range(2, n+1, 2): 
    if num % 3 != 0 or num % 5 == 0:
        numeros_especiais.append(str(num))
if numeros_especiais:
    print(", ".join(numeros_especiais))
else:
    print("\nNenhum número atende aos critérios")
    
    
#AÇÃO 3

texto = input("\nDigite um texto: ").lower()
vogais = 'aeiouáéíóúâêîôûãõ'
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print(f"\nO texto contém {contador} vogais")


#AÇÃO 4

entrada = input("\nDigite números inteiros separados por vírgula: ")
numeros = [int(num.strip()) for num in entrada.split(',')]

produto = 1
for num in numeros:
    produto *= num

print(f"\nO produto dos números é: {produto}")


#AÇÃO 5

precos = {
    "arroz": 5.00,
    "feijão": 4.00,
    "leite": 3.50,
    "pão": 1.50,
    "carne": 25.99,
    "frango": 12.50,
    "ovos": 8.90,
    "queijo": 15.75,
    "tomate": 3.20,
    "cebola": 2.85
}

def calcular_total(lista_compras):
    total = 0.0
    for produto in lista_compras:
        if produto in precos:
            total += precos[produto]
        else:
            print(f"Aviso: Produto '{produto}' não encontrado na lista de preços")
    return total

# Entrada do usuário
entrada = input("\nDigite os produtos da sua lista de compras, separados por vírgula: ")
itens_compra = [item.strip().lower() for item in entrada.split(',')]

# Cálculo e exibição do total
valor_total = calcular_total(itens_compra)
print(f"\nTotal da compra: R$ {valor_total:.2f}")