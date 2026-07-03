calculo = input("""
      Selecione a operação:

     1 - Adição
     2 - Subtração 
     3 - Multiplicação
     4 - Divisão
      """)

num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))

if calculo == "1":
    resultado = num1 + num2
elif calculo == "2":
    resultado = num1 - num2
elif calculo == "3":
    resultado = num1 * num2
elif calculo == "4":
    resultado = num1 / num2

print("o resultado é: ", resultado)
