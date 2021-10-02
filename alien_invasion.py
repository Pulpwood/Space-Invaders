import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Class to manage resources and game in general (screen etc.)"""
	def __init__(self):
		"""Initializaion of the game"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)

	def run_game(self):
		"""Main loop of the game"""
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		"""Auxiliary method - Maintain events for mouse and keyboard."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_screen(self):
		"""Auxiliary method - Refresh background for every loop"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		#Display last screen
		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()