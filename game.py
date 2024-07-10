import random
import copy

velocidade_atual = 0

def iniciando_a_vida(tamanho, probabilidade_selecionada):
    """Cria uma nova população de acordo com a probabilidade de vida \n (int, int) -> list()"""
    população_geral = []              # inicia uma lista vazia pra ser colocadas as células
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
    """Verifica a quantidade de celulas vizinhas vivas \n (list, float, float, int) -> int"""
    total = 0
    for i in range(max(x - 1, 0), min(x + 1, tamanho - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, tamanho - 1) + 1):
            total += população_geral[i][j]
    return total - população_geral[x][y]


def atualizar_população(população_geral, tamanho):
    """Verifica as regras dos vizinhos e defini o proximo estado das células. \n (list(), int) -> list()"""
    proxima_população = copy.deepcopy(população_geral)      # copia a população atual para modifica-la
    for i in range(tamanho):    # passa por todas as células da matriz
        for j in range(tamanho):
            k = quantidade_vizinhos(população_geral, i, j, tamanho)
            if k < 2 or k > 3:              # Se a célula tiver mais de 3 vizinhos ou menos de 2, ela morre.
                proxima_população[i][j] = 0
            elif k == 3:                    # Se a célula estiver morta e tiver o total de 3 vizinhos, ela revive.
                proxima_população[i][j] = 1
    return proxima_população


def celulas_vivas(população):
    """Verifica a quantidade de números '1' numa determinada matriz \n (list()) -> int"""
    qtd = 0 
    for linha in população:
        for celula in linha:
            if celula == 1:
                qtd += 1
    return qtd


# CASOS DE TESTES
if __name__ == "__main__":
    celulasteste = iniciando_a_vida(3,1) # Vai gerar uma matriz de zeros e uns com grande chance da maioria vir 1
    print(celulasteste)  # print da matriz gerada para o teste
    print(celulas_vivas([[0,0,0,0,1],[1,1,1,0,0]]) ) # retorna 4
    print(quantidade_vizinhos(celulasteste, 1, 1, 3))
    print(atualizar_população(celulasteste, 3))  # Verifica a população e mata ou revive uma celula de acordo com as regras definidas (mais de 3 vizinhos ou - de 2 = morte, 3 vizinhos em volta a celula vive)




# def velocidades(vel):
#     velocidades = [190, 350, 490]
#     proxima_velocidade = velocidades[velocidade_atual]
#     return proxima_velocidade

# def alterar_velocidade():
#     global velocidade_atual
#     if velocidade_atual == 2:
#         velocidade_atual = 0                      por conta de conflitos e pouco tempo não conseguimos 
#     else:                                         implementar o switch de velocidade
#         velocidade_atual += 1
#     vel = velocidades(velocidade_atual)
#     return vel

# print(alterar_velocidade)
# print(alterar_velocidade)