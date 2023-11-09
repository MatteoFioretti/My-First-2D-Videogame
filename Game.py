import pygame
from sys import exit


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.walking_right = False        
        self.walking_left = False        
        self.player_stand = pygame.image.load("Graphic/Player/player_stand.png").convert_alpha()
        player_walk_1 = pygame.image.load("Graphic/Player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("Graphic/Player/player_walk_2.png").convert_alpha()
        player_walk_1_flipped = pygame.transform.flip(player_walk_1,True,False)
        player_walk_2_flipped = pygame.transform.flip(player_walk_2,True,False)
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_walk_flipped = [player_walk_1_flipped,player_walk_2_flipped]
        self.player_index = 0
        
        self.jump = pygame.image.load("Graphic/Player/jump.png").convert_alpha()
        self.jump_flipped = pygame.transform.flip(self.jump, True,False)
        
        self.image = self.player_stand
        self.rect = self.image.get_rect(midbottom = (50,330))
        self.gravity = 0
        self.jump_strength = -20
        
    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 330:
            self.rect.bottom = 330
    
    def player_jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 330:
            self.gravity = self.jump_strength

    def player_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect.bottom == 330:
            self.walking_right = True
            self.rect.right += 3
            if self.rect.right >= screen_wdt:
                self.rect.right = screen_wdt
            
        if keys[pygame.K_a] and self.rect.bottom == 330:
            self.walking_left = True
            self.rect.left -= 3
            if self.rect.left <= 0:
                self.rect.left = 0
    
    def player_animations(self):
        if self.rect.bottom < 330:
            self.image = self.jump
        
        elif self.rect.bottom < 330 and self.walking_left:
            self.image = self.jump_flipped
        
        elif self.walking_right:   
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        
        elif self.walking_left:   
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk_flipped[int(self.player_index)]

        else:
             self.image = self.player_stand
        

    def update(self):
        self.player_move()
        self.player_jump()
        self.player_gravity()
        self.player_animations()

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

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())


# Game
while True:

    # Check for user's inputs
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.sprite.walking_right = False
            elif event.key == pygame.K_a:
                player.sprite.walking_left = False
     
    
    # blitted surfaces
    screen.blit(sky_resized,sky_rect)
    screen.blit(ground_resized,ground_rect)
    
    #player animations
    player.draw(screen)
    player.update()
    
    pygame.display.update()
    # 60 frames every iteration 
    clock.tick(60)

   