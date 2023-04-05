import pygame
import time
import random
import sys
check = True
WINDOW_WIDTH = 546
WINDOW_HEIGHT = 546
GRID_SIZE = 26
GRID_SPACING = 52
SCORE = 0
SNAKE_SPEED = 6
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

pygame.font.init()
def gameover():
    time.sleep(2)
    global check
    screen.fill((255,0,0))

def draw_grid(width,height,gridsize,gridspacing):
    
    for i in range(gridspacing, width - gridspacing+1, gridsize):
        pygame.draw.line(screen, (255, 255, 255), (i , gridspacing), (i, height - gridspacing))
    for j in range(gridspacing, height - gridspacing+1, gridsize):
        pygame.draw.line(screen, (255, 255, 255), (gridspacing , j), (width - gridspacing , j))

class food(pygame.sprite.Sprite):
    def __init__(self,snake,fruits):
        global WINDOW_HEIGHT,WINDOW_WIDTH,GRID_SIZE,GRID_SPACING
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((25,25))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()
        fruits.add(self)
        self.rect.topleft = ((random.randrange(GRID_SPACING,WINDOW_WIDTH - GRID_SPACING,GRID_SPACING),random.randrange(GRID_SPACING,WINDOW_HEIGHT - GRID_SPACING,GRID_SPACING)))
        while pygame.sprite.spritecollideany(self, snake.body_group):
            self.rect.topleft = ((random.randrange(GRID_SPACING,WINDOW_WIDTH - GRID_SPACING,GRID_SPACING),random.randrange(GRID_SPACING,WINDOW_HEIGHT - GRID_SPACING,GRID_SPACING)))

    def draw(self):
         screen.blit(self.surf,self.rect)


class body_block(pygame.sprite.Sprite):
    def __init__(self,snake_head):
        pygame.sprite.Sprite.__init__(self)
        self.direction = snake_head.body_group.sprites()[-1].direction
        
        
        self.surf = pygame.Surface((25,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        self.rect.center = snake_head.body_group.sprites()[-1].rect.center

        if self.direction == "right":
            self.rect.move_ip(-26,0)
        if self.direction == "left":
            self.rect.move_ip(26,0)
        if self.direction == "up":
            self.rect.move_ip(0,26)
        if self.direction == "down":
            self.rect.move_ip(0,-26) 

        snake_head.body_group.add(self)
        self.index = snake_head.body_group.sprites().index(self)

    def change_direction(self,snake_head):
        self.direction = snake_head.body_group.sprites()[self.index-1].direction
        
    def draw(self):
         screen.blit(self.surf,self.rect)


class snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((25,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        self.rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)
        self.direction = "right"
        self.body_group = pygame.sprite.Group()
        self.body_group.add(self)

        body = body_block(self)
        body1 = body_block(self)

        self.bodies_list = [body,body1]

    def move(self):
        for piece in self.body_group:
            if piece.direction == "right":
                piece.rect.move_ip(26,0)
            if piece.direction == "left":
                piece.rect.move_ip(-26,0)
            if piece.direction == "up":
                piece.rect.move_ip(0,-26)
            if piece.direction == "down":
                piece.rect.move_ip(0,26)
        
    def draw(self):
         screen.blit(self.surf,self.rect)

Snake = snake()

fruits = pygame.sprite.Group()

last_key_time = pygame.time.get_ticks()

while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
        if event.type == pygame.KEYDOWN:
            if pygame.time.get_ticks() - last_key_time > 10:
                if event.key == pygame.K_SPACE:
                    check = False
                if event.key == pygame.K_w:
                    if Snake.direction != "down":
                        Snake.direction = "up"
                if event.key == pygame.K_a:
                    if Snake.direction != "right":
                        Snake.direction = "left"
                if event.key == pygame.K_s:
                    if Snake.direction != "up":
                        Snake.direction = "down"
                if event.key == pygame.K_d:
                    if Snake.direction != "left":
                        Snake.direction = "right"
                last_key_time = pygame.time.get_ticks()
    # spawn food if there isnt in the area
    if len(fruits) == 0:
        fruit = food(Snake,fruits)
        fruits.add(fruit)

    Snake.move()
    for body in reversed(Snake.bodies_list):
        body.change_direction(Snake)
    
    # check collison with the walls
    if Snake.rect.x < GRID_SPACING or Snake.rect.x >= WINDOW_WIDTH - GRID_SPACING or Snake.rect.y < GRID_SPACING or Snake.rect.y >= WINDOW_HEIGHT - GRID_SPACING:
        gameover()
        pass
    else:
        
        screen.fill((0,0,0))
        font_small = pygame.font.SysFont("Arial", 20)
        scores = font_small.render("Score:"+str(SCORE), True, (255,255,255))
        level = font_small.render("Level:"+str(SCORE//4),True,(255,255,255))
        screen.blit(scores, (450, 15))
        screen.blit(level,(250,15))

        Snake.draw()
        fruit.draw()
        draw_grid(WINDOW_WIDTH,WINDOW_HEIGHT,GRID_SIZE,GRID_SPACING)
        for body in Snake.bodies_list:
            body.draw()
        
        # check collison with food and snakes body
        if pygame.sprite.spritecollideany(Snake, fruits):
            body_l = body_block(Snake)
            Snake.bodies_list.append(body_l)
            for entity in fruits:
                    entity.kill() 
            SCORE+=1
        if pygame.sprite.spritecollideany(Snake,Snake.bodies_list):
            gameover()
    clock.tick(SNAKE_SPEED+SCORE//4)
    pygame.display.update()