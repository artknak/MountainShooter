#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame.image


# Background, player e enemy serão gerados a partir da classe abstrata Entity.
# Cada entidade recebe um nome, uma posição e uma velocidade (útil principalmente para fazer Parallax no background).
# Além disso, as entidades devem implementar o método move().

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('asset/' + name + '.png')             # Carregando imagens de modo genérico
        self.rect = self.surf.get_rect(left=position[0], top=position[1])   # Definindo posições através de tupla
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
