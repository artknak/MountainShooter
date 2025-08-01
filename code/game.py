#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.menu import Menu


class Game:
    def __init__(self):
        # pygame.init é obrigatório para iniciar o pygame e todas
        # as suas dependências!
        pygame.init()
        # Criando a janela do jogo.
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        # A janela precisa de um loop para se manter aberta.
        while True:
            menu = Menu(self.window)
            menu.run()

            # Check for all events.
            # Criando evento para fechar janela!
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # Close window
            #         quit()  # End pygame