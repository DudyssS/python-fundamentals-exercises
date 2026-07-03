#AÇÃO 1

num = int(input("Digite um número: "))

if num > 0:
    if num %2 == 0:
        print("O número", num, "é positivo e par")
    else:
        print("O número", num, "é positivo e ímpar")
elif num < 0:
    if num %2 == 0:
        print("O número", num, "é negativo e par")
    else:
        print("O número", num, "é negativo e ímpar")
else:
    print("O número é zero")
    
    
#AÇÃO 2

entrada = input("Digite as três idades separadas por vírgula (ex: 23, 45, 31): ")

idade1, idade2, idade3 = map(int, entrada.split(','))

maior = idade1
if idade2 > maior:
    maior = idade2
if idade3 > maior:
    maior = idade3

print(f"A maior idade é: {maior}")


#AÇÃO 3

ano = int(input("Digite um ano:"))

if ano % 4 == 0:
    if ano % 100 != 0:
        print(ano, "é um ano bissexto.")
    else:
        print(ano, "não é um ano bissexto.")
elif ano % 400 == 0:
    if ano % 100 == 0:
        print(ano, "é um ano bissexto.")
    else:
        print(ano, "não é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")
    