#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        while True:
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()  # Chamando método de movimento
            pygame.display.flip()
