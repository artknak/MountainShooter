#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window

        # Para adicionar o background do menu, precisamos carregá-la e adicioná-la a um retângulo Esse retângulo
        # representará a imagem de fundo.
        self.surf = pygame.image.load('./asset/MenuBg.png')  # Carregando imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # Retângulo é desenhado a partir do topo superior esquerdo

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')  # Carregando música do menu
        pygame.mixer_music.play(-1)  # Toca a música infinitamente

        while True:  # Loop para ficar infinitamente carregando o background
            self.window.blit(source=self.surf, dest=self.rect)  # Aplicando a imagem ao retângulo do background
            self.menu_text(75, 'Mountain', COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(75, 'Shooter', COLOR_ORANGE, ((WIN_WIDTH / 2), 115))

            # Laço para imprimir opções do menu
            for opt in range(len(MENU_OPTION)):
                # A cada laço, o texto é impresso com um offset de 30 px
                self.menu_text(25, MENU_OPTION[opt], COLOR_WHITE, ((WIN_WIDTH / 2), 170 + 25 * opt))

            pygame.display.flip()  # Atualizando tela

            # Criando evento para fechar janela!
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame


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

