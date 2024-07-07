import random
import copy

def iniciando_a_vida(tamanho, probabilidade_selecionada):
    life = []
    for i in range(tamanho):
        liferow = []
        for j in range(tamanho):
            if random.randint(0, int(probabilidade_selecionada)) == 0:
                liferow.append(1)
            else:
                liferow.append(0)
        life.append(liferow)
    return life

def quantidade_vizinhos(life, x, y, tamanho):
    total = 0
    for i in range(max(x - 1, 0), min(x + 1, tamanho - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, tamanho - 1) + 1):
            total += life[i][j]
    return total - life[x][y]

def update_life(life, tamanho):
    newlife = copy.deepcopy(life)
    for i in range(tamanho):
        for j in range(tamanho):
            k = quantidade_vizinhos(life, i, j, tamanho)
            if k < 2 or k > 3:
                newlife[i][j] = 0
            elif k == 3:
                newlife[i][j] = 1
    return newlife