import pygame
from pygame import math

class PlayerManager2D(pygame.sprite.Sprite):
    def __init__(self, window_size = (650, 500), gravity = 1):
        super().__init__()
        self.object_size = (50, 50)
        self.surface = pygame.Surface(self.object_size)
        self.surface.fill((255, 0, 0))
        self.rect = self.surface.get_rect()
        
        self.position = math.Vector2()
        self.velocity = math.Vector2(0, 0)
        self.acceleration = math.Vector2(0, 0)
        self.gravity = gravity
        self.isGrounded = False
        
        self.window_size = window_size
    
    def set_player(self):
        self.position = math.Vector2(self.window_size[0] / 2, self.window_size[1] / 2)

    def jump(self, force_quantity):
        if self.isGrounded:
            self.velocity.y = -force_quantity

    def add_movement(self):
        self.acceleration = math.Vector2(0, self.gravity)

        if pygame.key.get_pressed()[pygame.K_a]:
            self.acceleration.x = -1
        if pygame.key.get_pressed()[pygame.K_d]:
            self.acceleration.x = 1

        self.acceleration.x += self.velocity.x * -.30
        self.velocity += self.acceleration 
        self.position += self.velocity + self.acceleration
        self.rect.midbottom = self.position
    
    def floor_collider(self, collision):
        collided = pygame.sprite.spritecollide(self, collision, False)
        if (collided):
            self.isGrounded = True
            self.position.y = collided[0].rect.top
            self.velocity.y = 0
        else:
            self.isGrounded = False