import pygame
from sys import exit
from random import randint


class Sky(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sky = pygame.image.load("Graphic/Background/sky.png").convert()
        self.image = self.sky
        self.rect = self.image.get_rect(topleft = (0,0))
        
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ground = pygame.image.load("Graphic/Background/ground.png")
        self.image = self.ground
        self.rect = self.image.get_rect(topleft = (0,300))
        
class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.walking_right = False        
        self.walking_left = False        
        self.gravity = 0
        self.jump_strength = -20
        
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
        
        # by default the player will stand
        self.image = self.player_stand
        self.rect = self.image.get_rect(midbottom = (50,300))
        
    
    def reset(self):
        # Reset player attributes to initial values
        self.rect.midbottom = (50, 300)
        self.walking_right = False
        self.walking_left = False
        self.gravity = 0
        self.jump_strength = -20
        self.player_index = 0
        self.image = self.player_stand

    
    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def player_jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 300:
            self.gravity = self.jump_strength

    def player_move(self):
        keys = pygame.key.get_pressed()
        letter_D = keys[pygame.K_d]
        letter_A = keys[pygame.K_a]
        
        if letter_D:
            self.walking_right = True
            self.rect.right += 3
            if self.rect.right >= screen_wdt:
                self.rect.right = screen_wdt
            
        if letter_A:
            self.walking_left = True
            self.rect.left -= 3
            if self.rect.left <= 0:
                self.rect.left = 0
    
    def player_animations(self):
        if self.rect.bottom < 300:
            if self.walking_left:
                self.image = self.jump_flipped
            else: 
                self.image = self.jump
        
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
        self.player_jump()
        self.player_move()
        self.player_gravity()
        self.player_animations()

class Enemy (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        enemy_walk_1 = pygame.image.load("Graphic/Enemy/snail1.png")
        enemy_walk_2 = pygame.image.load("Graphic/Enemy/snail2.png")
        self.enemy_walk = [enemy_walk_1,enemy_walk_2]
        self.enemy_walk_index = 0
        
        self.image = self.enemy_walk[self.enemy_walk_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),300))
    
    def enemy_move(self):
        self.rect.left -= 6
        if self.rect.left <= 0:
            self.kill()
    
    def animation(self):
        self.enemy_walk_index += 0.06
        if self.enemy_walk_index >= len(self.enemy_walk):
            self.enemy_walk_index = 0
        else:
            self.image = self.enemy_walk[int(self.enemy_walk_index)]
            
    
    def update(self):
        self.enemy_move()    
        self.animation()

def game_over():
    if pygame.sprite.spritecollide(player.sprite,enemy_group,False):
        enemy_group.empty()
        return True
    return False    
    
def player_kill():
    for enemy in enemy_group.sprites():
        if player.sprite.rect.colliderect(enemy.rect) and player.sprite.rect.midbottom[1] < enemy.rect.midbottom[1]:
            enemy.kill()
            return 1
    return 0

def score(kills):
    score_surf = font.render(f"SCORE: {kills}",False,(0,0,0))
    score_surf_scaled = pygame.transform.scale(score_surf,(score_surf.get_width() * 2, score_surf.get_height() * 2))
    score_rect = score_surf.get_rect(center = (screen_wdt//2, 35))
    screen.blit(score_surf_scaled,score_rect)

pygame.init()

game_active = False
kills = 0

font = pygame.font.SysFont("lucidasansdemigrassettocorsivo", 10)

# Screen Setup
screen_wdt = 800
screen_hgt = 400
screen = pygame.display.set_mode((screen_wdt,screen_hgt))
pygame.display.set_caption("MyFirstGame")
pygame.display.set_icon(pygame.image.load("Graphic/Player/player_stand.png").convert_alpha())

# Clock Setup
clock = pygame.time.Clock()

# Sky
sky = pygame.sprite.GroupSingle()
sky.add(Sky())

ground = pygame.sprite.GroupSingle()
ground.add(Ground())

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Enemy
enemy_group = pygame.sprite.Group()
# Enemy timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,1500)

#title surface
title_surf = font.render("Pixel runner",False,(111,196,169))
title_surf_scaled = pygame.transform.scale(title_surf, (title_surf.get_width() * 5.5, title_surf.get_height() * 5.5)).convert_alpha()
title_rect = title_surf_scaled.get_rect(center = (400,200))

# start button
start_button_surf = font.render("Press enter To Start",False,(0,0,0))
start_button_surf_scaled = pygame.transform.scale(start_button_surf, (start_button_surf.get_width() * 3.5, start_button_surf.get_height() * 3.5)).convert_alpha()
start_button_rect = start_button_surf_scaled.get_rect(midbottom = (400,screen_hgt-30))

# Game
while True:

    # Check for user's inputs
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        
        
        if game_active:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.sprite.walking_right = False
                elif event.key == pygame.K_a:
                    player.sprite.walking_left = False
            
            if event.type == enemy_timer:
                enemy_group.add(Enemy())
      
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_active = True
        
    if game_active:
        
        sky.draw(screen)
        ground.draw(screen)

        # player character
        player.draw(screen)
        player.update()

        # enemy character
        enemy_group.draw(screen)
        enemy_group.update()
        
        kills += player_kill()
        score(kills)
        game_active = not game_over()
    
    if not game_active:
        
        screen.fill((94,129,162))
        screen.blit(start_button_surf_scaled,start_button_rect)
        player.sprite.reset()
        if kills == 0:
            screen.blit(title_surf_scaled,title_rect)
        else:
            score_surf = font.render(f"Points: {kills}",False,(0,0,0))
            score_surf_scaled = pygame.transform.scale(score_surf, (score_surf.get_width()*5, score_surf.get_height()*5))
            score_rect = score_surf_scaled.get_rect(center  = (screen_wdt//2,screen_hgt//2))
            screen.blit(score_surf_scaled,score_rect)
        
        
    pygame.display.update()
    # 60 frames every iteration 
    clock.tick(60)

   