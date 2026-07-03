
print('Caso você precise calcular uma equação de 2º, essa é sua solução. Siga os passos a seguir para prosseguir com o cálculo:')
a = int(input('Coloque o valor de \"a\":'))
b = int(input('Coloque o valor de \"b\":'))
c = int(input('Coloque o valor de \"c\":'))

delta = b**2 - 4*a*c

x1= float((-b + delta**0.5) / (2*a))
x2= float((-b - delta**0.5) / (2*a))

print(f'Sua resposta aqui: {x1}, {x2}')