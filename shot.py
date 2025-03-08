from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0) # Initialize velocity    

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), 
                           self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt