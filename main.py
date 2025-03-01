import pygame
from constants import *
import circleshape
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    p1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        pygame.Surface.fill(screen, (0, 0, 0))
        p1.draw(screen)    
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        clock.tick(60)

        dt = clock.tick(60) / 1000.0

print("Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()