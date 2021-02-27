from lib_gobang import P
import random
class shape:
  def __init__(self):
      pass
class dumb_AI:
  def __init__(self):
    pass
  def next_move(self,board):
    moves = P(random.randint(0,14),random.randint(0,14))
    while board[moves.y][moves.x] != 0:
      moves = P(random.randint(0,14),random.randint(0,14))
    return moves
class not_so_dumb_AI:
  def __init__(self):
    pass
  def next_move(self,board):
    moves = P(0,0)
    
