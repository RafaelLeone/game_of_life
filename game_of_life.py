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

matriz = numpy.zeros((4,4), dtype=numpy.int)

matriz[1][0] = 1
matriz[1][1] = 1
matriz[2][1] = 1
print(matriz)

for numero_da_linha, linha in enumerate(matriz):
    for numero_da_coluna, celula in enumerate(linha):
        vizinhos = []
        vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-1])
        vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna-0])
        vizinhos.append(matriz[numero_da_linha-1][numero_da_coluna+1])
        vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna-1])
        vizinhos.append(matriz[numero_da_linha-0][numero_da_coluna+1])
        vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-1])
        vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna-0])
        vizinhos.append(matriz[numero_da_linha+1][numero_da_coluna+1])

        print("linha:", numero_da_linha, "coluna:", numero_da_coluna)
        print(vizinhos)
        
        if celula == 0 and len(vizinhos) == 3:
            ... # recebe 1
        elif (celula == 1 and len(vizinhos) == 2) or (celula == 1 and len(vizinhos) == 3):
            ... # recebe 1
        else:
            ... # recebe 0
