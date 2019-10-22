# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:18:39 2019

@author: lydia
"""

#==========================================
# Purpose: 
#   Calculates and produces the Collatz sequence for any positive integer given 
# Input Parameter(s): 
#   n is a positive integer 
# Return Value(s): 
#   A list of numbers in the Collatz sequence from n to 1
#==========================================

def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz(n//2) 
    else:
        return [n] + collatz(n*3+1)

    
#==========================================
# Purpose: 
#   Finds the minimum value in a list of integers
# Input Parameter(s): 
#   num_list is a list of integers 
# Return Value(s): 
#   The minimum value in the list
#==========================================

def find_min(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        if num_list[0] < num_list[1]:
            num_list[1] = num_list[0]
        return find_min(num_list[1:])    


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
#   Determines who can win a game of tic-tac-toe with a given board if both 
#   players are as strategic as possible going forward.  
# Input Parameter(s): 
#   board is a list representation of a tic-tac-toe board 
# Return Value(s): 
#   An integer that represents the current state of the board.
#   1 means that X has won, or can force a win
#   -1 means that O has won, or can force a win
#   0 means that if both players play perfectly, the game will end in a draw        
#==========================================

def force_win(board):
    if winner(board) == 'X':
        return 1
    if winner(board) == 'O':
        return -1
    if winner(board) == 'D':
        return 0
    if len(open_slots(board))%2 == 0:
        #O turn to move
        min_pts = 1
        for move in open_slots(board):
            board_2 = board[:]
            board_2[move] = 'O'
            if force_win(board_2) < min_pts:
                min_pts = force_win(board_2)
        return min_pts  
    else:
        #X turn
        max_pts = -1
        for move in open_slots(board):
            board_2 = board[:]
            board_2[move] = 'X'
            if force_win(board_2) > max_pts:
                max_pts = force_win(board_2)
        return max_pts        
            
#==========================================
# Purpose: 
#   Simulates a single game of tic-tac-toe in which X is played randomly while 
#   O is played strategically.         
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
            min_pts = 1
            for move in open_slots(board):
                board_2 = board[:]
                board_2[move] = 'O'
                if force_win(board_2) < min_pts:
                    min_pts = force_win(board_2)
                    best_move = move
            board[best_move] = 'O'
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