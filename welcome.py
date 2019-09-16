import random

from flags import *
from kageku import *

game = Kageku()

print("Starting board")
print(game)

turn = 0
while not game.is_game_over():
  print("---- Turn", turn // 2 + 1, "----")

  actions = game.available_actions()
  action = random.choice(actions)

  print(("White" if game.turn == WHITE else "Black") + "'s move:", action)

  game.apply_action(action)
  print(game)

  turn += 1

print("The winner is the", ("White" if game.get_winner() == WHITE else "Black"), "player")
