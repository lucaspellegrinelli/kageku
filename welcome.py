import random

from flags import *
from kageku import *

game = Kageku()

print("Starting board")
print(game)

for i in range(10):
  if game.is_game_over():
    break

  print(game.piece_count)
  print("---- Turn", i // 2 + 1, "----")
  actions = game.available_actions()
  action = random.choice(actions)
  game.apply_action(action)
  print(("White" if game.turn == WHITE else "Black") + "'s move:", action)
  print(game)
