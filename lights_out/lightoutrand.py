# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:25:06 2019

@author: trent
"""
import random

import pygame as pg

import board as b
import move as m
from lights_out.constants import BOARD_SHAPE
from lights_out.square import Square

bd = b.Board(BOARD_SHAPE)



################################################################
pg.init()
FPS = 1000
width = 1200
height = 600
spacing = 5
boarder = 20
if width/BOARD_SHAPE[0] > height/BOARD_SHAPE[1]:
    bound = height
    d = 1
else:
    bound = width
    d = 0

sq_size = (bound-spacing*BOARD_SHAPE[d]-2*boarder)/BOARD_SHAPE[d]
print(sq_size)
screen = pg.display.set_mode((width,height))
pg.display.set_caption('Lights Out')
clock = pg.time.Clock()
white = (10,100,250)
backg = (5,5,5)
    

##############################################################
x =  (width * 0.5-37)
y = (height * 0.5-37)
crashed = False

sprites = []
squares = pg.sprite.Group()
for r in range(BOARD_SHAPE[1]):
        for c in range(BOARD_SHAPE[0]):
            temp_square = Square(bd,(c,r),((BOARD_SHAPE[0]/2)-.5,(BOARD_SHAPE[1]/2)-.5),(width,height),spacing,sq_size)
            squares.add(temp_square)
            sprites.append(temp_square)
                   
timer = 0
choosing = True
zeros = True
moves = 0
def check_zeros():
    for r in range(BOARD_SHAPE[1]):
        for c in range(BOARD_SHAPE[0]):
            if bd.board[r][c] == 1:
                return False
    return True

for i in range(15):
    choice = random.randint(0,len(sprites)-1)
    bd.choose(sprites[choice])
while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True
    
    zeros = check_zeros()
    if not zeros:
        bd.choose(sprites[random.randint(0,len(sprites)-1)])
        moves += 1
    else:
        print(moves)
    if moves % 2000 == 0:
        print(moves)
    

    screen.fill(backg)
    squares.draw(screen)
    squares.update()
     
    pg.display.flip()
    
    timer += FPS
    clock.tick(FPS)
    
pg.quit()
quit()




