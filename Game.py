import pygame
from sys import exit


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Enemy (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

# Screen Setup
screen_wdt = 800
screen_hgt = 400
screen = pygame.display.set_mode((screen_wdt,screen_hgt))

# Clock Setup
clock = pygame.time.Clock()

# Game
while True:

    # Check for user's inputs
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

   