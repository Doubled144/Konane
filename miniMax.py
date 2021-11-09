
#Joeseph Malone & DOMINIC DuRant

import math
from konane import *;

class MinimaxPlayer(Konane, Player): 
    
    def __init__(self, size, depthLimit):         
        Konane.__init__(self, size)         
        self.limit = depthLimit 
 
    def initialize(self, side):         
        self.side = side
        if side == "B":
            self.name = "KingOfGames1"
        else:
            self.name = "KingOfGames2"

    def eval(self, board):
        n = len(board)
        if n == 0:
            return (0)
        else:
            return (self.countSymbol(board, 'W'))

    def MiniMax(self, board, depth, a, b, maximizingPlayer):
        #return best move
        
        if (depth == 0):
            return (self.eval (board), [])
        
        if (maximizingPlayer):
            value = -float('inf')
            miniMaxBoard = board
            #Get all possible moves
            #Call max on each one with decramented depth        
            moves = self.generateMoves(board, self.side)
            if moves == []:
                return (-float('inf'), [])
            for move in moves:
                miniMaxMove = self.MiniMax(self.nextBoard(board, self.side, move), (depth - 1), a, b, False)
                # value = 
                if(value < miniMaxMove[0]):
                    value = miniMaxMove[0]
                    miniMaxBoard = move
                a = max(a, value)
                if (a >= b):
                    break

            return (value, miniMaxBoard)
        else:
            otherSide = ''
            if(self.side == 'B'):
                otherSide = 'W'
            else:
                otherSide = 'B'
            value = float('inf')
            miniMaxBoard = board
            moves = self.generateMoves(board, otherSide)
            if moves == []:
                return (float('inf'), [])        
            for move in moves:
                miniMaxMove = self.MiniMax(self.nextBoard(board, otherSide, move), (depth - 1), a, b, True)
                if(value > miniMaxMove[0]):
                    value = miniMaxMove[0]
                    miniMaxBoard  = move
                b = min(b, value)
                if (b <= a):
                    break
            
            return (value, miniMaxBoard)

    def getMove(self, board):
        return self.MiniMax(board, self.limit, -float('inf'), float('inf'), True)[1]
     
game = Konane(8)
game.playNGames(20, MinimaxPlayer(8,4), SimplePlayer(8), 0)  