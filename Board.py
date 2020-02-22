# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:04:08 2020
0 beyaz
1 siyah
@author: ozan
"""


class Board:
    def __init__(self):

        self.matrix =  [[0 for _ in range(8)] for _ in range(8)]
        
        
    def Engine():
        pass
    
    def Valid(self,piece , x , y):
        new_x = piece.x + x
        new_y = piece.y + y
        
        if new_x < 8 and new_y < 8 and new_x >= 0 and new_y >=0:
            #out of bounds
            if self.matrix[new_x][new_y] == 0 or self.matrix[new_x][new_y].player != piece.player:
                self.matrix[new_x][new_y] = piece
                self.matrix[piece.x][piece.y] = 0
                print("not empty")
                return new_x,new_y
                    
        print("Invalid Move")
        return piece.x,piece.y
    
    def visual(self):
        for x in self.matrix:
            print(*x, sep = " ")
            
    
    
''' '''









