import pygame.font

class Button():
	def __init__(self, ai_game, msg):
		""" Show button"""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		#define buttons dimensions
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		self.interspace = 50
		self.easy_width, self.easy_height = self.screen_rect.center[0] - self.width - self.interspace, self.screen_rect.center[1]
		self.hard_width, self.hard_height = self.screen_rect.center[0] + self.width + self.interspace, self.screen_rect.center[1]

		#Create buttons and adjust to mid
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		if msg == 'Play':
			self.rect.center = self.screen_rect.center
		elif msg == 'Easy':
			self.rect.center = self.easy_width, self.easy_height
		elif msg == 'Medium':
			self.rect.center = self.screen_rect.center
		elif msg == 'Hard':
			self.rect.center = self.hard_width, self.hard_height


		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Insert text to buttton"""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		#Display empty button
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


