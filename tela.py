import turtle
import game

screen = turtle.Screen()
celula = turtle.Turtle()

def setup_screen():
    """Configura a tela do turtle \n () -> None"""
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
    """Desenha as linhas da grade utilizando coodenadas \n (float, float, float, float) -> None"""
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)
    turtle.pencolor('gray')
    turtle.pensize(3)


def desenhar_grid(tamanho):
    """Realiza o desenho completo da grade utlizando as linhas de acordo com o tamanho definido\n (int) -> None"""
    x = -400
    for _ in range(tamanho + 1):
        desenhar_linhas(x, -400, x, 400)
        x += 800 / tamanho
    y = -400
    for _ in range(tamanho + 1):
        desenhar_linhas(-400, y, 400, y)        
        y += 800 / tamanho


def desenhar_quadrado(x, y, size):
    """Defini o perimetro de cada celula na grade \n (float, float, int) -> None """
    celula.up()
    celula.goto(x, y)
    celula.down()
    celula.seth(0)
    celula.begin_fill()
    for _ in range(4):
        celula.fd(size)
        celula.left(90)
    celula.end_fill()


def acender_celula(x, y, tamanho):
    """Acende o quadrado da célula nas coordenadas desejadas \n (int, int) -> None"""
    lx = 800 / tamanho * x - 400
    ly = 800 / tamanho * y - 400
    desenhar_quadrado(lx + 1, ly + 1, 800 / tamanho - 2)


def acender_população_viva(população_geral, tamanho):
    """Responsavel por acender todas as células vivas da população \n (list(), int) -> None"""
    for i in range(tamanho):
        for j in range(tamanho):
            if população_geral[i][j] == 1:
                acender_celula(i, j, tamanho)


def mostrar_informação(x, y, text):
    """Essa função tem a finalidade escrever algo na tela do turtle em determinada coordenada \n (float, float, text) -> None"""
    pen = turtle.Turtle()
    pen.clear()
    pen.hideturtle()
    pen.penup()
    
    pen.goto(x,y)
    pen.write(text, align="center", font=("Arial", 12, "normal"))


def celulas_vivas(população):
    qtd = 0 
    for linha in população:
        for celula in linha:
            if celula == 1:
                qtd += 1
    return qtd


def hud(celulas):
    """Mostra as informações necessarias da simulação como a quantidade de células vivas \n (int) -> None"""
    mostrar_informação(-300, 400, F"VIVAS: {celulas}")


def atualizar_população(população_geral, tamanho):
    """Atualiza a grade com o proximo turno da população. \n (list, int) -> None"""
    proxima_população = game.atualizar_população(população_geral, tamanho)
    celula.clear()
    acender_população_viva(proxima_população, tamanho)
    screen.update()
    screen.ontimer(lambda: atualizar_população(proxima_população, tamanho), 290)
    hud(celulas_vivas(população_geral))


def parar():
    """Fecha a janela e encerra a simulação. \n () -> None"""
    turtle.bye()