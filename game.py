import random
import copy

def iniciando_a_vida(tamanho, probabilidade_selecionada):
    conjunto_de_celulas = []
    for i in range(tamanho):
        conjunto_de_celulas = []
        for j in range(tamanho):
            if random.randint(0, int(probabilidade_selecionada)) == 0:
                conjunto_de_celulas.append(1)
            else:
                conjunto_de_celulas.append(0)
        conjunto_de_celulas.append(conjunto_de_celulas)
    return conjunto_de_celulas

def quantidade_vizinhos(conjunto_de_celulas, x, y, tamanho):
    total = 0
    for i in range(max(x - 1, 0), min(x + 1, tamanho - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, tamanho - 1) + 1):
            total += conjunto_de_celulas[i][j]
    return total - conjunto_de_celulas[x][y]

def atualizar_população(conjunto_de_celulas, tamanho):
    proxima_população = copy.deepcopy(conjunto_de_celulas)
    for i in range(tamanho):
        for j in range(tamanho):
            k = quantidade_vizinhos(conjunto_de_celulas, i, j, tamanho)
            if k < 2 or k > 3:
                proxima_população[i][j] = 0
            elif k == 3:
                proxima_população[i][j] = 1
    return proxima_população