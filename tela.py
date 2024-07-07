import turtle
import game

screen = turtle.Screen()
lifeturtle = turtle.Turtle()

def setup_screen():
    screen.setup(1000, 1000)
    screen.title("Conway's Game of Life by Nexus")
    turtle.hideturtle()
    turtle.speed(0)
    turtle.tracer(0, 0)
    lifeturtle.up()
    lifeturtle.hideturtle()
    lifeturtle.speed(0)
    lifeturtle.color('black')

def draw_line(x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)
    turtle.pencolor('gray')
    turtle.pensize(3)

def draw_grid(tamanho):
    x = -400
    for _ in range(tamanho + 1):
        draw_line(x, -400, x, 400)
        x += 800 / tamanho
    y = -400
    for _ in range(tamanho + 1):
        draw_line(-400, y, 400, y)
        y += 800 / tamanho

def desenhar_quadrado(x, y, size):
    lifeturtle.up()
    lifeturtle.goto(x, y)
    lifeturtle.down()
    lifeturtle.seth(0)
    lifeturtle.begin_fill()
    for _ in range(4):
        lifeturtle.fd(size)
        lifeturtle.left(90)
    lifeturtle.end_fill()

def desenhar_vida_inicial(x, y, tamanho):
    lx = 800 / tamanho * x - 400
    ly = 800 / tamanho * y - 400
    desenhar_quadrado(lx + 1, ly + 1, 800 / tamanho - 2)

def desenhar_vida_total(life, tamanho):
    for i in range(tamanho):
        for j in range(tamanho):
            if life[i][j] == 1:
                desenhar_vida_inicial(i, j, tamanho)

def update_life(life, tamanho):
    newlife = game.update_life(life, tamanho)
    lifeturtle.clear()
    desenhar_vida_total(newlife, tamanho)
    screen.update()
    screen.ontimer(lambda: update_life(newlife, tamanho), 350)
    print(newlife)

def parar():
    turtle.bye()