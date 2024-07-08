import turtle
import game

screen = turtle.Screen()
celula = turtle.Turtle()

def setup_screen():
    screen.setup(1000, 1000)
    screen.title("Conway's Game of life by Nexus")
    turtle.hideturtle()
    turtle.speed(0)
    turtle.tracer(0, 0)
    celula.up()
    celula.hideturtle()
    celula.speed(0)
    celula.color('black')

def desenhar_linhas(x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)
    turtle.pencolor('gray')
    turtle.pensize(3)

def desenhar_grid(tamanho):
    x = -400
    for _ in range(tamanho + 1):
        desenhar_linhas(x, -400, x, 400)
        x += 800 / tamanho
    y = -400
    for _ in range(tamanho + 1):
        desenhar_linhas(-400, y, 400, y)
        y += 800 / tamanho

def desenhar_quadrado(x, y, size):
    celula.up()
    celula.goto(x, y)
    celula.down()
    celula.seth(0)
    celula.begin_fill()
    for _ in range(4):
        celula.fd(size)
        celula.left(90)
    celula.end_fill()

def desenhar_vida_inicial(x, y, tamanho):
    lx = 800 / tamanho * x - 400
    ly = 800 / tamanho * y - 400
    desenhar_quadrado(lx + 1, ly + 1, 800 / tamanho - 2)

def desenhar_vida_total(conjunto_de_celulas, tamanho):
    for i in range(tamanho):
        for j in range(tamanho):
            if conjunto_de_celulas[i][j] == 1:
                desenhar_vida_inicial(i, j, tamanho)

def atualizar_população(conjunto_de_celulas, tamanho):
    proxima_população = game.atualizar_população(conjunto_de_celulas, tamanho)
    celula.clear()
    desenhar_vida_total(proxima_população, tamanho)
    screen.update()
    screen.ontimer(lambda: atualizar_população(proxima_população, tamanho), 350)
    print(proxima_população)

def parar():
    turtle.bye()