#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH


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
