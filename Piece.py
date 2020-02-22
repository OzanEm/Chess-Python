# -*- coding: utf-8 -*-
"""

"""

class Piece:
    def __init__(self, player, x , y):
        self.player = player
        self.x = x
        self.y = y
    
    def move(self, board,mov_x,mov_y):
        self.x,self.y = board.Valid(self , mov_x , mov_y)#plus x
    
    def __str__(self):
        return self.__class__.__name__+"-"+str(self.player) 
    
    def MoveThrough(self,board,mov_x,mov_y):
        path_x = mov_x - self.x
        path_y = mov_y - self.y
        
        if mov_x == 0 :
            for i in range(self.y,mov_y):
                if board.matrix[self.x][i] != 0:
                    return False
        
        if mov_y == 0 :
            for i in range(self.x,mov_x):
                if board.matrix[i][self.y] != 0:
                    return False            
                
        if abs(mov_x) == abs(mov_y):
            for i in range(abs(mov_x)):
                if board.matrix[i][i]:
                    pass
        
        

class Pawn(Piece):

   def Validation(self, board,mov_x,mov_y):
        
        if mov_y != 0:
            print("invalid")
            return
        if self.player == 0:
            if mov_x == 1:
                self.move( board,mov_x,mov_y)
                print("valid")
            if mov_x == 2 and self.x == 1:
                self.move( board,mov_x,mov_y)
                
        if self.player == 1:
            if mov_x == -1:
                 self.move(board,mov_x,mov_y)
                 print("valid")
            if mov_x == -2 and self.x == 6:
                self.move( board,mov_x,mov_y)
               
       
        
   
class Rook(Piece):
    
   def Validation(self, board,mov_x,mov_y):
       if mov_y == 0 and mov_x != 0:
           self.move( board,mov_x,mov_y)
       if mov_x == 0 and mov_y != 0:
           self.move( board,mov_x,mov_y)
           
        
class Knight(Piece):
    
   def Validation(self, board,mov_x,mov_y):
       if (mov_y == -3 or mov_y == 3 or mov_y == 1 or mov_y == -1) and \
       (mov_x == -3 or mov_x == 3 or mov_x == 1 or mov_x == -1) and \
           (abs(mov_x) != abs(mov_y)):
               self.move( board,mov_x,mov_y)
        
        
    
    
        
class Bishop(Piece):
    
   def Validation(self, board,mov_x,mov_y):
       if mov_x == mov_y and mov_x != 0:
           self.move( board,mov_x,mov_y)
       
class Queen(Piece):
    
   def Validation(self, board,mov_x,mov_y):
       if mov_y == 0 and mov_x != 0:
           self.move( board,mov_x,mov_y)
       if mov_x == 0 and mov_y != 0:
           self.move( board,mov_x,mov_y)
       #bishop
       if mov_x == mov_y and mov_x != 0:
           self.move( board,mov_x,mov_y)

    
class King(Piece):
    
   def Validation(self, board,mov_x,mov_y):
       if ( abs(mov_x) and abs(mov_y) ) <= 1:
           self.move( board,mov_x,mov_y)
''' '''