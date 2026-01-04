import pygame
from random import uniform, randint

class Player(pygame.sprite.Sprite):
	def __init__(self, groups, pos, keys, surf):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_frect(center = pos)
		self.speed = 400
		self.kup = keys[0]
		self.kdown = keys[1]
	def update(self, dt):
		keys = pygame.key.get_pressed()
		if keys[self.kup]:
			self.rect.top -= self.speed * dt
		if keys[self.kdown]:
			self.rect.bottom += self.speed * dt
		if self.rect.bottom >= 1280:
			self.rect.bottom = 1280 - 5
		if self.rect.top <= 0:
			self.rect.top = 5

class Ball(pygame.sprite.Sprite):
	def __init__(self, group, pos, surf):
		super().__init__(group)
		self.image = surf
		self.rect = self.image.get_frect(center = pos)
		self.direction = pygame.math.Vector2(randint(-1, 1), uniform(-0.45, 0.45))
		self.speed = 500
	def update(self, dt):
		if self.direction.x == 0:
			self.direction.x = randint(-1, 1)
		self.rect.center += self.direction * self.speed * dt
		if self.rect.top <= 0 or self.rect.bottom >= 1280:
			self.direction.y *= -1

class Death(pygame.sprite.Sprite):
	def __init__(self, groups, surf, rect):
		self.image = surf
		self.rect = rect


pygame.init()



def ping_pong():
	WIDTH, HEIGH = 1280, 720
	screen = pygame.display.set_mode((WIDTH, HEIGH))

	player_surf = pygame.surface.Surface((25, 150))
	player_surf.fill("white")
	line_surf = pygame.surface.Surface((5, HEIGH))
	line_surf.fill("white")
	ball_surf = pygame.surface.Surface((50, 50))
	ball_surf.fill("white")

	p1_death_surf = pygame.surface.Surface((200, HEIGH))
	p2_death_surf = pygame.surface.Surface((200, HEIGH))
	p1_lose_rect = p1_death_surf.get_frect(topleft = (0, 0))
	p2_lose_rect = p1_death_surf.get_frect(topleft = (WIDTH -200, 0))

	all_sprites = pygame.sprite.Group()
	player_sprites = pygame.sprite.Group()
	ball_sprites = pygame.sprite.Group()
	player1 = Player((all_sprites, player_sprites), (280, HEIGH/2), (pygame.K_w, pygame.K_s), player_surf)
	player2 = Player((all_sprites, player_sprites), (1000, HEIGH/2), (pygame.K_UP, pygame.K_DOWN), player_surf)
	ball = Ball((all_sprites, ball_sprites), (WIDTH/2, HEIGH/2), ball_surf)
	death_p1 = Death(all_sprites, p1_death_surf, p1_lose_rect)
	death_p2 = Death(all_sprites, p2_death_surf, p2_lose_rect)
	clock = pygame.time.Clock()
	p1_score = 0
	p2_score = 0
	run = True
	while run:
		dt = clock.tick(60) / 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				run = False

		all_sprites.update(dt)

		screen.fill("black")
		screen.blit(line_surf, (WIDTH/2, 0))
		all_sprites.draw(screen)
		if pygame.sprite.spritecollide(death_p1, ball_sprites, True):
			p2_score += 1
			print("Player 1 Score:", p1_score, "\tPlayer 2 Score: ", p2_score)
			ball = Ball((all_sprites, ball_sprites), (WIDTH/2, HEIGH/2), ball_surf)
		if pygame.sprite.spritecollide(death_p2, ball_sprites, True):
			p1_score += 1
			print("Player 1 Score:", p1_score, "\tPlayer 2 Score: ", p2_score)
			ball = Ball((all_sprites, ball_sprites), (WIDTH/2, HEIGH/2), ball_surf)
		if pygame.sprite.groupcollide(player_sprites, ball_sprites, False, False):
			ball.direction.x *= -1
			ball.direction.y = uniform(-0.45, 0.45)

		pygame.display.update()