import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def show_score():
    draw_text(screen, str(score), 18, WIDTH // 2, 10)

def game_over():
    draw_text(screen, "Game Over", 64, WIDTH // 2, HEIGHT // 4)
    draw_text(screen, "Press R to play again", 22, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centerx = HEIGHT // 2
        self.vel_y = 0
    
    def update(self):
        self.vel_y += 1
        self.rect.y += self.vel_y
        if self.rect.bottom > HEIGHT:
            game_over()
    
    def jump(self):
        self.vel_y = -10

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 300))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randrange(HEIGHT // 2 + 50)
    
    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

score = 0

for i in range(2):
    pipe = Pipe()
    all_sprites.add(pipe)
    pipes.add(pipe)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, pipes, False)
    if hits:
        game_over()

    if player.rect.bottom > HEIGHT:
        game_over()

    if player.rect.top < 0:
        player.rect.top = 0
    
    if player.rect.bottom > HEIGHT:
        player.rect.bottom = HEIGHT

    if player.rect.bottom < HEIGHT:
        score += 0.01
    
    screen.fill(BLACK)
    all_sprites.draw(screen)
    show_score()
    pygame.display.flip()

pygame.quit()