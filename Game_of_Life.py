from celulas import iniciando_a_vida, update_life
from tela import iniciar_tela, desenhar_grid, turtle
    
def main():
    iniciar_tela()
    iniciando_a_vida()
    update_life()
    desenhar_grid()

turtle.done()