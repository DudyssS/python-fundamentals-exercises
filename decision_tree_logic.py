#AÇÃO 1 E 2

num = int(input("Digite um número: "))

if num > 0:
    if num %2 == 0:
        if num %5 == 0:
            print("O número", num, "é positivo, par e múltiplo de 5")
        else:
            print("O número", num, "é positivo e par")
    else:
        if num %5 == 0:
            print("O número", num, "é positivo, ímpar e múltiplo de 5")
        else:
            print("O número", num, "é positivo e ímpar")
elif num == 0:
    print("O número é zero")

else:
    print("O número", num, "é negativo")
    
    
#AÇÃO 3
    
print("- Digite o número da sua resposta.\n")
p1 = input("Você possui algum tipo de problema de saúde?\n\n 1. Sim\n 2. Não\n\n")

if p1 == "1":
    r1 = input("Já fez uma consulta médica antes de começar qualquer atividade?\n\n 1. Sim\n 2. Não\n\n")
    if r1 == "1":
        p2 = input("Qual tipo de atividade física você prefere?\n\n 1. Aeróbica\n 2. Musculação\n 3. Outro\n\n")
        if p2 == "1":
            print("HIIT, corrida, pular corda, dança, circuito funcional - ideal pra queimar gordura e melhorar o fôlego.")
        elif p2 == "2":
            print("Treino dividido ou full body, foco em hipertrofia (8-12 reps), pesos livres e máquinas - ótimo pra ganhar massa e definir.")
        elif p2 == "3":
            print("Calistenia, artes marciais, esportes, yoga/pilates, jogos ativos – bom pra variar, manter a motivação e trabalhar corpo inteiro.")
    else:
        print("Realize uma consulta antes de realizar qualquer atividade física.")
else:
    p2 = input("Qual tipo de atividade física você prefere?\n\n 1. Aeróbica\n 2. Musculação\n 3. Outro\n\n")
    if p2 == "1":
        print("HIIT, corrida, pular corda, dança, circuito funcional - ideal pra queimar gordura e melhorar o fôlego.")
    elif p2 == "2":
        print("Treino dividido ou full body, foco em hipertrofia (8-12 reps), pesos livres e máquinas - ótimo pra ganhar massa e definir.")
    elif p2 == "3":
        print("Calistenia, artes marciais, esportes, yoga/pilates, jogos ativos – bom pra variar, manter a motivação e trabalhar corpo inteiro.")


#AÇÃO 4

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
    
    
#AÇÃO 5
    
    
data = input("Digite uma data: ")
dia, mes, ano = map(int, data.split('/'))

if mes < 1 or mes > 12:
    print(f"A data {dia}/{mes}/{ano} não é válida.")
else:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        bissexto = True
    else:
        bissexto = False
        
        
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if bissexto and mes == 2:
        dias_por_mes[1] = 29
        
        
if dia < 1 or dia > dias_por_mes[mes - 1]:
        print(f"A data {dia}/{mes}/{ano} não é válida.")
else:
        print(f"A data {dia}/{mes}/{ano} é válida.")