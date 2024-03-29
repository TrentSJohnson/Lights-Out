# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:31:21 2019

@author: trent
"""
from lights_out.constants import BOARD_SHAPE


class Move:

    def __init__(self, a):
        self.mapping = a
        self.corner = [self.mapping[0] - 1, self.mapping[1] - 1]
        # print(self.corner)
        self.layout = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        if self.mapping[1] == 0:
            self.layout.pop(0)
            self.corner = [self.corner[0], self.corner[1] + 1]
        if self.mapping[1] == BOARD_SHAPE[1] - 1:
            self.layout.pop(2)

        if self.mapping[0] == 0:
            self.corner = [self.corner[0] + 1, self.corner[1]]
            for i in range(len(self.layout)):
                self.layout[i].pop(0)
        if self.mapping[0] == BOARD_SHAPE[0] - 1:
            for i in range(len(self.layout)):
                self.layout[i].pop(2)
        self.corner = (self.corner[0], self.corner[1])
