import random

def generate_new_board():
    '''
    To generate a new board
    '''
    board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    return board;

def print_board(board):
    '''
    To print the current situation of board
    '''
    symbols = {0: ' ', 1: 'X', -1: 'O'}
    for i, row in enumerate(board):
        print(" |".join(symbols[cell] for cell in row))
        if i < 2:
            print("-" * 8)

def play_turn(board, turn, position):
    '''
    To play a turn on the board

    board: the current board on which game is going on
    turn: whole turn (1->X | 0->O)
    position: where to play (1 to 9)
    '''

    row = (position-1) // 3
    col = (position-1) % 3

    if(board[row][col] != 0): return -1

    else: board[row][col] = turn

    return 1

def is_game_finish(board):
    ''' 
    Return the player which won, in case of draw return 2
    '''                
    
    for i in range(3): # cheching columns
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i] != 0 : return board[1][i]

    for i in range(3): # checking rows
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1] != 0 : return board[i][1]

    # checking diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != 0 : return board[0][0]

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != 0 : return board[0][2]

    #check draw
    filled = 0
    for row in board:
        for elem in row:
            if elem != 0: filled += 1
    
    if filled == 9: return 2

    return 0

def get_valid_moves(board):
    '''To get valid moves'''
    return [i for i in range(1, 10) if board[(i-1)//3][(i-1)%3] == 0]

def get_board_state(board):
    '''To get the board in a single list'''
    return [cell for row in board for cell in row]
    


 


        



