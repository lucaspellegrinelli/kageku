import random
import time

from flags import *
from kageku import *

iters = 100000
wins = {WHITE: 0, BLACK: 0}

start_time = time.time()

for i in range(iters):
  if i > 0 and i % (iters // 100) == 0:
    print("Running iteration #" + str(i))
    print("  Took %s seconds" % (time.time() - start_time))
    start_time = time.time()

  game = Kageku()

  while not game.is_game_over():
    actions = game.available_actions()
    action = random.choice(actions)
    game.apply_action(action)

  wins[game.get_winner()] += 1

print("White won", str(100 * wins[WHITE] / iters) + "%", "of the games")
print("Black won", str(100 * wins[BLACK] / iters) + "%", "of the games")

# White won 50.448% of the games
# Black won 49.552% of the games
