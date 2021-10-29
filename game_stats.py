class GameStats:
	"""Monitor statistics"""

	def __init__(self, ai_game):
		self.settings = ai_game.settings
		self.reset_stats()

		#Start the game in the inactive state
		self.game_active = False

		self.high_score = 0
		self.stats = 0
		
	def reset_stats(self):
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 0 


