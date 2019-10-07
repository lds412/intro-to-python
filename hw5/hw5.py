# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:35:27 2019

@author: lydia
"""

#==========================================
# Purpose: 
#   Detects students who get good grades, have a social life, 
#   and get enough sleep
# Input Parameter(s): 
#   grades is a list of students who get good grades 
#   life is a list of students who have a social life 
#   sleep is a list of students who get enough sleep 
# Return Value(s): 
#   A list of all students who appear in all three lists.
#==========================================

def wizards(grades, life, sleep):
    wiz=[]
    for i in grades:
        if i in life and i in sleep:
          wiz.append(i)
    return wiz      


#==========================================
# Purpose: 
#   Detects which spots are still open on a tic-tac-toe board
# Input Parameter(s): 
#   board is a list that represents a tic-tac-toe board 
# Return Value(s): 
#   A list of the indexes which are still open (contain a '-')
#==========================================
    
def open_slots(board):
    open_spots=[]
    for i in range(len(board)):
        if board[i] == '-':
            open_spots.append(i)
    return open_spots

#==========================================
# Purpose: 
#   Determines the winner of a tic-tac-toe game
# Input Parameter(s): 
#   board is a list that represents a tic-tac-toe board  
# Return Value(s): 
#    A single character string that describes whether a player has won the game
#   'X', if X won the game
#   'O', if O won the game 
#   'D', if the game ended in a draw
#   '-', if the game is not over    
#==========================================

def winner(board):  
    if board[0:3] == ['X','X','X'] or board[3:6] == ['X','X','X']\
    or board[6:9] == ['X','X','X'] or board[0:7:3] == ['X','X','X']\
    or board[1:8:3] == ['X','X','X'] or board[2:9:3] == ['X','X','X']\
    or board[0:9:4] == ['X','X','X'] or board[2:7:2] == ['X','X','X']:
        return 'X'
    elif board[0:3] == ['O','O','O'] or board[3:6] == ['O','O','O']\
    or board[6:9] == ['O','O','O'] or board[0:7:3] == ['O','O','O']\
    or board[1:8:3] == ['O','O','O'] or board[2:9:3] == ['O','O','O']\
    or board[0:9:4] == ['O','O','O'] or board[2:7:2] == ['O','O','O']:
        return 'O'
    elif open_slots(board) != []:
        return '-'  
    else:
        return 'D'
    
#==========================================
# Purpose: 
#   Simulates a single game of tic-tac-toe in which the computer plays 
#   randomly against itself.
# Input Parameter(s): 
#   None
# Return Value(s): 
#   A one character string that signifies the winner 
#   ('X', 'O', or 'D' for a draw)
#==========================================

import random

def tic_tac_toe():
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    while winner(board) == '-':
        move = random.choice(open_slots(board))
        board[move] = 'X'
        if winner(board) == '-':
            move = random.choice(open_slots(board))
            board[move] = 'O'
    return winner(board)    
    
#==========================================
# Purpose: 
#   Calls tic_tac_toe n times, and prints out the total number of times X won, 
#   the number of times O won, and the number of times that a draw occurred. 
# Input Parameter(s): 
#   n is an integer representing the number of games to play
# Return Value(s): 
#   None
#==========================================

def play_games(n):
    X = 0
    O = 0
    D = 0
    for i in range(n):
        game = tic_tac_toe()
        if game == 'X':
            X += 1
        if game == 'O':
            O += 1
        if game == 'D':
            D += 1
    print("X wins:",X)
    print("O wins:",O)
    print("Draws:",D)        