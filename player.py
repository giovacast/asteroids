from constants import *
from circleshape import CircleShape
import pygame
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shots = [] #List to store shots
		self.shoot_timer = 0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
		
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), width=2)

	def rotate(self, dt):
		self.rotation += (PLAYER_TURN_SPEED * dt)

	def update(self, dt):
		self.shoot_timer -= dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)	
		if keys[pygame.K_SPACE]:
			self.shoot()
	
		# Update all shots
		# Use a copy of the list to modify while iterating
		for shot in self.shots[:]: 
			shot.update(dt)
	
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):			
		if self.shoot_timer > 0:
			return
		self.shoot_timer = PLAYER_SHOOT_COOLDOWN
		# Create new shot at player's position
		shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
		# Set velocity based on player's rotation
		shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation) 
					* PLAYER_SHOOT_SPEED)
		# Add to shots list
		self.shots.append(shot)