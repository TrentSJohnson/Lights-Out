# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:27:05 2019

@author: trent
"""
import move as m

class Board:
    def __init__(self,size):
        self.board = []
        self.size = size
        #print(self.size)
        for i in range(size[1]):
            self.board.append([])
            for s in range(size[0]):
                self.board[i].append(0)
        #print(self.board)
    def add(self,selection1):
        selection = m.Move(selection1.locat)
        x = selection.corner[0]
        y = selection.corner[1]
        #print("corner =" , selection.corner)
        for r in range(len(selection.layout)):
            for c in range(len(selection.layout[r])):
                self.board[r+y][c+x] = (self.board[r+y][c+x] + selection.layout[r][c])%2
    
    def print_board(self):
        for r in range(self.size[1]):
            print(self.board[r])
           
            
    def choose(self,s):
        self.add(s)
        #self.print_board()
        
        
        