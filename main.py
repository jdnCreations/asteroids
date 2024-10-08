# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from asteroid import *
from shot import *
from constants import *
from asteroidfield import *
import sys

def main():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(x, y)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ASTEROIDS")
    print("Starting asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000

        for item in updatable:
          item.update(dt)

        for item in asteroids:
          for shot in shots:
            if shot.collided(item):
              item.split()
              shot.kill()
          if player.collided(item):
            print("Game over!")
            sys.exit()


        for item in shots:
          item.draw(screen)


        for item in drawable:
          item.draw(screen)

        pygame.display.flip()

        

if __name__ == "__main__":
    main()
