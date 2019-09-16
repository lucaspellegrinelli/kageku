import random

from flags import *
from action import *
from kageku import *

game = Kageku()

print(game)

for i in range(10):
  moves = game.available_actions()
  game.apply_action(random.choice(moves))
  print(game)
