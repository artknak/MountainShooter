#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':  # Background para o level 1
                list_bg = []
                for i in range(7):
                    # Instancia varios objetos Background passando nome e posição
                    # Como Background é parte de Entity, as imagens serão carregadas, já que em self.surf temos um
                    # pygame.load.image que recebe um nome e itera sobre asset de forma genérica.
                    list_bg.append(Background(f'Level1Bg{i}', position))

                    # Precisamos de 14 imagens no total. Isso ocorre pois quando movermos as 7 primeiras imagens total-
                    # mente para a esquerda, precisamos que haja continuidade no background, se não ficaria só um borrão.
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))

                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT // 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT // 2 + 30))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

