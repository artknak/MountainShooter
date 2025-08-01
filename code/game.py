#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        # pygame.init é obrigatório para iniciar o pygame e todas
        # as suas dependências!
        pygame.init()
        # Criando a janela do jogo.
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        # A janela precisa de um loop para se manter aberta.
        while True:
            menu = Menu(self.window)
            menu.run()

