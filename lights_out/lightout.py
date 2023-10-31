# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:25:06 2019

@author: trent
"""

import random

import pygame as pg

from lights_out.board import Board
from lights_out.constants import (
    FPS,
    WIDTH,
    HEIGHT,
    SPACING,
    BOARD_SHAPE,
    SQUARE_SIZE,
    BACKGROUND,
)
from lights_out.square import Square



################################################################
pg.init()
pg.display.set_caption('Lights Out')
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
bd = Board(BOARD_SHAPE)




##############################################################
x = (WIDTH * 0.5 - 37)
y = (HEIGHT * 0.5 - 37)
crashed = False

sprites = []
squares = pg.sprite.Group()
for r in range(BOARD_SHAPE[1]):
    for c in range(BOARD_SHAPE[0]):
        temp_square = Square(bd, (c, r), ((BOARD_SHAPE[0] / 2) - .5, (BOARD_SHAPE[1] / 2) - .5), (WIDTH, HEIGHT), SPACING,
                             SQUARE_SIZE)
        squares.add(temp_square)
        sprites.append(temp_square)

timer = 0
choosing = True
zeros = True
moves = 0
timer = 0

for i in range(15):
    choice = random.randint(0, len(sprites) - 1)
    # print(sprites[choice].locat)
    bd.choose(sprites[choice])

while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True
        print(event)

        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            timer = 0

            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            if len(clicked_sprites) > 0:
                bd.choose(clicked_sprites[0])
                bd.print_board()

    screen.fill(BACKGROUND)
    squares.draw(screen)
    squares.update()

    pg.display.flip()

    timer += FPS
    clock.tick(FPS)
pg.quit()
quit()
