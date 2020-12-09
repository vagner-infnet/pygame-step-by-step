"""
exibindo uma tela vazia.
a tela abre.
escutamos a seta direita
para fechar a tela.
"""
import pygame

def exibe_janela_e_escuta_a_seta_direita():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    largura_altura_da_JANELA = (largura_da_JANELA, altura_da_JANELA)
    pygame.display.set_mode(largura_altura_da_JANELA)
    pygame.display.set_caption("Pressione a seta para a direita para encerrar.")
    pygame.display.init()
    ####################################################
    continuar_no_loop_while = True
    contador = 0
    ####################################################
    while continuar_no_loop_while:

        events = pygame.event.get()
        
        for event in events:
            print(f"novo evento detectado nº {contador}")
            contador = contador + 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    continuar_no_loop_while = False              
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_escuta_a_seta_direita()
