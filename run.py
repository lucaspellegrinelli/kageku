import random

from flags import *
from action import *
from kageku import *

game = Kageku()
mvs = game.available_actions()
print(mvs)
