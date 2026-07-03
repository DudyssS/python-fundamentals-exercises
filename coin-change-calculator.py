valor_cobrado = float(input('Insira o valor do produto desejado: '))
valor_pago = float(input('Insira o valor do pagamento: '))
troco = round((valor_pago - valor_cobrado) * 100) 

if troco < 0:
    print("Pagamento insuficiente!")
elif troco == 0:
    print("Não há troco necessário.")
else:
    moedas = [100, 50, 25, 10, 5, 1]
    moeda_tipo = ['1 real', '50 centavos', '25 centavos', '10 centavos', '5 centavos', '1 centavo']
    total_moedas = 0

    print(f"\nTroco: R${troco/100:.2f}\n")
    
    for i in range(len(moedas)):
        quantidade_moeda = troco // moedas[i]

        if quantidade_moeda > 0:
            print(f"{quantidade_moeda:.0f} moeda(s) de {moeda_tipo[i]}")
            total_moedas += quantidade_moeda
            troco = troco % moedas[i]

    print(f"\nTotal de moedas usadas: {total_moedas:.0f}")