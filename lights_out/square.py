# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 18:26:59 2019

@author: trent
"""
import pygame as pg

from lights_out import board as b
from lights_out.constants import WHITE


class Square(pg.sprite.Sprite):
    dim = (192, 192, 192)
    lit = (255, 250, 205)
    board = b.Board((5, 5))

    def __init__(self, board, locat, center, screeen, spacing, size):
        pg.sprite.Sprite.__init__(self)
        self.board = board
        self.location = locat
        self.image = pg.Surface((size, size))
        self.image.fill(WHITE)
        self.posx = (spacing + size) * (center[0] - locat[0]) + screeen[0] / 2
        self.posy = (spacing + size) * (center[1] - locat[1]) + screeen[1] / 2
        self.rect = self.image.get_rect()
        self.rect.center = (self.posx, self.posy)
        pg.draw.rect(self.image, WHITE, [0, 0, size, size])

    def update(self):
        on = self.board.board[self.location[1]][self.location[0]]

        if on:
            self.image.fill(self.lit)
        else:
            self.image.fill(self.dim)
