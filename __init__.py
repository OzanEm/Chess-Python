# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:52:45 2020
sudoku yap
@author: ozan
"""


from Board import Board
from Piece import Piece,Pawn,Rook,Knight,Bishop,Queen,King
import chessAI
#
board = Board()
#
board.matrix[0][0] = Rook(0, 0, 0)
board.matrix[0][1] = Knight(0, 0, 1)
board.matrix[0][2] = Bishop(0, 0, 2)
board.matrix[0][3] = Queen(0, 0, 3)
board.matrix[0][4] = King(0, 0, 4)
board.matrix[0][5] = Bishop(0, 0, 5)
board.matrix[0][6] = Knight(0, 0, 6)
board.matrix[0][7] = Rook(0, 0, 7)
#
board.matrix[1][0] = Pawn(0, 1, 0)
board.matrix[1][1] = Pawn(0, 1, 1)
board.matrix[1][2] = Pawn(0, 1, 2)
board.matrix[1][3] = Pawn(0, 1, 3)
board.matrix[1][4] = Pawn(0, 1, 4)
board.matrix[1][5] = Pawn(0, 1, 5)
board.matrix[1][6] = Pawn(0, 1, 6)
board.matrix[1][7] = Pawn(0, 1, 7)
#
board.matrix[7][0] = Rook(1, 0, 0)
board.matrix[7][1] = Knight(1, 0, 1)
board.matrix[7][2] = Bishop(1, 0, 2)
board.matrix[7][3] = Queen(1, 0, 3)
board.matrix[7][4] = King(1, 0, 4)
board.matrix[7][5] = Bishop(1, 0, 5)
board.matrix[7][6] = Knight(1, 0, 6)
board.matrix[7][7] = Rook(1, 0, 7)
#
board.matrix[6][0] = Pawn(1, 1, 0)
board.matrix[6][1] = Pawn(1, 1, 1)
board.matrix[6][2] = Pawn(1, 1, 2)
board.matrix[6][3] = Pawn(1, 1, 3)
board.matrix[6][4] = Pawn(1, 1, 4)
board.matrix[6][5] = Pawn(1, 1, 5)
board.matrix[6][6] = Pawn(1, 1, 6)
board.matrix[6][7] = Pawn(1, 1, 7)

board.visual()

def main():
    

    Terminal()
 
    
def Terminal():
    
    while True:
        User_Input = input("Please enter your move:")
        
        if User_Input == "m":
            x= int(input("enter:"))
            y = int(input("enter:"))
            
            Selected = board.matrix[x][y]
            
            new_x = int(input("move x:"))
            new_y = int(input("move y:"))
            Selected.Validation(board,new_x,new_y)
            board.visual()
        
        if User_Input == "exit":
            break
    
        
    

if __name__ == "__main__":
    main()
    
    

    






