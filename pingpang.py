import pygame,sys,math
from pygame.locals import*
pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1246,520),0,32)
background=pygame.image.load("./pingpang_table.jpg")
pygame.display.set_caption('pingpang game')
img = pygame.image.load('./pingpang.gif')
imgx = 100
imgy = 350
speed = 10
direction = "right"
while True:
    screen.blit(background,(0,0))
    if direction == 'right':
        imgx += speed
        if imgx >= 1100 and imgy >= 350:
            direction = 'up_left'
        elif imgx >= 1100 and imgy < 350:
            direction = 'down_left'

    elif direction == 'up_left':
        angle = 165
        angle_rad = math.radians(angle)
        speedx = abs(math.cos(angle_rad) * speed)
        speedy = abs(math.sin(angle_rad) * speed)
        imgy -= speedy
        imgx -= speedx
        if imgx <= 100:
            direction = 'right'
    elif direction == 'down_left':
        angle = 195
        angle_rad = math.radians(angle)
        speedx = abs(math.cos(angle_rad) * speed)
        speedy = abs(math.sin(angle_rad) * speed)
        imgx -= speedx
        imgy += speedy
        if imgx <= 100:
            direction = 'right'

    screen.blit(img,(imgx,imgy))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)


