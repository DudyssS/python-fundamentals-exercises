## conversor temperatura

conversao = int(input(""" Qual unidade de temperatura ser convertida?
                  
    1 - Celsius
    2 - Fahrenheit
    3 - Kelvin
                  
    """))

if conversao <1 or conversao >3:
    print("Não temos essa opção.")
else:
    graus = float(input(""" 
    Quantos graus?
    
    """))

if conversao == 1:
    print((graus * 9/5) + 32, '° Fahrenheit')
    print((graus + 273.15), '° Kelvin')
elif conversao == 2:
    print((graus - 32) * 5/9,'° Celsius')
    print((graus - 32) * 5/9 + 273.15,'° Kelvin')
elif conversao == 3:
    print((graus - 273.15), '° Celsius')
    print((graus - 273.15) * 9/5 + 32, '° Fahrenheit')
