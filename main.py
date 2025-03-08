import pygame   
from constants import *
import circleshape
import player
import asteroid
import asteroidfield
import shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    asteroid.Asteroid.containers = (asteroids, updatables, drawables)
    asteroidfield.AsteroidField.containers = (updatables)
    player.Player.containers = (updatables, drawables)
    shot.Shot.containers = (shots, updatables, drawables)

    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = asteroidfield.AsteroidField()
    

    while True:
        pygame.Surface.fill(screen, (0, 0, 0))

        for item in drawables:
             item.draw(screen)

        updatables.update(dt)

        for item in asteroids:
            item.check_for_collision(player1)

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