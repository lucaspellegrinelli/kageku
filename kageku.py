from flags import *

class Kageku:
  def __init__(self):
    self.board = self.create_initial_board()
    self.actions = []
    self.turn = WHITE

  def create_initial_board(self):
    return [
      [(KING, BLACK), (NO_PIECE, NO_COLOR), (ROOK, BLACK), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR)],
      [(PAWN, BLACK), (PAWN, BLACK), (PAWN, BLACK), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR)],
      [(NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR)],
      [(NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR)],
      [(NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR)],
      [(NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR)],
      [(NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (PAWN, WHITE), (PAWN, WHITE), (PAWN, WHITE)],
      [(NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (NO_PIECE, NO_COLOR), (ROOK, WHITE), (NO_PIECE, NO_COLOR), (KING, WHITE)]
    ]

  def apply_action(self, action):
    if action.type == 0:
      from_pos = self.text_pos_to_int_pos(action.details[0:2])
      to_pos = self.text_pos_to_int_pos(action.details[2:4])
      self.set_piece_at(to_pos, self.get_piece_at(from_pos))
      self.set_piece_at(from_pos, (NO_PIECE, NO_COLOR))
    elif action.type == 1:
      adds = action.unpack_add_action_details()
      for add in adds:
        pos = self.text_pos_to_int_pos(add[0:2])
        piece = PIECE_TEXT_TO_ID[add[2].lower()]
        self.set_piece_at(pos, (piece, action.color))

    self.actions.append(action)
    self.change_turn()

  def undo_last_action(self):
    action = self.actions.pop()
    if action.type == 0:
      from_pos = self.text_pos_to_int_pos(action.details[0:2])
      to_pos = self.text_pos_to_int_pos(action.details[2:4])
      self.set_piece_at(from_pos, self.get_piece_at(to_pos))
      self.set_piece_at(to_pos, (NO_PIECE, NO_COLOR))
    else:
      adds = action.unpack_add_action_details()
      for add in adds:
        pos = self.text_pos_to_int_pos(add[0:2])
        self.set_piece_at(pos, (NO_PIECE, NO_COLOR))

    self.change_turn()

  def is_game_over(self):
    return (PAWN, WHITE) in self.board[0] or (PAWN, BLACK) in self.board[-1] or self.is_checkmate()

  def is_checkmate(self):
    # TODO
    return False

  def get_piece_at(self, pos):
    return self.board[pos[0]][pos[1]]

  def set_piece_at(self, pos, piece):
    self.board[pos[0]][pos[1]] = piece

  def text_pos_to_int_pos(self, str_pos):
    return (8 - int(str_pos[1]), ord(str_pos[0]) - 97)

  def change_turn(self):
    self.turn = WHITE if self.turn == BLACK else BLACK

  def __repr__(self):
    str_repr = ""
    for line in self.board:
      for piece in line:
        piece_repr = PIECE_ID_TO_TEXT[piece[0]] + " "
        piece_repr = piece_repr.upper() if piece[1] == WHITE else piece_repr.lower()
        str_repr += piece_repr
      str_repr += "\n"

    return str_repr
