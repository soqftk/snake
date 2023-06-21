import pygame
from pygame.locals import *
from sys import exit
from random import randint
import os 
# import pickle


pygame.init()

# Varibles
DISPLAY_SIZE = (1080, 720)
SCORE = 0
GAME_OVER = False
poem = (SCORE)



# t_score = 'scores.txt'

# my_score = SCORE


# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock() 
font = pygame.font.SysFont(None, 32)

SPEED = 20
DIRECTION = [SPEED, 0]

def score():
    global SCORE, WHITE
    text = font.render(f'SCORE: {SCORE}', True, WHITE)
    text_rect = text.get_rect(center=(65, 15))
    screen.blit(text, text_rect)

def pickup():
    global apple_rect, head_rect, SCORE, snake

    if head_rect.colliderect(apple_rect):
        apple_rect.x = randint(50, DISPLAY_SIZE[0] - 70)
        apple_rect.y = randint(15, DISPLAY_SIZE[1] - 15)
        snake.append(snake[1].copy())
        SCORE += 10

def load_img(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (20, 20))
    rect = image.get_rect(center=(x,y))
    transparent = image.get_at((0,0))
    image.set_colorkey(transparent)
    return image, rect

def move(obj, snake):
    global DIRECTION, SPEED, WHITE, KEYS

    if  (KEYS[K_UP] or KEYS[K_w]) and DIRECTION[1] == 0:
        DIRECTION = [0, -SPEED]
    elif (KEYS[K_DOWN] or KEYS[K_s]) and DIRECTION[1] == 0:
        DIRECTION = [0, SPEED]
    elif (KEYS[K_RIGHT] or KEYS[K_d]) and DIRECTION[0] == 0:
        DIRECTION = [SPEED, 0]
    elif (KEYS[K_LEFT] or KEYS[K_a]) and DIRECTION[0] == 0:
        DIRECTION = [-SPEED, 0]

    if obj.bottom > DISPLAY_SIZE[1]:
        obj.top = 1
    elif obj.top < 0:
        obj.bottom = DISPLAY_SIZE[1] - 1
    elif obj.right > DISPLAY_SIZE[0]:
        obj.left = 1
    elif obj.left < 0:
        obj.right = DISPLAY_SIZE[0] - 1

    for i in range(len(snake)-1, 0, -1):
        snake[i].x = snake[i-1].x
        snake[i].y = snake[i-1].y

    obj.move_ip(DIRECTION)

# while True:
#     line = f.readline()
#     if len(line) == 0:
#         break
#     print(line, end='')        

# f = open(t_score, 'wb')
# pickle.dump(my_score, f)

# del my_score

# f = open(t_score, 'rb')
# storedscore = pickle.load(f)
# print(storedscore)

def game_over():
    global snake, head_rect, GAME_OVER
    for el in snake[1:]:
        if head_rect.colliderect(el):
            GAME_OVER = True

            with open('scores.txt', 'a') as f:
                f.write(f"\n{str(SCORE)}")                 


head_image, head_rect = load_img('./img/head.png', 400, 300)
body_image, body_react = load_img('./img/body.png', 380, 300)
apple_image, apple_rect = load_img('./img/apple.png', 200, 200)

snake = [head_rect, body_react]


while not(GAME_OVER):
    screen.fill(BLACK)

    for events in pygame.event.get():
        if events.type == QUIT:
            pygame.quit()
            exit()

    KEYS = pygame.key.get_pressed()
    screen.blit(apple_image, apple_rect)
    
    screen.blit(head_image, head_rect)
    for body in snake[1:]:
        screen.blit(body_image, body)

    move(head_rect, snake)
    game_over()
    pickup()
    score()
    pygame.display.update()
    clock.tick(20)


    # os.close(dir_fd)
else:
    # dir_fd = os.open('/some/dir', os.O_RDONLY)
# def opener(path, flags):
#     return os.open(path, flags, dir_fd=dir_fd)
    # scores = list()
    # try:
    #     with open('README.txt', 'w', opener=opener) as file:
    #        print('This will be written to /some/dir/test.txt', file=file) 
    # while True:
    #     line = f.readline()
    #     if len(line) == 0:
    #         break
    #     print(line, end='')        


    # scores = list()
    # try:
    # #     with open("score.csv", mode="r") as file:
    #        reader = csv.DictReader(file)
    #        scores = [ResourceWarning for now in reader]
    # except FileNotFoundError:
    #     print("SCORE: 0")
    
    # max_score = max(scores)
    # scores.append(SCORE)
   

    while True: 
        screen.fill(BLACK)
        text = font.render(f'Your score is: {SCORE}', True, WHITE)
        text_rect = text.get_rect(center=(560, 480))
        screen.blit(text, text_rect)
      

        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                exit()

        
        pygame.display.update()
        clock.tick(20)