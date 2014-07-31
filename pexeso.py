#!/usr/bin/python3
'''
  Inspired by: http://youtu.be/dJe5RnRBTfs?list=PLDFB7FFF90EE6F0C1
'''
from random import shuffle


board = ['A', 'B', 'C', 'D'] * 2
shuffle(board)


flipped = []

tries = 0

def printBoard(board):
  board_visible = list('_'*8)
  print(' '.join(board_visible))
  print('0 1 2 3 4 5 6 7')


while True:

  printBoard(board)

  if board_visible == board:
    print('You won in {} steps!'.format(tries))
    break

  if len(flipped) == 2:
    a, b = [board[i] for i in flipped]
    if a != b:
      for i in flipped:
        board_visible[i] = '_'
    flipped = []

  user_input = input('> ')
  print(tries)

  if user_input == 'q':
    break

  try:
    idx = int(user_input)
    if board_visible[idx] != '_':
      raise ValueError
      continue
    board_visible[idx] = board[idx]
    flipped.append(idx)
    tries += 1
  except (ValueError, IndexError):
    print('Invalid input.\nPress buttons 0-7 or q to quit.')

