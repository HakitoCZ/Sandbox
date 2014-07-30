#!/usr/bin/python3

board = ['A', 'B', 'C', 'D'] * 2

board_visible = list('________')

flipped = []

while True:

  print(' '.join(board_visible))
  print('0 1 2 3 4 5 6 7')

  if len(flipped) == 2:
    a, b = [board[i] for i in flipped] # whateveer does it do
    if a != b:
      for i in flipped:
        board_visible[i] = '_'
    flipped = []

  user_input = input('> ')

  if user_input == 'q':
    break

  try:

    idx = int(user_input)

    board_visible[idx] = board[idx]

    flipped.append(idx)

  except (ValueError, IndexError):
    print('Invalid input.\nPress buttons 0-7 or q to quit.')

