class Settings:
	"""Store the game settings."""
	def __init__(self):
		"""Initialization of game settings."""
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 550
		self.bg_color = (230,230,230)

		self.ship_speed = 1.8

		#bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 9

		#Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		self.fleet_direction = 1



