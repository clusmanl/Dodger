import pygame
import random
from entities.Player import Player
from entities.Enemy import Enemy
from game.gameplay import test_collision

pygame.init()

# ----- CONSTANTS -------------------

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

WIDTH = 1024
HEIGHT = 800

SPAWN_ENEMY_ID_TOP = 1
SPAWN_ENEMY_ID_LEFT = 3
SPAWN_ENEMY_ID_RIGHT = 5
TIMER_MS_TOP = 100
TIMER_MS_SIDE = 1000

TIMER_ID = 2

# ----- INIT ------------------------

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dodger")

pygame.mouse.set_visible(False)

carryOn = True

clock = pygame.time.Clock()

player = Player(200, 200, 20, (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)))

enemies_from_top = []
enemies_from_left = []
enemies_from_right = []

pygame.time.set_timer(SPAWN_ENEMY_ID_TOP, TIMER_MS_TOP)
pygame.time.set_timer(SPAWN_ENEMY_ID_LEFT, TIMER_MS_SIDE)
pygame.time.set_timer(SPAWN_ENEMY_ID_RIGHT, 2000)
pygame.time.set_timer(TIMER_ID, 1000)

left_enemies = False
right_enemies = False

pygame.mouse.set_pos(WIDTH/2, HEIGHT*2/3)

# -------------- Score -----------------------------

pygame.font.init()
font = pygame.font.SysFont('Arial', 30)
score = 0
score_surface = font.render('Score: {}'.format(score), True, WHITE)
screen.blit(score_surface, (3, 3))


# -------------- Main Game Loop --------------------

while carryOn:

    screen.fill(BLACK)

    # ---------- Event Handling --------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == SPAWN_ENEMY_ID_TOP:
            enemies_from_top.append(Enemy(random.randint(0, WIDTH - 20), 0, random.randint(20, 60), (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)), random.randint(4, 6)))
        elif event.type == TIMER_ID:
            score = score + 1
            score_surface = font.render('Score: {}'.format(score), True, WHITE)
        elif event.type == SPAWN_ENEMY_ID_LEFT and left_enemies:
            enemies_from_left.append(Enemy(0, random.randint(0, HEIGHT), random.randint(20, 60), (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)), random.randint(4, 6)))
        elif event.type == SPAWN_ENEMY_ID_RIGHT and right_enemies:
            enemies_from_right.append(Enemy(WIDTH - 20, random.randint(0, HEIGHT), random.randint(20, 60), (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255)), random.randint(4, 6)))

    if score == 3:
        left_enemies = True

    if score == 6:
        right_enemies = True

    # ---------- Collision Handling ----------------

    if test_collision(enemies_from_top, player) or test_collision(enemies_from_right, player) \
            or test_collision(enemies_from_left, player):
        carryOn = False

    # ---------- Player moving ---------------------

    player.x = pygame.mouse.get_pos()[0]
    player.y = pygame.mouse.get_pos()[1]

    # ---------- Drawing entities ------------------

    for enemy in enemies_from_top:
        enemy.move_from_top(enemy.speed)
        pygame.draw.rect(screen, enemy.color, [enemy.x, enemy.y, enemy.width, enemy.width], 0)
        if enemy.y > HEIGHT:
            enemies_from_top.remove(enemy)

    for enemy in enemies_from_left:
        enemy.move_from_left(enemy.speed)
        pygame.draw.rect(screen, enemy.color, [enemy.x, enemy.y, enemy.width, enemy.width], 0)
        if enemy.x > WIDTH:
            enemies_from_left.remove(enemy)

    for enemy in enemies_from_right:
        enemy.move_from_right(enemy.speed)
        pygame.draw.rect(screen, enemy.color, [enemy.x, enemy.y, enemy.width, enemy.width], 0)
        if enemy.x < 0:
            enemies_from_right.remove(enemy)

    pygame.draw.rect(screen, RED, [player.x, player.y, player.width, player.width], 0)

    screen.blit(score_surface, (3, 3))
    pygame.display.flip()

    clock.tick(60)

carryOn = True
screen.fill(BLACK)
score_string = 'Your score is {}'.format(score)
screen.blit(score_surface, (WIDTH/2 - 50, HEIGHT/2))
pygame.display.flip()

while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    clock.tick(60)

pygame.quit()
