import sys
import time
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

class AlienInvasion:
	"""Class to manage resources and game in general (screen etc.)"""
	def __init__(self):
		"""Initializaion of the game"""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		''' Full screen option
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		'''
		#Create an instance of the statistics and score
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		#self.play_button = Button(self, "Play")
		#create difficulty buttons
		self.easy_button = Button(self, "Easy")
		self.mid_button = Button (self, "Medium")
		self.hard_button = Button(self, "Hard")

	def run_game(self):
		"""Main loop of the game"""
		while True:
			self._check_events()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()

			self._update_screen()

	def _check_events(self):
		"""Auxiliary method - Maintain events for mouse and keyboard."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if self.stats.high_score > self.stats.max_high_score:
					filename = 'best_score.txt'
					with open(filename, 'a') as file_object:
						file_object.write(f"{self.stats.high_score}\n")	
					sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				#self._check_play_button(mouse_pos)
				self._set_difficulty_level(mouse_pos)

	# def _check_play_button(self, mouse_pos):
	# 	button_clicked = self.play_button.rect.collidepoint(mouse_pos)
	# 	#reset settings for the next game
	# 	if button_clicked and not self.stats.game_active:

	# 		self.settings.initialize_dynamic_settings()
	# 		self._start_game()

	def _set_difficulty_level(self, mouse_pos):
		easy = self.easy_button.rect.collidepoint(mouse_pos)
		medium = self.mid_button.rect.collidepoint(mouse_pos)
		hard = self.hard_button.rect.collidepoint(mouse_pos)
		if easy and not self.stats.game_active:
			self.settings.initialize_dynamic_settings_easy()
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_ships()
			self._start_game()
		if medium and not self.stats.game_active:
			self.settings.initialize_dynamic_settings_mid()
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_ships()
			self._start_game()
		if hard and not self.stats.game_active:
			self.settings.initialize_dynamic_settings_hard()
			self.sb.prep_score()
			self.sb.prep_level()			
			self.sb.prep_ships()
			self._start_game()

	def _start_game(self):
		self.stats.reset_stats()
		self.stats.game_active = True
		self.sb.prep_score()
		self.sb.prep_ships()

		#Remove aliens list and bullets
		self.aliens.empty()
		self.bullets.empty()

		#Create new fleet and center ship()
		self._create_fleet()
		self.ship.center_ship()

		#Hide cursor
		pygame.mouse.set_visible(False)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			if self.stats.high_score > self.stats.max_high_score:
				filename = 'best_score.txt'
				with open(filename, 'a') as file_object:
					file_object.write(f"{self.stats.high_score}\n")	
			sys.exit()
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_g:
			self._start_game()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update bullets position and remove the outsided ones."""
		self.bullets.update()
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		"""Collision and remove"""
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points * len(aliens)
			self.sb.prep_score()

		if not self.aliens:
			#Remove bullets and create the fleet
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()

			#Increment level
			self.stats.level += 1
			self.sb.prep_level()

	def _update_aliens(self):
		"""Update position of aliens."""
		self._check_fleet_edges()
		self.aliens.update()

		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		self._check_aliens_bottom()
		#print(self.stats.ships_left)

	def _create_fleet(self):
		"""Set dimensions of alien in regards to screen, set number of aliens per row"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		#How many rows on the screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (2 * alien_height) - ship_height)
		number_rows = available_space_y	// (2 * alien_height)

		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _ship_hit(self):
		"""After ship hits an alien"""
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			self.sb.prep_ships()
			self.ship.center_ship()
			#Empty aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			

			time.sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)
			if self.stats.score > self.stats.high_score:
				self.stats.high_score = self.stats.score
				self.sb.prep_high_score()

	def _check_aliens_bottom(self):
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break

	def _create_alien(self, alien_number, row_number):
		#Create first row of aliens
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""When alien reach the edge of the screen."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Moving fleet down."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_screen(self):
		"""Auxiliary method - Refresh background for every loop"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

	

		#display score
		self.sb.show_score()

		if not self.stats.game_active:
			#self.play_button.draw_button()

			self.easy_button.draw_button()
			self.mid_button.draw_button()
			self.hard_button.draw_button()


		#Display last screen
		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()