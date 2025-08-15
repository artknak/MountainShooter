#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo
        self.entity_list: list[Entity] = []  # Lista de entidades (contém background, player e inimigos)
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # Adidicionando background do lvl 1
        self.entity_list.append(EntityFactory.get_entity('Player1'))   # Adicionando player

        # Só spawna player 2 se o game_mode for COOP ou COMP
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Seta um timer em ms para a geração de inimigos

    def run(self):
        # Carregando música
        pygame.mixer_music.load(f'asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:
            # Definindo fps
            clock.tick(60)

            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()  # Chamando método de movimento
            pygame.display.flip()

            # Evento para fechar a janela do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # Level text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f} s',
                            COLOR_WHITE, (10, 5))  # Timeout text (tempo de duração da fase)
            self.level_text(14, f'Fps: {clock.get_fps():.0f}',
                            COLOR_WHITE, (10, WIN_HEIGHT - 35))  # Fps text
            self.level_text(14, f'Entidades: {len(self.entity_list)}',
                            COLOR_WHITE, (10, WIN_HEIGHT - 20))  # Entity text (mostra quantos têm na fase)
            pygame.display.flip()

            EntityMediator.verify_collision(self.entity_list)  # Verificador de colisões

            # Verifica a vida da entidade
            # Se for 0, apaga a entidade de entity_list, ou seja, a apaga do jogo
            EntityMediator.verify_health(self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
