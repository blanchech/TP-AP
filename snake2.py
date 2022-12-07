import sys
import pygame
import random as rd

white = [255, 255, 255]
black = [0, 0, 0]
red=[255, 0, 0]
snake = [[10, 15],[11, 15],[12, 15]]
direction = [1.0,0.0]
fruit=[rd.randint(0, 29)*20, rd.randint(0, 29)*20, 20, 20]


pygame.init()
screen = pygame.display.set_mode([20*30, 20*30])
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP and direction != [0.0, 1.0]:
                direction = [0.0, -1.0]
            elif event.key == pygame.K_LEFT and direction != [1.0, 0.0]:
                direction = [-1.0, 0.0]
            elif event.key == pygame.K_DOWN and direction != [0.0, -1.0]:
                direction = [0.0, 1.0]
            elif event.key == pygame.K_RIGHT and direction != [-1.0, 0.0]:
                direction = [1.0, 0.0]
    head = snake[-1]
    new_head = [head[0] + direction[0],head[1] + direction[1]]
    del snake[0]
    tail = snake[0]
    new_tail = [tail[0] + direction[0], tail[1] + direction[1]]
    snake.append(new_head)
    screen.fill(white)
    if snake[-1] == [fruit[0]//20, fruit[1]//20]: 
        fruit=[rd.randint(0, 29)*20, rd.randint(0, 29)*20, 20, 20]
        snake.insert(0, new_tail)
    if snake[-1][0]<0:
        pygame.quit()
        sys.exit()
    elif snake[-1][0]>30:
        pygame.quit()
        sys.exit()
    elif snake[-1][1]<0:
        pygame.quit()
        sys.exit()
    elif snake[-1][1]>30:
        pygame.quit()
        sys.exit()

    for x, y in snake:
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, black, rect)
        pygame.draw.rect(screen, red, fruit)
    pygame.display.update()
    clock.tick(5)
    
        