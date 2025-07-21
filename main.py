# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
pygame.init()

clock = pygame.time.Clock()

def main():
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    screen=pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    player = Player(x=(SCREEN_WIDTH/2),y=(SCREEN_HEIGHT/2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
 

if __name__ == "__main__":
    main()
