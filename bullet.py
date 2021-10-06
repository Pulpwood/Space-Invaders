import pygame
from pygame.sprite import Sprite #sprite enable to group the elements and perform an action on the whoule group

class Bullet(Sprite):
	"""Class to manage bullets"""
	def __init__(self, ai_game):
		#create a bullet in the present ship position
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		#create bullet in the (0, 0) and define its position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		self.y = float(self.rect.y)

	def update(self):
		self.y -= self.settings.bullet_speed
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

