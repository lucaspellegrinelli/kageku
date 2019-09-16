from flags import *

class Action:
  def __init__(self, color, details):
    self.type = 0 if len(details) == 4 else 1
    self.color = color
    self.details = details

  def unpack_add_action_details(self):
    all_adds = []
    for i in range(0, len(self.details), 3):
      add_str = self.details[i:i + 3]
      add_str = add_str[0:2] + (add_str[2].lower() if self.color == BLACK else add_str[2].upper())
      all_adds.append(add_str)
    return all_adds

  def __repr__(self):
    return ("add" if self.type == 1 else "move") + " " + str(self.details)
