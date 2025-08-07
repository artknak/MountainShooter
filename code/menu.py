#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window

        # Para adicionar o background do menu, precisamos carregá-la e adicioná-la a um retângulo. Esse retângulo
        # representará a imagem de fundo.
        self.surf = pygame.image.load('./asset/MenuBg.png')  # Carregando imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # Retângulo é desenhado a partir do topo superior esquerdo

    def run(self):
        menu_option = 0  # Possibilita opções no menu (Ex: "NEW GAME - 1P" é representado por menu_option = 0)
        pygame.mixer_music.load('./asset/Menu.mp3')  # Carregando música do menu
        pygame.mixer_music.play(-1)  # Toca a música infinitamente

        while True:  # Loop para ficar infinitamente carregando o background
            self.window.blit(source=self.surf, dest=self.rect)  # Aplicando a imagem ao retângulo do background
            self.menu_text(75, 'Mountain', COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(75, 'Shooter', COLOR_ORANGE, ((WIN_WIDTH / 2), 115))

            # Laço para imprimir opções do menu
            # A cada repetição, as opções são impressas com um offset de 30 px
            for opt in range(len(MENU_OPTION)):
                if opt == menu_option:
                    # If para pintar o texto selecionado de amarelo
                    self.menu_text(25, MENU_OPTION[opt], COLOR_YELLOW, ((WIN_WIDTH / 2),
                                                                        170 + 25 * opt))
                else:
                    self.menu_text(25, MENU_OPTION[opt], COLOR_WHITE, ((WIN_WIDTH / 2),
                                                                       170 + 25 * opt))
            pygame.display.flip()  # Atualizando tela

            # Registrando eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                   # Evento para encerrar janela
                    pygame.quit()                               # Close window
                    quit()                                      # End pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:              # Possibilita descer no menu
                        if menu_option < len(MENU_OPTION) - 1:  # Usuário é permitido descer somente até o exit
                            menu_option += 1                    # Sem isso, poderia descer até sair da tela
                        else:
                            menu_option = 0                     # Volta ao início se menu_option for > len(MENU_OPTION)

                    if event.key == pygame.K_UP:                # Possibilita subir no menu
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1

                    if event.key == pygame.K_RETURN:            # Registra enter no menu
                        return MENU_OPTION[menu_option]         # Pega opção no menu através do seu índice




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """
        Define tamanho, conteúdo, cor e posição do texto do menu.
        """
        # Define a fonte do texto e seu tamanho
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        # Aplica cor ao texto e o converte para uma imagem
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        # Criando retângulo para inserir imagem do texto
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        # Desenhando retângulo
        self.window.blit(source=text_surf, dest=text_rect)

