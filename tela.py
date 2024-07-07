import turtle
import game

tela = turtle.Screen()
celulas = turtle.Turtle()

def setup_screen():
    tela.setup(1000, 1000)
    tela.title("Conway's Game of Life by Nexus")
    turtle.hideturtle()
    turtle.speed(0)
    turtle.tracer(0, 0)
    celulas.up()
    celulas.hideturtle()
    celulas.speed(0)
    celulas.color('black')


def deenhar_linha(x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)
    turtle.pencolor('gray')
    turtle.pensize(3)


def desenhar_grid(tamanho):
    x = -400
    for _ in range(tamanho + 1):
        deenhar_linha(x, -400, x, 400)
        x += 800 / tamanho
    y = -400
    for _ in range(tamanho + 1):
        deenhar_linha(-400, y, 400, y)
        y += 800 / tamanho

def desenhar_quadrado(x, y, size):
    celulas.up()
    celulas.goto(x, y)
    celulas.down()
    celulas.seth(0)
    celulas.begin_fill()
    for _ in range(4):
        celulas.fd(size)
        celulas.left(90)
    celulas.end_fill()

def desenhar_vida_inicial(x, y, tamanho):
    lx = 800 / tamanho * x - 400
    ly = 800 / tamanho * y - 400
    desenhar_quadrado(lx + 1, ly + 1, 800 / tamanho - 2)

def desenhar_grid(conjunto_de_celulas, tamanho):
    for i in range(tamanho):
        for j in range(tamanho):
            if conjunto_de_celulas[i][j] == 1:
                desenhar_vida_inicial(i, j, tamanho)

def atualizar_população(conjunto_de_celulas, tamanho):
    proxima_população = game.atualizar_população(conjunto_de_celulas, tamanho)
    celulas.clear()
    desenhar_grid(proxima_população, tamanho)
    tela.update()
    tela.ontimer(lambda: atualizar_população(proxima_população, tamanho), 350)
    print(proxima_população)

def parar():
    turtle.bye()