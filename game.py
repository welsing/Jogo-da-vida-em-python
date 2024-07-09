import random
import copy

velocidade_atual = 0

def iniciando_a_vida(tamanho, probabilidade_selecionada):
    """Cria uma nova população de acordo com a probabilidade de vida \n (int, int) -> list()"""
    população_geral = []
    for i in range(tamanho):
        conjunto_de_celulas = []
        for j in range(tamanho):
            if random.randint(0, int(probabilidade_selecionada)) == 0:
                conjunto_de_celulas.append(1)
            else:
                conjunto_de_celulas.append(0)
        população_geral.append(conjunto_de_celulas)
    return população_geral

def quantidade_vizinhos(população_geral, x, y, tamanho):
    """Defini o comportamento das celulas \n (list, float, float, int) -> int"""
    total = 0
    for i in range(max(x - 1, 0), min(x + 1, tamanho - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, tamanho - 1) + 1):
            total += população_geral[i][j]
    return total - população_geral[x][y]

def atualizar_população(população_geral, tamanho):
    """Verifica as regras dos vizinhos e defini o proximo estado das células. \n (list(), int) -> list()"""
    proxima_população = copy.deepcopy(população_geral)
    for i in range(tamanho):
        for j in range(tamanho):
            k = quantidade_vizinhos(população_geral, i, j, tamanho)
            if k < 2 or k > 3:
                proxima_população[i][j] = 0
            elif k == 3:
                proxima_população[i][j] = 1
    return proxima_população

# def velocidades(vel):
    
#     velocidades = [190, 350, 490]
#     proxima_velocidade = velocidades[velocidade_atual]
#     return proxima_velocidade

# def alterar_velocidade():
#     global velocidade_atual
#     if velocidade_atual == 2:
#         velocidade_atual = 0
#     else:
#         velocidade_atual += 1
#     vel = velocidades(velocidade_atual)
#     return vel