#!/usr/bin/python3
'''
  Inspired by: http://youtu.be/dJe5RnRBTfs?list=PLDFB7FFF90EE6F0C1
'''
from random import shuffle


board = ['A', 'B', 'C', 'D'] * 2
shuffle(board)

board_visible = list('_'*8)

flipped = []

tries = 0

def printBoard(board):
  print(' '.join(board))
  print('0 1 2 3 4 5 6 7')

def boardIsComplete(board):
  return not '_' in board
  

while True:

  printBoard(board_visible)

  if boardIsComplete(board_visible):
    print('You won in {} steps!'.format(tries))
    break

  if len(flipped) == 2:
    a, b = [board[i] for i in flipped]
    if a != b:
      for i in flipped:
        board_visible[i] = '_'
  print(tries)
    flipped = []

  user_input = input('> ')

  if user_input == 'q':
    break

  try:
    idx = int(user_input)
    if board_visible[idx] != '_':
      raise ValueError
      continue
    tries += 1
    board_visible[idx] = board[idx]
    flipped.append(idx)
  except (ValueError, IndexError):
    print('Invalid input.\nPress buttons 0-7 or q to quit.')

