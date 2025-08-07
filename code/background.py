#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Quando o background for totalmente movido para a esquerda, reseta a posição para depois da direita (WIN_WIDTH)
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
