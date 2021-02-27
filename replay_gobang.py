import gobang_vision as gv
import time
f = open("test.txt", "r")
games = f.read()
f.close()
games = games.split(":")
print("total games:"+str(len(games)-1))
print("game_number:")
game_number = int(input())-1
print("speed:")
speed = int(input())
game_moves = eval(games[game_number])
gv.setup()
i = 0
for e in game_moves:
  gv.place_piece_gobang(i%2+1,gv.P(e[0],e[1]))
  time.sleep(2/speed)