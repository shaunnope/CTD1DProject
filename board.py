from copy import deepcopy

class Board:
  # init empty board and board score
  def __init__(self):
    self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    self.wins = {'circle': 0, 'cross': 0}

  # returns True if coords provided is empty cell
  # False otherwise
  def coordinates_valid(self, coords):
    x_coord = coords[0]
    y_coord = coords[1]

    # Check if coordinates are within range
    is_valid = (x_coord < 3 and y_coord < 3)
    # Check if cell is empty
    if (is_valid):
      is_valid = (self.board[x_coord][y_coord] == 0)

    # If coordinates are invalid, let the user know
    if (not is_valid):
      error_message = f"Coordinates for given action are invalid! (You passed x_coord = {x_coord} and y_coord = {y_coord})"
      print(error_message)

    # Return the boolean is_valid
    return is_valid

  # attempt to update board with given move
  # if valid move, return new board and update is_circle
  # if invalid, return current board and is_circle
  def update_board(self, coords, is_circle):
    x_coord = coords[0]
    y_coord = coords[1]

    # Check if we have valid coordinates
    is_valid = self.coordinates_valid(self.board, coords)

    # If valid coordinates, update the board
    new_board = deepcopy(self.board)
    if (is_valid):
      new_board[x_coord, y_coord] = 2 - int(is_circle)
      return new_board, not is_circle
    else:
      return new_board, is_circle

  # checks if a win is attained on a face
  def check_win(self, coords):
    x_coord = coords[0]
    y_coord = coords[1]
    board = self.board

    # Check if new action wins the game. If the game is won, win = True
    win = False

    # Check columns
    if x_coord == 0:
      if board[x_coord, y_coord] == board[x_coord + 1, y_coord] == board[x_coord + 2, y_coord]:
        win = True
    elif x_coord == 1:
      if board[x_coord, y_coord] == board[x_coord + 1, y_coord] == board[x_coord - 1, y_coord]:
        win = True
    elif x_coord == 2:
      if board[x_coord, y_coord] == board[x_coord - 1, y_coord] == board[x_coord - 2, y_coord]:
        win = True

    # Check rows
    if y_coord == 0:
      if board[x_coord, y_coord] == board[x_coord, y_coord + 1] == board[x_coord, y_coord + 2]:
        win = True
    elif y_coord == 1:
      if board[x_coord, y_coord] == board[x_coord, y_coord + 1] == board[x_coord, y_coord - 1]:
        win = True
    elif y_coord == 2:
      if board[x_coord, y_coord] == board[x_coord, y_coord - 1] == board[x_coord, y_coord - 2]:
        win == True

    # Check top-left to bottom-right diagonal
    if y_coord == x_coord == 0:
      if board[x_coord, y_coord] == board[x_coord + 1, y_coord + 1] == board[x_coord + 2, y_coord + 2]:
        win = True
    elif y_coord == x_coord == 1:
      if board[x_coord, y_coord] == board[x_coord + 1, y_coord + 1] == board[x_coord - 1, y_coord - 1]:
        win = True
    elif y_coord == x_coord == 2:
      if board[x_coord, y_coord] == board[x_coord - 1, y_coord - 1] == board[x_coord - 2, y_coord - 2]:
        win == True

    # Check top-right to botttom-left diagonal
    if y_coord == 0 and x_coord == 2:
      if board[x_coord, y_coord] == board[x_coord - 1, y_coord + 1] == board[x_coord - 2, y_coord + 2]:
        win = True
    elif y_coord == x_coord == 1:
      if board[x_coord, y_coord] == board[x_coord + 1, y_coord + 1] == board[x_coord - 1, y_coord - 1]:
        win = True
    elif y_coord == 2 and x_coord == 0:
      if board[x_coord, y_coord] == board[x_coord + 1, y_coord - 1] == board[x_coord + 2, y_coord - 2]:
        win == True

    return win

# (cross: _ wins, circle: _ wins)
# (no. of wins == 3) == winner
class Cube:
    def __init__(self, wins=3):
        self.boards = [Board() for i in range(6)]
        self.wins_needed = wins

    def display_cube(self):
      pass

    def add_board(self, board):
        self.boards.append(board)

    def is_over(self, board, wins_needed=3):
        pass

    def turn_cube(self, board, move):
        pass
