import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        for group in self.containers:
            group.add(self)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_angle=random.uniform(30,50)
        v1 = self.velocity.rotate(new_angle)
        v2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius-ASTEROID_MIN_RADIUS
        A1 = Asteroid(self.position.x,self.position.y,new_radius)
        A2 = Asteroid(self.position.x,self.position.y,new_radius)
        A1.velocity = v1
        A2.velocity = v2
        for group in self.groups():
            group.add(A1)
            group.add(A2)
        
