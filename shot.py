import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, position, direction):
        super().__init__(position.x, position.y, radius=SHOT_RADIUS)
        self.position = pygame.math.Vector2(position)
        self.velocity = direction * PLAYER_SHOOT_SPEED
        for group in Shot.containers:
            group.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)