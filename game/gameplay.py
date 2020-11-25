from entities.Player import Player
from entities.Enemy import Enemy


def test_collision(enemies, player):
    for enemy in enemies:
        if (enemy.x + enemy.width) >= player.x >= enemy.x or (enemy.x + enemy.width) >= (player.x + player.width) >= enemy.x:
            if(enemy.y + enemy.width) >= player.y >= enemy.y or (enemy.y + enemy.width) >= (player.y + player.width) >= enemy.y:
                return True

    return False
