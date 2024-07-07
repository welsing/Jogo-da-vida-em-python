import turtle
from interface import setup_screen, draw_grid, desenhar_vida_total, update_life, parar
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

    life = game.iniciando_a_vida(tamanho, probabilidade_selecionada)
    
    setup_screen()
    draw_grid(tamanho)
    desenhar_vida_total(life, tamanho)
    update_life(life, tamanho)

    turtle.onkeypress(parar, "q")
    turtle.listen()
    turtle.done()

if __name__ == "__main__":
    main()