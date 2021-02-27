gobangboard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
moves=[]

from collections import namedtuple

class P:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def print_gobangboard():
  for e in gobangboard:
    print(e)
def place_piece_gobang(player,position):
  global gobangboard
  if gobangboard[position.x][position.y] == 0:
    gobangboard[position.x][position.y] = player
  else:
    print("bruh")
    return 0
  if if_win_gobang(player,position) == 1:
    print("noice u win")
    gobangboard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    return 1
  else:
    gobangboard[position.x][position.y] = player
    print("oof")
    print_gobangboard()
    return 0
def if_win_gobang(player,position):
  lines = [0,0,0,0]
  for e in range(1,5):
    if position.x+e < 15 and  position.y+e < 15 and gobangboard[position.x+e][position.y+e] == player:
      lines[0] += 1
    else:
      break
  for e in range(-1,-5,-1):
    if position.x+e >= 0 and position.y+e >= 0 and gobangboard[position.x+e][position.y+e] == player:
      lines[0] += 1
    else:
      break
  for e in range(1,5):
    if position.x-e >= 0 and position.y+e < 15 and gobangboard[position.x-e][position.y+e] == player:
      lines[1] += 1
    else:
      break
  for e in range(1,5):
    if position.x+e < 15 and position.y-e >= 0 and gobangboard[position.x+e][position.y-e] == player:
      lines[1] += 1
    else:
      break
  for e in range(1,5):
    if position.x+e < 15 and gobangboard[position.x+e][position.y] == player:
      lines[2] += 1
    else:
      break
  for e in range(1,5):
    if position.x-e >= 0 and gobangboard[position.x-e][position.y] == player:
      lines[2] += 1
    else:
      break
  for e in range(1,5):
    if position.y+e < 15 and gobangboard[position.x][position.y+e] == player:
      lines[3] += 1
    else:
      break
  for e in range(1,5):
    if position.y-e >= 0 and gobangboard[position.x][position.y-e] == player:
      lines[3] += 1
    else:
      break
  for e in lines:
    if e >= 4:
      return 1
  return 0
def play_gobang():
  print("player:")
  player = int(input())
  # 1,2
  print("position:")
  p = input()
  x,y = p.split(",")
  l = P(int(x),int(y))
  position = l
  while play_gobang(player,position) == 0:
    print("player:")
    player = int(input())
    # 1,2
    print("position:")
    p = input()
    x,y = p.split(",")
    l = P(int(x),int(y))
    position = l
