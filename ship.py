import pygame

class Ship:
	"""Class to manage the ship."""

	def __init__(self, ai_game):

		self.screen = ai_game.screen #enable access to screen from main class
		self.screen_rect = ai_game.screen.get_rect()

		#get the image
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#starting position of the ship
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""Display ship in the actual position."""
		self.screen.blit(self.image, self.rect)