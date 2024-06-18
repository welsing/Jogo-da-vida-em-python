import turtle
import random
import copy

screen=turtle.Screen()
turtle.setup(1000,1000)
turtle.title("Jogo da Vida do Nickar")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0,0)

lifeturtle = turtle.Turtle() # Desenhando vida
lifeturtle.up()
lifeturtle.hideturtle()
lifeturtle.speed(0)
lifeturtle.color('black')

n = 50 # nXn grid
def draw_line(x1,y1,x2,y2): # pra desenhando as linhas x e y
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)
    
def draw_grid(): # desenhando a grid mesmo
    turtle.pencolor('gray')
    turtle.pensize(3)
    x = -400
    for i in range(n+1):
        draw_line(x,-400,x,400)
        x += 800/n
    y = -400
    for i in range(n+1):
        draw_line(-400,y,400,y)
        y += 800/n

life = list() # criando a lista
def init_lives():
    for i in range(n):
        liferow = [] # a lista da vida
        for j in range(n):
            if random.randint(0,7) == 0: # 1/7 de chance de vida
                liferow.append(1) # 1 da a vida
            else:
                liferow.append(0) # 0 a vida morre
        life.append(liferow) 

def draw_square(x,y,size): # desenhando uma fileira de vida
    lifeturtle.up()
    lifeturtle.goto(x,y)
    lifeturtle.down()
    lifeturtle.seth(0)
    lifeturtle.begin_fill()
    for i in range(4):
        lifeturtle.fd(size)
        lifeturtle.left(90)
    lifeturtle.end_fill()

def draw_life(x,y): # desenhando a vida em (x,y)
    lx = 800/n*x - 400 # convertendo x,y para coordenadas na tela
    ly = 800/n*y - 400
    draw_square(lx+1,ly+1,800/n-2)

def draw_all_life(): # desenhando a vida em geral
    global life
    for i in range(n):
        for j in range(n):
            if life[i][j] == 1: draw_life(i,j) # draw live cells

def num_neighbors(x,y): # ensinando como funciona os vizinhos para o pc [x,y]
    sum = 0
    for i in range(max(x-1,0),min(x+1,n-1)+1):
        for j in range(max(y-1,0),min(y+1,n-1)+1):
            sum += life[i][j]
    return sum - life[x][y]
        
def update_life(): # atualizando o ciclo
    global life 
    newlife = copy.deepcopy(life) # fazendo uma copia da vida
    for i in range(n):
        for j in range(n):
            k = num_neighbors(i,j)
            if k < 2 or k > 3:
                newlife[i][j] = 0
            elif k == 3:
                newlife[i][j] = 1
    life = copy.deepcopy(newlife) # copiar de volta a vida
    lifeturtle.clear() # limpa a vida anterior
    draw_all_life()
    screen.update() 
    screen.ontimer(update_life,200) # atualizando a cada 0.2 segundos

draw_grid()
init_lives()
update_life()
