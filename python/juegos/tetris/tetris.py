"""
A Tetris code 
"""
import pygame
from copy import deepcopy
from random import choice, randrange

W, H = 10,20
TILE = 30
GAME_RES= W*TILE, H*TILE
FPS=60
RES = 500, 800


pygame.init()
sc= pygame.display.set_mode(RES)
game_sc = pygame.Surface(GAME_RES)
clock = pygame.time.Clock()

grid= [pygame.Rect(x*TILE, y*TILE, TILE, TILE) for x in range(W) for y in range (H)]

figure_pos =[[(-1,0), (-2,0), (0,0), (1,0)],
             [(0,-1), (-1,-1), (-1,0), (0,0)],
             [(-1,0), (-1,1), (0,0), (0,-1)],
             [(0,0), (-1,0), (0,1), (-1,-1)],
             [(0,0), (0,-1), (0,1,), (-1,-1)],
             [(0,0), (0,-1), (0,1,), (1,-1)],             
             [(0,0), (0,-1), (0,1,), (-1,0)]
]
figures=[[pygame.Rect(x+W//2, y+1,1,1)for x,y in fig_pos] for fig_pos in figure_pos]
figure_rect = pygame.Rect(0,0,TILE-2,TILE-2)
field = [[0 for i in range(W)] for j in range(H)]

anim_count, anim_speed, anim_limit= 0,60,2000


bg = pygame.image.load('img/bg4.jpg').convert()
game_bg = pygame.image.load('img/bg5.jpg').convert()

main_font = pygame.font.Font('font/tetris.ttf', 45)
font = pygame.font.Font('font/tetris.ttf', 25)

title_tetris = main_font.render('TETRIS', True, pygame.Color('darkorange'))
title_score = main_font.render('score:', True, pygame.Color('blue'))
title_record = main_font.render('record:', True, pygame.Color('purple'))

get_color = lambda:(randrange(30,256), randrange(30,256), randrange(30,256))
figure, next_figure =deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()

score, lines =0,0
scores = {0:0 , 1:100, 2:300, 3:700, 4:1500}

def check_borders():
    if figure[i].x < 0 or figure[i].x > W-1:
        return False
    elif figure[i].y > H -1 or field[figure[i].y][figure[i].x]:
        return False
    return True

def get_record():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')

def set_record(record, score):
    rec = max(int(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))
    
while True:
    record= get_record()
    dx, rotate = 0, False
    sc.blit(bg,(0,0))
    sc.blit(game_sc, (20,20))
    game_sc.blit(game_bg, (0,0))
    
    #delay for full lines
    for __ in range(lines):
        pygame.time.wait(200)
    #control
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                dx=-1
            elif event.key ==pygame.K_RIGHT:
                dx=1
            elif event.key ==pygame.K_DOWN:
                anim_limit=60
            elif event.key ==pygame.K_UP:                
                rotate = True                         
    
    #move X
    figure_old= deepcopy(figure)
    for i in range (4):
        figure[i].x+=dx
        if not check_borders():
            figure= deepcopy(figure_old)
            break
    #move Y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count=0
        figure_old=deepcopy(figure)
        for i in range(4):
            figure[i].y+=1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = color
                figure, color = next_figure, next_color
                next_figure, next_color= deepcopy(choice(figures)), get_color()
                anim_limit= 2000
                break
    #rotate
    center = figure[0]
    figure_old= deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y- center.y
            y = figure[i].x- center.x
            figure[i].x = center.x - x
            figure[i].y = center.y - y
            if not check_borders():
                figure= deepcopy(figure_old)
                break
    #check lines
    line, lines = H-1, 0
    for row in range(H-1 , -1, -1 ):
        count=0
        for i in range(W):          
            if field[row][i]:
                count+=1
            field[line][i]= field[row][i]
        if count <W:
            line -=1
        else:
            anim_speed+= 3
            lines +=1
    #computer score
    score+= scores[lines]
    
                           
    # draw grid       
    [pygame.draw.rect(game_sc,(40,40,40), i_rect,1) for i_rect in grid]
    
    
    # draw figure
    for i in range(4):
        figure_rect.x= figure[i].x*TILE
        figure_rect.y= figure[i].y*TILE
        pygame.draw.rect(game_sc, color, figure_rect)
    
    # draw field        
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x*TILE, y*TILE
                pygame.draw.rect(game_sc, col, figure_rect)
    
    #draw next figure
    for i in range(4):
        figure_rect.x= next_figure[i].x*TILE+255
        figure_rect.y= next_figure[i].y*TILE+100
        pygame.draw.rect(sc, next_color, figure_rect)
    
    #game over
    for i in range(W):
        if field[0][i]:
            set_record(record, score)
            field = [[0 for i in range(W)] for i in range(H)]
            anim_count, anim_speed, anim_limit = 0, 60, 2000
            score=0
            for i_rect in grid:
                pygame.draw.rect(game_sc, get_color(), i_rect)
                sc.blit(game_sc, (20,20))
                pygame.display.flip()
                clock.tick(200)
    
    #draw titles
    sc.blit(title_tetris, (300,20))
    sc.blit(title_score, (340, 290))
    sc.blit(font.render(str(score), True, pygame.Color('white')), (370,340))
    sc.blit(title_record, (320, 450))
    sc.blit(font.render(record, True, pygame.Color('gold')), (370,500))
    pygame.display.flip()
    clock.tick()