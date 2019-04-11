# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:25:06 2019

@author: trent
"""

import pygame as pg
import board as b
import move as m
import random


board_size = (5,5)
m.Move.board_size = board_size
bd = b.Board(board_size)


################################################################
pg.init()
FPS = 1000
width = 1200
height = 600
spacing = 5
boarder = 20
if width/board_size[0] > height/board_size[1]:
    bound = height
    d = 1
else:
    bound = width
    d = 0

sq_size = (bound-spacing*board_size[d]-2*boarder)/board_size[d]
print(sq_size)
screen = pg.display.set_mode((width,height))
pg.display.set_caption('Lights Out')
clock = pg.time.Clock()
white = (10,100,250)
backg = (5,5,5)

###############################################################

class Square(pg.sprite.Sprite):
    dim = (192,192,192)
    lit = (255,250,205)
    board = b.Board((5,5))
    def __init__(self,board,locat,center,screeen,spacing,size):
        pg.sprite.Sprite.__init__(self)
        self.board = board
        self.locat = locat
        self.image = pg.Surface((size,size))
        self.image.fill(white)
        self.posx = (spacing+size) * (center[0]-locat[0])+screeen[0]/2
        self.posy = (spacing+size) * (center[1]-locat[1])+screeen[1]/2
        self.rect = self.image.get_rect()
        self.rect.center = (self.posx,self.posy)
        pg.draw.rect(self.image, white, [0, 0, size, size])
    def update(self):
        on = self.board.board[self.locat[1]][self.locat[0]]
        
        if on:
            self.image.fill(self.lit)
        else:
            self.image.fill(self.dim)
        
             
    

##############################################################
x =  (width * 0.5-37)
y = (height * 0.5-37)
crashed = False

sprites = []
squares = pg.sprite.Group()
for r in range(board_size[1]):
        for c in range(board_size[0]):
            temp_square = Square(bd,(c,r),((board_size[0]/2)-.5,(board_size[1]/2)-.5),(width,height),spacing,sq_size)
            squares.add(temp_square)
            sprites.append(temp_square)
                   
timer = 0
choosing = True
zeros = True
moves = 0        
timer = 0

for i in range(15):
    choice = random.randint(0,len(sprites)-1)
    #print(sprites[choice].locat)
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
            else:
                print("fjadslfajsdl/n/n\/n\nfk")


    screen.fill(backg)
    squares.draw(screen)
    squares.update()
     
    pg.display.flip()
    
    timer += FPS
    clock.tick(FPS)
pg.quit()
quit()




