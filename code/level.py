#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode  # Modo de jogo
        self.entity_list: list[Entity] = []  # Lista de entidades (contém background, player e inimigos)
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))  # Adidicionando background do lvl 1

        player = EntityFactory.get_entity('Player1')  # Adicionando player
        player.score = player_score[0]
        self.entity_list.append(player)

        # Só spawna player 2 se o game_mode for COOP ou COMP
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')  # Adicionando player
            player.score = player_score[1]
            self.entity_list.append(player)

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)      # Seta um timer em ms para a geração de inimigos
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # Checa a condição de vitória a cada 100 ms

    def run(self, player_score: list[int]):
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

                if isinstance(entity, (Player, Enemy)):  # A bala também é uma entidade
                    shoot = entity.shoot()
                    if shoot is not None:                # Se uma entidade (Player, Enemy) atirar
                        self.entity_list.append(shoot)   # Uma bala é adicionada a lista de entidades

                if entity.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {entity.health} / Score: {entity.score}',
                                    C_GREEN, (10, 25))
                if entity.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {entity.health} / Score: {entity.score}',
                                    C_CYAN, (10, 45))

            # Evento para fechar a janela do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Checa se pode fazer spawn de um inimigo
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                # Decrementa self.timeout conforme o timer e com o TIMEOUT_STEP
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:

                        for ent in self.entity_list:  # Atualiza os scores para os players
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score

                        return True  # Retorna True para encerrar o level

                # Se Player morrer, finaliza jogo e não permite avançar para próxima fase
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # Level text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f} s',
                            C_WHITE, (10, 5))  # Timeout text (tempo de duração da fase)
            self.level_text(14, f'Fps: {clock.get_fps():.0f}',
                            C_WHITE, (10, WIN_HEIGHT - 35))  # Fps text
            self.level_text(14, f'Entidades: {len(self.entity_list)}',
                            C_WHITE, (10, WIN_HEIGHT - 20))  # Entity text (mostra quantos têm na fase)
            pygame.display.flip()

            EntityMediator.verify_collision(self.entity_list)  # Verificador de colisões

            # Verifica a vida da entidade
            # Se for 0, apaga a entidade de entity_list, ou seja, a apaga do jogo
            EntityMediator.verify_health(self.entity_list)

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
