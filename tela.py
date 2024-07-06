import turtle

def desenhar_linha(x1,y1,x2,y2): # pra desenhando as linhas x e y
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)
    

def desenhar_grid(): # desenhando a grid mesmo
    turtle.pencolor('gray')
    turtle.pensize(3)
    x = -400
    for i in range(tamanho+1):
        desenhar_linha(x,-400,x,400)
        x += 800/tamanho
    y = -400
    for i in range(tamanho+1):
        desenhar_linha(-400,y,400,y)
        y += 800/tamanho

def iniciar_tela():
    # alertbox()
    desenhar_linha()
    desenhar_grid()


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


def selecionar_tamanho_grade():
    while True:
        tamanho = screen.textinput("Grid", "Tamanho da Grid (n X n)") # nXn grid
        print(tamanho)
        if not tamanho.isdigit():
            turtle.TK.messagebox.showinfo(title= "AVISO!", message = "DIGITE APENAS NÚMEROS!")
        else:
            tamanho = int(tamanho)
            break
        
    return tamanho

def selecionar_probabilidade():
    while True:
        probabilidade_selecionada = screen.textinput("Probabilidade de Vida", "ESCOLHA 1 A 7 (1 sendo o maximo e 7 o minimo.)")
        print(probabilidade_selecionada)
        if probabilidade_selecionada not in "1234567":
            turtle.TK.messagebox.showinfo(title= "AVISO!", message = "A escolha precisa ser entre 1 e 7!")
        else:
            probabilidade_selecionada = int(probabilidade_selecionada)
            break
    return probabilidade_selecionada

# def alertbox():
#     tamanho = selecionar_tamanho_grade
#     probabilidade = selecionar_probabilidade
#     return tamanho, probabilidade


def parar(): # finalização da tarefa (SUJEITO A ALTERAÇÃO)
    turtle.bye()


tamanho = selecionar_tamanho_grade
probabilidade = selecionar_probabilidade

tortuga = turtle.Turtle() # Criando uma tela para alertas 
tortuga.hideturtle()
lifeturtle = turtle.Turtle() # Desenhando vida
lifeturtle.up()             
lifeturtle.hideturtle()
lifeturtle.speed(0)
lifeturtle.color('black')

screen = turtle.Screen() # Cria a tela
turtle.setup(1000,1000) # Configura o tamanho da Janela
turtle.title("Conway's Game of Life by Nexus")  # Defini o titulo da Janela
turtle.hideturtle() # Esconde o cursos do Turtle
turtle.speed(0)     # Defini a Velocidade MAXIMA
turtle.tracer(0,0)  # Desativa a animação do turtle (Faz um desenho mais rapido)



# def alertbox():
#     tamanho = selecionar_tamanho_grade()
#     probabilidade = selecionar_probabilidade()
#     turtle.TK.messagebox.showinfo(title = "AVISO!", message = "É possível fechar a simulação utilizando a tecla [Q]")


turtle.onkeypress(parar, "q")
turtle.listen()