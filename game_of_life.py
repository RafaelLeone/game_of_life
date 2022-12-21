# print('linhacoluna')
# 0 com 3 vizinhos -> 1
# 1 com 2 ou 3 vizinhos sobrevive

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

import numpy

TAMANHO_DA_MATRIZ = 4

matriz = numpy.zeros((TAMANHO_DA_MATRIZ, TAMANHO_DA_MATRIZ), dtype=numpy.int)

matriz[1][0] = 1
matriz[1][1] = 1
matriz[2][1] = 1
print(matriz)

for numero_da_linha, linha in enumerate(matriz):
    for numero_da_coluna, celula in enumerate(linha):
        vizinhos = []

        #Se ele for da ponta:
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

        #Se ele for da parede e nao da ponta.
        elif(
            numero_da_linha == 0 or
            numero_da_coluna == 0 or
            numero_da_linha == TAMANHO_DA_MATRIZ-1 or
            numero_da_coluna == TAMANHO_DA_MATRIZ-1
        ): 
            ...
        else:
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-1]) #N esquerda
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0]) #N
            vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna+1]) #N direita
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1]) #Esquerda
            vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1]) #Direita
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-1]) #S esquerda
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0]) #S
            vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna+1]) #S direita

        print("linha:", numero_da_linha, "coluna:", numero_da_coluna)
        print(vizinhos)
        
        if celula == 0 and len(vizinhos) == 3:
            ... # recebe 1
        elif (celula == 1 and len(vizinhos) == 2) or (celula == 1 and len(vizinhos) == 3):
            ... # recebe 1
        else:
            ... # recebe 0
