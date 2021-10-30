class GameStats:
	"""Monitor statistics"""

	def __init__(self, ai_game):
		self.settings = ai_game.settings
		self.reset_stats()

		#Start the game in the inactive state
		self.game_active = False
		self.stats = 0

		with open('best_score.txt', 'r') as file_object:
			lines = file_object.readlines()
			lines_int = []
			for line in lines:
				line_int = int(line)
				lines_int.append(line_int)
		self.high_score = max(lines_int)
		self.max_high_score = max(lines_int)

	def reset_stats(self):
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 0


