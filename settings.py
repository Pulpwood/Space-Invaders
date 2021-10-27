class Settings:
	"""Store the game settings."""
	def __init__(self):
		"""Initialization of game settings."""
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 550
		self.bg_color = (230,230,230)

		#self.ship_speed = 2.8
		self.ship_limit = 2

		#bullet settings
		#self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 9

		#Alien settings
		#self.alien_speed = 1.0
		self.fleet_drop_speed = 7
		#self.fleet_direction = 1

		self.speedup_scale = 1.2

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0
		self.fleet_direction = 1

	def initialize_dynamic_settings_easy(self):
		self.ship_speed = 1.5
		self.bullet_speed = 2.0
		self.alien_speed = 0.33
		self.fleet_direction = 1

	def initialize_dynamic_settings_mid(self):
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 0.8
		self.fleet_direction = 1

	def initialize_dynamic_settings_hard(self):
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.3
		self.fleet_direction = 1
	#def initialize_dynamic_settings_changing_difficulty(self)

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

