#AÇÃO 1 & 3


def verifica_matriz_identidade(matriz):
    n = len(matriz)
    
    for i in range(n):
        for j in range(n):
            # Verifica elementos na diagonal principal
            if i == j:
                if matriz[i][j] != 1:
                    return False
            # Verifica outros elementos
            else:
                if matriz[i][j] != 0:
                    return False
    return True

def encontrar_maior(matriz):
    maior = matriz[0][0]
    for linha in matriz:
        for elemento in linha:
            if elemento > maior:
                maior = elemento
    return maior

def main():
    n = int(input("Digite o tamanho da matriz NxN: "))
    matriz = []

    print(f"Digite os elementos da matriz {n}x{n} (linha por linha, separados por espaço):")
    for _ in range(n):
        linha = input().strip().split()
        # Converte a string de entrada em uma lista de inteiros
        linha = [int(num) for num in linha]
        matriz.append(linha)

    # Verificação de matriz identidade
    if verifica_matriz_identidade(matriz):
        print("É uma matriz identidade")
    else:
        print("Não é uma matriz identidade")
    
    # Encontrar o maior elemento
    maior = encontrar_maior(matriz)
    print(f"O maior elemento da matriz é: {maior}")

if __name__ == "__main__":
    main()
    
    
#AÇÃO 2

def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma

# Exemplos de uso
matriz1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matriz2 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

print(soma_matriz(matriz1))  # Saída: 136
print(soma_matriz(matriz2))  # Saída: 4


#AÇÃO 4

def multiplicar_listas(lista1, lista2):
    #Multiplica elementos de duas listas 2 a 2
    return [[x * y for y in lista2] for x in lista1]

lista1 = list(map(int, input("Digite a primeira lista (números separados por espaço): ").split()))
lista2 = list(map(int, input("Digite a segunda lista (números separados por espaço): ").split()))
print("Resultado:", multiplicar_listas(lista1, lista2))


#AÇÃO 5

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Carrega a imagem
image_path = 'image.jpg'
img = Image.open(image_path)

# Converte para tons de cinza
img = img.convert('L')

# Converte para matriz numpy
matrix = np.array(img)
linhas, colunas = matrix.shape

# Inversão dos eixos 
matrix_invertida = np.flipud(np.fliplr(matrix))

# Imagem original e a invertida
plt.figure(figsize=(10, 5))

# Imagem original
plt.subplot(1, 2, 1)
plt.imshow(matrix, cmap='gray')
plt.title('Original')
plt.axis('off')

# Imagem com eixos invertidos
plt.subplot(1, 2, 2)
plt.imshow(matrix_invertida, cmap='gray')
plt.title('Eixos Invertidos')
plt.axis('off')

plt.tight_layout()
plt.show()