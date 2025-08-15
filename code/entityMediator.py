from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.playerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        '''Verifica se inimigo atingiu o limite da tela.'''

        if isinstance(ent, Enemy):  # Verifica apenas em entidades Enemy
            if ent.rect.right < 0:
                ent.health = 0      # Zera a vida da entidade ao sair da tela

        if isinstance(ent, PlayerShot):
            if ent.rect.left > WIN_WIDTH:
                ent.health = 0      # Zera a vida das "balas" de Player ao saírem da tela

        if isinstance(ent, EnemyShot):
            if ent.rect.right < 0:
                ent.health = 0      # Zera a vida das "balas" de Enemy ao saírem da tela

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)  # Remove a entidade da lista (apaga a instância)