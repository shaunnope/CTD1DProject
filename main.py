import math
import random
from copy import deepcopy

import tkinter as tk

# displays current state of the board
def display_board(board):
  pass

# checks if coords provided point to an empty cell
# coord format
def coordinates_valid(board,coords):
  x_coord = coords[0]
  y_coord = coords[1]

  # Check if coordinates are within range
  is_valid = (x_coord < 3 and y_coord < 3) 
  if(is_valid):
      is_valid = (board[x_coord][y_coord] == 0)
  
  # If coordinates are invalid, let the user know
  if(not is_valid):
      error_message = f"Coordinates for given action are invalid! (You passed x_coord = {x_coord} and y_coord = {y_coord})"
      print(error_message)
  
  # Return the boolean is_valid
  return is_valid

# attempts to play a move at provided coords, updates board if valid move
def update_board(board, coords, is_circle):
  x_coord = coords[0]
  y_coord = coords[1]

  # Display previous board
  print("--- Displaying previous board. ---")
  display_board(board)
  
  # Check if we have valid coordinates
  is_valid = coordinates_valid(board,coords)
  
  # If valid coordinates, update the board
  new_board = deepcopy(board)
  if(is_valid):
      new_board[x_coord,y_coord] = 2 - int(is_circle)

  # Display new board
  print(f"Displaying new board after action [{x_coord} , {y_coord}].")
  display_board(new_board)
  
  # Return new board
  return new_board

# checks if a win is attained on a face
def check_win(board, coords):
  x_coord = coords[0]
  y_coord = coords[1]

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

# count the number of wins for each player
def count_wins(board):
  pass

# update the number of wins for each player
def update_wins(board, cube):
  pass

# shifts cells by move
def turn_cube(board, move):
  pass

# checks if game is over. ie. 3 concurrent wins
def is_over(board, wins_needed = 3):
  pass


