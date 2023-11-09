import pygame
from sys import exit


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Enemy (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


pygame.init()

# Screen Setup
screen_wdt = 800
screen_hgt = 400
screen = pygame.display.set_mode((screen_wdt,screen_hgt))
pygame.display.set_caption("MyFirstGame")


# Clock Setup
clock = pygame.time.Clock()

# Background surface setup
sky = pygame.image.load("Graphic/Background/sky.png").convert()
sky_resized = pygame.transform.scale(sky,(800,400))
sky_rect = sky_resized.get_rect(topleft = (0,0))

ground = pygame.image.load("Graphic/Background/ground.png")
ground_resized = pygame.transform.scale(ground,(1600,100))
ground_rect = ground_resized.get_rect(midbottom = (0,screen_hgt+30))

# Game
while True:

    # Check for user's inputs
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
    
    
    screen.blit(sky_resized,sky_rect)
    screen.blit(ground_resized,ground_rect)
    
    pygame.display.update()
    # 60 frames every iteration 
    clock.tick(60)

   