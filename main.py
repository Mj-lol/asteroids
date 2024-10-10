# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from asteroid import *
from asteroidfield import *
from constants import *
from player import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    dt = 0
    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    f = AsteroidField()
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for p in updatable:
            p.update(dt)
        for a in asteroids:
            if a.collide(player):
                print("Game over!")
                sys.exit()
            for s in shots:
                if a.collide(s):
                    a.split()
                    s.kill()

        screen.fill("gray")

        for p in drawable:
            p.draw(screen)

        pygame.display.flip()

        time = clock.tick(60)
        dt = time/1000



if __name__ == "__main__":
    main()
