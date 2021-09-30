import sys
import pygame

class AlienInvasion:
	"""Class to manage resources and game in general (screen etc.)"""
	def __init__(self):
		"""Initializaion of the game"""

		pygame.init()


		self.screen = pygame.display.set_mode((600, 500))
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		"""Main loop of the game"""
		while True:
			#Press button or mouse
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()