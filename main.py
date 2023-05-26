import pygame, random
from pygame import mixer
run = True
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1150,700))
pygame.display.set_caption('Alien Game')
#music
# lvl_2='music/04 Pallet Town.mp3'
# lvl_3='music/09 A Rival Appears.mp3'
# pygame.mixer.init()
# s_effect = mixer.Sound(lvl_1)
# s_effect.set_volume(0.2)
pygame.mixer.init(frequency=22450, size=32, channels=2, buffer=4096)
hit = mixer.Sound('music/hit-sound.mp3')
game_over = mixer.Sound('music/game-over.mp3')
bg_music = mixer.Sound('music/game music.mp3')
bg_music.play()
#states
state = 'playing'
#bullets
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, width, height, screen, color, border):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height))
        self.surface_rect = self.surface.get_rect(center=(self.x_pos, self.y_pos))
        self.screen = screen
        self.color = color
        self.border = border
        self.health = 4
        self.hearts = pygame.image.load('pics/heart_nobg.png').convert_alpha()
        self.hearts = pygame.transform.scale(self.hearts, (300, 300))
        self.hit_anim =['gray','white','gray']
    def display(self):
        self.surface.fill('white')
        screen.blit(self.surface, self.surface_rect)
    def move(self):
        self.surface_rect.x +=15
        if self.surface_rect.x >= 1200:
            self.surface_rect.x = 0
            self.surface_rect.y = random.randrange(0,500)
    def bullet_rect(self):
        return self.surface_rect
    def collision(self):
        global state
        if self.surface_rect.colliderect(p.rectangle()):
            self.surface_rect.x = -100
            self.surface_rect.y = random.randrange(0,500)
            self.health-=1
            hit.play()
        if self.health == 0:
            game_over.play()
            state = 'gameover'

    def heart_display(self):
        for i in range(self.health):
            screen.blit(self.hearts,(i*50+100,20))
b = Bullets(100,100,100,20,screen,'yellow',10)
#-----------------------------------------------------
#player-----------------------------------------------
class Player():
    def __init__(self,x_pos,y_pos,width,height,screen,color,border):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.screen = screen
        self.color = color
        self.border = border
        self.speed = 2
    def display (self):
        self.image.fill('white')
        screen.blit(self.image,self.rect)
    def move (self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x +=self.speed
        if keys[pygame.K_a]:
            self.rect.x -=self.speed
        if keys[pygame.K_w]:
            self.rect.y -=self.speed
        if keys[pygame.K_s]:
            self.rect.y +=self.speed
    def rectangle(self):
        return self.rect
p = Player(600, 170, 50, 50, screen, 'white', 20)
p.rectangle()
#-------------------------------------------------------
#game over screen
class game_over_screen():
    def __init__(self, screen):
        self.screen = screen
        self.f_settings = pygame.font.SysFont('Cascada Mono',50)
        #menu
        self.f = self.f_settings.render('Game over.',False,'white')
    def display(self):
        global test
        screen.blit(self.f,(450,300))
g_o = game_over_screen(screen)
#------------------------------------------
while run:
    screen.fill('black')
    if state == 'playing':
        #displays------
        #player------
        p.display()
        p.move()
        #bullet
        b.display()
        b.move()
        b.collision()
        b.heart_display()
    elif state =='gameover':
        g_o.display()
        keys = pygame.key.get_pressed()
        if keys[pygame.KEYDOWN]:
            print('yeah')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(110)
    pygame.display.update()
pygame.quit()

