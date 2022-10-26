from curses import KEY_RIGHT
import random
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

def is_white(i,j):
    if i%2==0 and j%2==0:
        return(True)
    elif i%2==1 and j%2==1:
        return(True)
    else:
        return(False)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    for x in range (600):
        for y in range (600):
            i=x//30
            j=y//30
            if is_white(i,j):
                screen[i:i+30][j:j+30]=(255,255,255)

    pygame.draw.rect(screen, color, rect)
    pygame.display.update()






