import random

from flags import *
from action import *
from kageku import *

game = Kageku()

print(game)

game.apply_action(Action(1, WHITE, "h3pg3p"))

print(game)

game.undo_last_action()

print(game)
