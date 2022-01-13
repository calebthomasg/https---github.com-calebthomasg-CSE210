###CREATED BY CALEB GENTRY###
#THE BOARD
"""
MY BOARD WILL BE MADE FROM LISTS INSIDE AN ARRAY
[
    [-, -, -],
    [-, -, -],
    [-, -, -]  
]
"""
#USER INTERACTION
"""
USERS WILL NEED TO INPUT SOMETHING IN ORDER TO CHOOSE A SQUARE. IN
THIS CASE, THEY WILL NEED TO INPUT A NUMBER FROM 1-9 AS THERE ARE A
TOTAL OF 9 SQUARES IN THE GAME OF TIC-TAC-TOE.
"MAKE YOUR MOVE (TYPE A NUMBER FROM 1-9)"
IF THEY INPUT SOMETHING BESIDES 1-9, THERE NEEDS TO BE A PROMPT.
"YOU MUST CHOOSE A NUMBER FROM 1-9"
IF THEY INPUT A NUMBER THAT'S ALREADY BEEN TAKEN, THERE NEEDS TO
BE A PROMPT.
"YOU MUST SELECT AN OPEN SQUARE"
"""
#GAME PROCESS
"""
-USER INPUTS NUMBER
-NUMBER IS ADDED TO BOARD
-CHECK IF USER HAS WON
-GAME CONTINUES/ENDS
"""

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

player = True
turn = 0
def display(board):
    for row in board:
        for slot in row:
            print(f"{slot}  ", end=" ")
        print()
        

def quit(user_input):
    if user_input.lower() == "q":
        print("YOU QUIT THE GAME")
        return True
    else: return False
    
def game_process(user_input):
    #IS IT A NUMBER? 
    if not number(user_input): return False
    user_input = int(user_input)
    #IS IT BETWEEN 1-9?
    if not one_nine(user_input): return False
    
    return True

def number(user_input):
    if  not user_input.isnumeric():
        print("THIS IS NOT A VALID OPTION.")
        return False
    else: return True
    
def one_nine(user_input):
    if user_input >9 or user_input <1:
        print("NOT A VALID NUMBER.")
        return False
    else: return True
    
def taken(squarez, board):
    row = squarez[0]
    column = squarez[1]
    if board[row][column] != "_":
        print("SQUARE IS ALREADY TAKEN")
        return True
    else: return False
    
def squares(user_input):
    row = int(user_input / 3)
    column = user_input
    if column > 2: column = int(column % 3)
    return(row, column)

def add_square(squarez, board, active_player):
    row = squarez[0]
    column = squarez[1]
    board[row][column] = active_player
    
def current_player(player):
    if player: return "X"
    else: return "O"
    
def winner(player, board):
    if check_row(player, board): return True
    if check_column(player, board): return True
    if check_diagnal(player, board): return True
    return False

def check_row(player, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != player:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_column(player, board):
    for column in range(3):
        complete_column = True
        for row in range(3):
            if board[row][column] != player:
                complete_column = False
                break
        if complete_column: return True
    return False

def check_diagnal(player, board):
    if board[0][0] ==player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else: return False

while turn <9:
    active_player = current_player(player)
    display(board)
    user_input = input("MAKE YOUR MOVE (TYPE A NUMBER FROM 1-9) OR ENTER Q TO QUIT:")
    if quit(user_input):
        break
    if not number(user_input):
        print("TRY AGAIN.")
        continue
    user_input = int(user_input) -1
    squarez = squares(user_input)
    board[0][0] = "X"
    if taken(squarez, board):
        print("TRY AGAIN")
        continue
    add_square(squarez, board, active_player)
    if winner(active_player, board):
        print(f"{active_player.upper()} WON!")
        break
    
    turn +=1
    if turn == 9:
        print("TIE")
    player = not player
    #BECAUSE ARRAYS START AT 0

    
