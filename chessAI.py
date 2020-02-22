# -*- coding: utf-8 -*-
"""

"""


import math
def minimax(pos, depth, alpha, beta, maxPlayer):
    
    if depth == 0 :
        
        return pos.value
 
    if maxPlayer:
        
        maxValue = -math.inf
        for row in RenderTree(pos.root):
            
            value = minimax(pos.child, depth - 1, alpha, beta ,False)
            maxValue = max(maxValue, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                
                break
        return maxValue
 
    else:
        
        minValue = +math.inf
        for row in RenderTree(pos.root):
            value = minimax(pos.child, depth - 1, alpha, beta, True)
            minValue = min(minValue, value)
            beta = min(beta, value)
            if beta <= alpha:
                
                break
        return minValue
 


from anytree import SymlinkNodeMixin, Node, RenderTree
class SymlinkNode(SymlinkNodeMixin):
    def __init__(self, target, matrix,parent=None, children=None):
        self.target = target
        self.parent = parent
        self.matrix = matrix
        if children:
            self.children = children
    def __repr__(self):
        return "SymlinkNode(%r)" % (self.target)

root = Node
s1 = Node("sub1", parent=root)("root")
matrix =  [[0 for _ in range(8)] for _ in range(8)]
l = SymlinkNode(s1, matrix,parent=root)


for row in RenderTree(root):
    print(row)



