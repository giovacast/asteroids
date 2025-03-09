import pygame   
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        pygame.Surface.fill(screen, (0, 0, 0))

        for item in drawables:
             item.draw(screen)

        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in player.shots:
                if asteroid.collides_with(shot):
                    asteroid.kill()
                    shot.kill()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000.0

print("Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()