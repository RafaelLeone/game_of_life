import numpy


# print('linhacoluna')
# 0 com 3 vizinhos -> 1
# 1 com 2 ou 3 vizinhos sobrevive
# O resto vira 0

# tempo 0:
# [0][0]: 0, [0][1]: 0, [0][2]: 0, [0][3]: 0
# [1][0]: 1, [1][1]: 1, [1][2]: 0, [1][3]: 0
# [2][0]: 0, [2][1]: 1, [2][2]: 0, [2][3]: 0
# [3][0]: 0, [3][1]: 0, [3][2]: 0, [3][3]: 0
# tempo 1:
# [0][0]: 0, [0][1]: 0, [0][2]: 0, [0][3]: 0
# [1][0]: 1, [1][1]: 1, [1][2]: 0, [1][3]: 0
# [2][0]: 1, [2][1]: 1, [2][2]: 0, [2][3]: 0
# [3][0]: 0, [3][1]: 0, [3][2]: 0, [3][3]: 0

TAMANHO_DA_MATRIZ = 4

matriz = numpy.zeros((TAMANHO_DA_MATRIZ, TAMANHO_DA_MATRIZ), dtype=numpy.int)

# Matriz inicial:
## Pode colocar os números que quiser entre 0 e TAMANHO_DA_MATRIZ-1
matriz[1][0] = 1
matriz[1][1] = 1
matriz[2][1] = 1
print('\n')
print("tempo 0: ")
print(matriz)

#Dá pra fazer um for i in range NUMERO_DE_VEZES_QUE_QUERO_RODAR aqui...
#Ou se o último tempo for igual ao penúltimo                     parar o programa
#Ou se tudo ficar 0                                              parar o programa
#Ou se o último  tempo repetir algum que já foi (guardar todes)  parar o programa
for numero_da_linha, linha in enumerate(matriz):
    for numero_da_coluna, celula in enumerate(linha):
        vizinhos = []
        numero_de_vizinhos_vivos = 0

        # Se ele for da ponta:
        if numero_da_linha == 0 and numero_da_coluna == 0:
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna+1]) #S direita
        elif numero_da_linha == 0 and numero_da_coluna == TAMANHO_DA_MATRIZ-1:
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-1]) #S esquerda
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
        elif numero_da_linha == TAMANHO_DA_MATRIZ-1 and numero_da_coluna == 0:
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna+1]) #N direita
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
        elif numero_da_linha == TAMANHO_DA_MATRIZ-1 and numero_da_coluna == TAMANHO_DA_MATRIZ-1:
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-1]) #N esquerda
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda

        # Se ele for da parede e nao da ponta.
        elif numero_da_linha == 0:
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-1]) #S esquerda
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna+1]) #S direita
        elif numero_da_coluna == 0:
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna+1]) #N direita
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna+1]) #S direita
        elif numero_da_linha == TAMANHO_DA_MATRIZ-1:
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-1]) #N esquerda
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna+1]) #N direita
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
        elif numero_da_coluna == TAMANHO_DA_MATRIZ-1:
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-1]) #N esquerda
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-1]) #S esquerda
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
        # Se não:
        else:
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-1]) #N esquerda
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna+1]) #N direita
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-1]) #S esquerda
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna+1]) #S direita

        # Vizinho vivos:
        for vizinho in vizinhos:
            if vizinho == 1:
                numero_de_vizinhos_vivos +=1
        
        # Transformação:
        if celula == 0 and numero_de_vizinhos_vivos == 3:
            matriz[numero_da_linha][numero_da_coluna] = 1 # recebe 1
        elif (celula == 1 and numero_de_vizinhos_vivos == 2) or (celula == 1 and numero_de_vizinhos_vivos == 3):
            matriz[numero_da_linha][numero_da_coluna] = 1 # recebe 1
        else:
            matriz[numero_da_linha][numero_da_coluna] = 0 # recebe 0

print('\n')
print("tempo 1: ") # Dá pra colocar o i aqui se fizer o for comentado da linha 33...
print(matriz)
print('\n')
# E botar um sleep aqui pra não aparecer tudo de uma vez.
