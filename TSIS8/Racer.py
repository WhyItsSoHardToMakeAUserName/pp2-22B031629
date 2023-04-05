import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((500,1000),pygame.RESIZABLE)

check = True


color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red

FPS = pygame.time.Clock()
FPS.tick(60)
class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("IMAGES/redcar.png"),(100,100))
        self.rect = self.image.get_rect(width = 45,height = 90)
        self.rect.center = (250,700)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect) 
    
    def move_left(self):
        if (self.rect.right <500):

            self.rect.move_ip(1,0)
    def move_right(self):
        if (self.rect.left > 0):
            
            self.rect.move_ip(-1,0)
    
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate((pygame.transform.scale(pygame.image.load("IMAGES/redcar.png"),(100,100))),180)
        self.rect = self.image.get_rect(width = 45,height = 90)
        self.rect.center = (random.randint(0,500),0)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect) 
        
    
    def move(self):
        self.rect.move_ip(0,1)
        if (self.rect.bottom > 1000):
            self.rect.top = 0
            self.rect.center = (random.randint(50, 450), 0)


object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))

Enemy = enemy()
Player = player()

enemies = pygame.sprite.Group()
enemies.add(Enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add(Player)
all_sprites.add(Enemy)

while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                check = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        Player.move_left()
    if keys[pygame.K_a]:
        Player.move_right()
    screen.fill((0,0,0))
    Enemy.move()
    Player.draw(screen)
    Enemy.draw(screen)

    if pygame.sprite.spritecollideany(Player, enemies):
          screen.fill((100,0,0))
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
    
    pygame.display.flip()
    