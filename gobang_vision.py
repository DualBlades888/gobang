from ai import dumb_AI
import turtle
from lib_gobang import P
gogang = turtle.Turtle()
gobangboard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
moves=[]

from collections import namedtuple
class Person:
  def __init__(self):
    pass
  def next_move(self, board):
    print("position:")
    p = input()
    x,y = p.split(",")
    l = P(int(x),int(y))
    return l

def print_gobangboard():
  for e in gobangboard:
    print(e)
def place_piece_gobang(position):
  global gobangboard
  global moves
  player = len(moves)%2+1
  if gobangboard[position.y][position.x] == 0:
    gobangboard[position.y][position.x] = player
    moves.append([position.x,position.y])
    draw_circle_gogang(position)
  else:
    print("bruh")
    return 0
  if if_win_gobang(player,P(position.y,position.x)) == 1:
    gobangboard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    return 1
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
def get_gogang_position(position):
  return P(40*position.x-300, 300-40*position.y)
def draw_circle_gogang(position):
  global moves
  if len(moves)%2+1 == 1:
    gogang.fillcolor("black")
  else:
    gogang.fillcolor("cyan")
  l = get_gogang_position(position)
  gogang.goto(l.x-20,l.y)
  gogang.pendown()
  gogang.begin_fill()
  gogang.circle(20)
  gogang.end_fill()
  gogang.penup()
def setup():
  gogang.color("blue","cyan")
  gogang.speed(10000)
  gogang.hideturtle()
  gogang.penup()
  start = P(0,0)
  for e in range(15):
    gogang.goto(get_gogang_position(start).x,get_gogang_position(start).y)
    gogang.pendown()
    gogang.forward(560)
    gogang.penup()
    gogang.goto(get_gogang_position(P(start.x-1,start.y)).x,get_gogang_position(start).y)
    gogang.pendown()
    gogang.write(str(start.y),font=("Arial", 16, "normal"))
    gogang.penup()
    start.y += 1
  #gogang.write("1 2 3 4 5 6 7 8 9",font=("Arial", 72, "normal"))
  start = P(0,0)
  gogang.right(90)
  for e in range(15):
    gogang.goto(get_gogang_position(start).x,get_gogang_position(start).y)
    gogang.pendown()
    gogang.forward(560)
    gogang.penup()
    gogang.goto(get_gogang_position(start).x,get_gogang_position(P(start.x,start.y-1)).y)
    gogang.pendown()
    gogang.write(str(start.x),font=("Arial", 16, "normal"))
    gogang.penup()
    start.x += 1
  gogang.penup()
def play_gobang_pvp():
  global gobangboard
  global moves
  flag = True
  setup()
  while flag:#play_gobang(player,position) == 0
    players = [
      Person(),
      dumb_AI()
    ]
    for e in players:
      position = e.next_move(gobangboard)
      if place_piece_gobang(position) == 1:
        f = open("test.txt","w")
        f.write(str(moves)+":")
        f.close()
        flag = False
        break

    print_gobangboard()
  print("noice u win!!")
if __name__ == "__main__":
  play_gobang_pvp()