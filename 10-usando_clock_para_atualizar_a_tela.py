"""
Faremos um painel(superfície) começar com tamanho 0 
e crescer até o tamanho da janela.
Usaremos Clock para a frequência de atualização da tela
"""
import pygame

def exibe_janela_e_usa_clock_para_atualizar_a_tela_numa_certa_frequencia():
    
    largura_da_JANELA = 400
    altura_da_JANELA = 400
    largura_altura_da_JANELA = (largura_da_JANELA, altura_da_JANELA)
    #JANELA > PRECISAMOS GRAVAR UMA REFERÊNCIA DA JANELA DO PROGRAMA
    JANELA = pygame.display.set_mode(largura_altura_da_JANELA)
    pygame.display.set_caption("Usando Clock")
    pygame.display.init()
    ####################################################
    def reseta_JANELA():
        #pintamos a janela, para apagar seu conteúdo
        cor_da_JANELA = (0, 0, 0)  # preto
        JANELA.fill(cor_da_JANELA)
    ####################################################
    #configurando superfície
    def set_painel_1(contador):

        print("desenhando painel_1")

        largura_do_PAINEL_1 = contador
        altura_do_PAINEL_1 = contador
        largura_altura_do_PAINEL_1 = (largura_do_PAINEL_1, altura_do_PAINEL_1)        
        PAINEL_1 = pygame.surface.Surface(largura_altura_do_PAINEL_1)       
        # pintando o painel com a cor desejada
        cor_do_PAINEL_1 = (255, 255, 255)  # branco 
        PAINEL_1.fill(cor_do_PAINEL_1) 

        distancia_da_esq_para_a_dir_do_PAINEL_1 = 0
        distancia_de_cima_para_baixo_do_PAINEL_1 = 0
        #desenhamos(blit) o painel na janela
        JANELA.blit(PAINEL_1, (distancia_da_esq_para_a_dir_do_PAINEL_1, distancia_de_cima_para_baixo_do_PAINEL_1))  # inserindo o painel na janela
    ####################################################
    continuar_no_loop_while = True
    contador = 0
    ####################################################
    while continuar_no_loop_while:
        
        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                continuar_no_loop_while = False
                continue  # sair deste loop for, sem executar as demais linhas dentro de while
        contador = contador + 1
        #contador == 400 > o painel tomou a área total da janela
        if contador > 400:
            #faremos o painel começar do zero, novamente
            contador = 0
        reseta_JANELA()
        set_painel_1(contador)
        # Fazendo a janela exibir os componentes com seus valores atualizados
        pygame.display.update()
        # clock permite acelerar/desacelerar o número de whiles por segundo
        pygame.time.Clock().tick(60)
    ####################################################
    # após ter feito tudo que queríamos, fechamos o programa:
    #pygame.display.quit() 

exibe_janela_e_usa_clock_para_atualizar_a_tela_numa_certa_frequencia()
