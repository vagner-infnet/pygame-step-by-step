"""
exibindo uma tela vazia.
a tela abre.
redesenhado forma numa superfície
a tela fecha automatiamente.
"""
import pygame

def exibe_janela_e_desenha_1forma():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    tupla_largura_altura = (largura_da_JANELA, altura_da_JANELA)
    #JANELA > PRECISAMOS GRAVAR UMA REFERÊNCIA DA JANELA DO PROGRAMA
    JANELA = pygame.display.set_mode(tupla_largura_altura)
    pygame.display.set_caption("Desenhando uma forma")
    pygame.display.init()
    ####################################################
    largura_do_PAINEL_1 = largura_da_JANELA/2
    altura_do_PAINEL_1 = altura_da_JANELA/2       
    largura_altura_do_PAINEL_1 = (largura_do_PAINEL_1, altura_do_PAINEL_1)
    PAINEL_1 = pygame.surface.Surface(largura_altura_do_PAINEL_1)

    y_inicial_do_PAINEL_1 = 0
    x_inicial_do_PAINEL_1 = 0
    def reseta_painel_1():
        print("desenhando painel_1")
        cor_do_PAINEL_1 = (255, 255, 255)  # branco
        PAINEL_1.fill(cor_do_PAINEL_1)  # pintando o painel com a cor desejada
    #JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  # inserindo o painel na janela
    reseta_painel_1()
    ####################################################
    #configurando superfície
    def forma_1(contador):
        print("desenhando forma_1")
        
        cor_da_FORMA_1 = (0, 0, 255)  # azul
        x_inicial_da_FORMA_1 = 0
        y_inicial_da_FORMA_1 = 0
        largura_da_FORMA_1 = contador        
        altura_da_FORMA_1 = contador 
        pygame.draw.rect(PAINEL_1, cor_da_FORMA_1, (x_inicial_da_FORMA_1, y_inicial_da_FORMA_1, largura_da_FORMA_1, altura_da_FORMA_1))
        #AGORA QUE DESENHEI UM RECT NO PAINEL, DEVO PEDIR À JANELA PARA RECEBER O PAINEL
        #JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  # inserindo o painel na janela
    ####################################################
    continuar_no_loop_while = True
    contador = 0
    ####################################################   
    while continuar_no_loop_while:
        ######################################
        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                continuar_no_loop_while = False
                #continue  # sair deste loop for
        contador = contador + 1
        if contador == altura_do_PAINEL_1:
            contador = 0
        #painel_1(contador)
        reseta_painel_1()
        forma_1(contador)
        # Fazendo a janela exibir os componentes com seus valores atualizados
        JANELA.blit(PAINEL_1, (x_inicial_do_PAINEL_1, y_inicial_do_PAINEL_1))  # inserindo o painel na janela
        pygame.display.update()
        pygame.time.Clock().tick(60) # nº de atualizações por segundo
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_desenha_1forma()