import turtle
import random
import copy

def draw_line(x1,y1,x2,y2): # pra desenhando as linhas x e y
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)
    

def desenhar_grid(): # desenhando a grid mesmo
    turtle.pencolor('gray')
    turtle.pensize(3)
    x = -400
    for i in range(tamanho_da_grade+1):
        draw_line(x,-400,x,400)
        x += 800/tamanho_da_grade
    y = -400
    for i in range(tamanho_da_grade+1):
        draw_line(-400,y,400,y)
        y += 800/tamanho_da_grade


def iniciando_a_vida():
    for i in range(tamanho_da_grade):
        liferow = [] # a lista da vida
        for j in range(tamanho_da_grade):
            if random.randint(0,int(probabilidade_selecionada)) == 0: # 1/7 de chance de vida
                liferow.append(1) # 1 da a vida
            else:
                liferow.append(0) # 0 a vida morre
        life.append(liferow)


def desenhar_quadrado(x,y,size): # desenhando uma fileira de vida
    lifeturtle.up()
    lifeturtle.goto(x,y)
    lifeturtle.down()
    lifeturtle.seth(0)
    lifeturtle.begin_fill()
    for i in range(4):
        lifeturtle.fd(size)
        lifeturtle.left(90)
    lifeturtle.end_fill()


def desenhar_vida_inicial(x,y): # desenhando a vida em (x,y)
    lx = 800/tamanho_da_grade*x - 400 # convertendo x,y para coordenadas na tela
    ly = 800/tamanho_da_grade*y - 400
    desenhar_quadrado(lx+1,ly+1,800/tamanho_da_grade-2)


def desenhar_vida_total(): # desenhando a vida em geral
    global life
    for i in range(tamanho_da_grade):
        for j in range(tamanho_da_grade):
            if life[i][j] == 1: desenhar_vida_inicial(i,j) # Acende um quadrado


def quantidade_vizinhos(x, y):  # Verifica os vizinhos em volta da celula
    total = 0
    for i in range(max(x - 1, 0), min(x + 1, tamanho_da_grade - 1) + 1):
        for j in range(max(y - 1, 0), min(y + 1, tamanho_da_grade - 1) + 1):
            total += life[i][j]
    return total - life[x][y]


def update_life(): # atualizando o ciclo
    global life 
    newlife = copy.deepcopy(life)            # fazendo uma copia da vida
    for i in range(tamanho_da_grade):
        for j in range(tamanho_da_grade):
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


def parar(): # finalização da tarefa (SUJEITO A ALTERAÇÃO)
    turtle.bye()


life = list() # criando a lista

screen = turtle.Screen() # Cria a tela
turtle.setup(1000,1000) # Configura o tamanho da Janela
turtle.title("Conway's Game of Life by Nexus")  # Defini o titulo da Janela
turtle.hideturtle() # Esconde o cursos do Turtle
turtle.speed(0)     # Defini a Velocidade MAXIMA
turtle.tracer(0,0)  # Desativa a animação do turtle (Faz um desenho mais rapido)

tortuga = turtle.Turtle() # Criando uma tela para alertas 
tortuga.hideturtle()
lifeturtle = turtle.Turtle() # Desenhando vida
lifeturtle.up()             
lifeturtle.hideturtle()
lifeturtle.speed(0)
lifeturtle.color('black')


# ALERTBOXS E INPUTS


turtle.TK.messagebox.showinfo(title = "AVISO!", message = "É possível fechar a simulação utilizando a tecla [Q]")


while True:
    tamanho_da_grade = int(screen.textinput("Grid", "Tamanho da Grid (n X n)")) # nXn grid
    if not tamanho_da_grade.isdigit():

        turtle.TK.messagebox.showinfo(title= "AVISO!", message = "DIGITE APENAS NÚMEROS!")



while True:
    probabilidade_selecionada = int(screen.textinput("Probabilidade de Vida", "ESCOLHA 1 A 7 (1 sendo o maximo e 7 o minimo.)"))
    if probabilidade_selecionada not in range(0,8):
        turtle.TK.messagebox.showinfo(title= "AVISO!", message = "A escolha precisa ser entre 1 e 7!")
    else:
        iniciando_a_vida()
        update_life()
        break

   
turtle.onkeypress(parar, "q")
turtle.listen()

    
# EXECUTÁVEL
desenhar_grid()

turtle.done()