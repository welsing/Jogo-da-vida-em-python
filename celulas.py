from tela import desenhar_quadrado, selecionar_probabilidade, selecionar_tamanho_grade, tamanho, probabilidade, screen, lifeturtle, turtle
import copy
import random


def iniciando_a_vida():
    for i in range(tamanho):
        liferow = [] # a lista da vida
        for j in range(tamanho):
            if random.randint(0,probabilidade) == 0: # 1/7 de chance de vida
                liferow.append(1) # 1 da a vida
            else:
                liferow.append(0) # 0 a vida morre
        life.append(liferow)


def desenhar_vida_inicial(x,y): # desenhando a vida em (x,y)
    lx = 800/tamanho*x - 400 # convertendo x,y para coordenadas na tela
    ly = 800/tamanho*y - 400
    desenhar_quadrado(lx+1,ly+1,800/tamanho-2)


def desenhar_vida_total(): # desenhando a vida em geral
    global life
    for i in range(tamanho):
        for j in range(tamanho):
            if life[i][j] == 1: desenhar_vida_inicial(i,j) # Acende um quadrado


def quantidade_vizinhos(x, y):  # Verifica os vizinhos em volta da celula
    total = 0
    for i in range(max(x - 1, 0), min(x + 1, tamanho - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, tamanho - 1) + 1):
            total += life[i][j]
    return total - life[x][y]


def update_life(): # atualizando o ciclo
    global life 
    newlife = copy.deepcopy(life)            # fazendo uma copia da vida
    for i in range(tamanho):
        for j in range(tamanho):
            k = quantidade_vizinhos(i,j)
            if k < 2 or k > 3:
                newlife[i][j] = 0
            elif k == 3:
                newlife[i][j] = 1
    life = copy.deepcopy(newlife)           # copiar de volta a vida
    lifeturtle.clear()                      # limpa a vida anterior
    desenhar_vida_total()
    screen.update() 
    screen.ontimer(update_life,350)         # atualizando a cada 0.35 segundos
    print(life)




life = list() # criando a lista



