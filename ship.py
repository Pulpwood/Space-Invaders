import pygame

class Ship:
	"""Class to manage the ship."""

	def __init__(self, ai_game):
		#enable access to screen from main class
		self.screen = ai_game.screen 
		#enable settings
		self.settings = ai_game.settings 

		self.screen_rect = ai_game.screen.get_rect()

		#get the image
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#starting position of the ship
		self.rect.midbottom = self.screen_rect.midbottom

		#change position of the ship to float data type
		self.x = float(self.rect.x)

		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the position of the ship."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		#update rect base on self.x
		self.rect.x = self.x

	def blitme(self):
		"""Display ship in the actual position."""
		self.screen.blit(self.image, self.rect)