import turtle
from tela import setup_screen, desenhar_grid, acender_população_viva, atualizar_população, parar
import game

def main():
    screen = turtle.Screen()
    turtle.TK.messagebox.showinfo(title="AVISO!", message="É possível fechar a simulação utilizando a tecla [Q]")
    
    while True:
        tamanho = screen.textinput("Grid", "Tamanho da Grid (n X n)")
        if not tamanho.isdigit():
            turtle.TK.messagebox.showinfo(title="AVISO!", message="DIGITE APENAS NÚMEROS!")
        else:
            tamanho = int(tamanho)
            break

    while True:
        probabilidade_selecionada = screen.textinput("Probabilidade de Vida", "ESCOLHA 1 A 7 (1 sendo o máximo e 7 o mínimo.)")
        if not probabilidade_selecionada.isdigit() or int(probabilidade_selecionada) not in range(1, 8):
            turtle.TK.messagebox.showinfo(title="AVISO!", message="A escolha precisa ser entre 1 e 7!")
        else:
            probabilidade_selecionada = int(probabilidade_selecionada)
            break

    população_geral = game.iniciando_a_vida(tamanho, probabilidade_selecionada)
    
    setup_screen()
    desenhar_grid(tamanho)
    acender_população_viva(população_geral, tamanho)
    atualizar_população(população_geral, tamanho)

    turtle.onkeypress(parar, "q")
    #turtle.onkeypress(game.alterar_velocidade, "t")
    turtle.listen()
    turtle.done()


main()