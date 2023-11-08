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

while True:
    continue