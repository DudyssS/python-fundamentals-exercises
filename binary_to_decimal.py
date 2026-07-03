entrada = input('Digite um número binário separando cada bit por espaço: ')

numeroBinario = entrada.split()

for i in range(len(numeroBinario)):
    numeroBinario[i] = int(numeroBinario[i])

numeroBinario = list(reversed(numeroBinario));

numeroDecimal = 0
for i in range(len(numeroBinario)):
    if (numeroBinario[i] != 0):
        numeroDecimal += 2**i

print(numeroDecimal)