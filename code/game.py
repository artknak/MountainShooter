#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        # pygame.init é obrigatório para iniciar o pygame e todas
        # as suas dependências!
        pygame.init()
        # Criando a janela do jogo.
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        # A janela precisa de um loop para se manter aberta.
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()  # Recebe o return (quando é registrado ENTER) do menu.py

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                # Instancia level passando tamanho de janela, nome e o tipo de jogo (1 player, 2 player COOP, etc)
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:  # Opção EXIT (fecha o jogo)
                pygame.quit()
                quit()
            else:
                pass


