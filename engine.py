import sys 
import pygame
from player import PlayerManager2D
from gameobjects import GameObjects

pygame.init()
size = width, height = 650, 500
black = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

player = PlayerManager2D()
player.set_player()

floor1 = GameObjects(size[0] / 2, size[1], size[0], 40)
flours = pygame.sprite.Group()
flours.add(floor1)

all_objects = pygame.sprite.Group()
all_objects.add(player)
all_objects.add(floor1)

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump(20)

    screen.fill(black)

    player.add_movement()
    player.floor_collider(flours)
    
    for object in all_objects:
        screen.blit(object.surface, object.rect)
        
    pygame.display.update()