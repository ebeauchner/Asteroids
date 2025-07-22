# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
pygame.init()

from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

clock = pygame.time.Clock()

def main():
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    screen=pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)

    player = Player(x=(SCREEN_WIDTH/2),y=(SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for item in asteroids:
            if item.check_collision(player):
                print("Game Over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
 

if __name__ == "__main__":
    main()
