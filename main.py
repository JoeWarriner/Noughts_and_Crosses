from gamestate import GameState
import time
import random
# TODO: Build a random bot to test if it can ever win.

POTENTIAL_MOVES = [
    [0, 0],  # Corners
    [2, 2],
    [0, 2],
    [2, 0],
    [1, 0],  # Sides
    [0, 1],
    [2, 0],
    [0, 2]
]

def get_user_input():
    user_move_sl = input('Input coordinates in the form x,y:').split(",")
    while True:
        user_move = []
        user_move.append(int(user_move_sl[0]))
        user_move.append(int(user_move_sl[1]))
        if game.check_move_possible(user_move) == True:
            break
        print('Please enter a valid move')
        user_move_sl = input('Input coordinates in the form x,y:').split(",")
    return user_move


def player_turn():
    print(game.board)
    print("Your turn! Where you would you like to go?")
    user_move = get_user_input()
    game.make_move('crosses', user_move)

def computer_turn():
    print(game.board)
    print("Now the computer's turn!")
    print("Computer is thinking...")
    time.sleep(2)
    print("The computer's move is:")
    computer_move = []

    if game.check_near_win('noughts') == True:
        computer_move = game.near_win_coords('noughts')

    elif game.check_near_win('crosses') == True:
        computer_move = game.near_win_coords('crosses')

    elif game.check_mrmc('noughts') == True:
        computer_move = game.mrmc_coords('noughts')

    elif game.check_move_possible([1,1]) == True:
        computer_move = [1, 1]

    else:
        random.shuffle(POTENTIAL_MOVES)
        for i in POTENTIAL_MOVES:
            if game.check_move_possible(i) == True:
                computer_move = i
                break

    game.make_move('noughts', computer_move)

def game_end():
    print(game.board)
    if game.check_winner() == 'crosses':
        print("Congratulations you win!")
    elif game.check_winner() == 'noughts':
        print("The computer wins! Better luck next time")
    else:
        print("It's a draw! This is the logically optimal result")


game = GameState()
while game.turn < 10:
    if game.check_winner() == 'none':
        if game.turn % 2 != 0:
            player_turn()
        else:
            computer_turn()
        game.turn += 1
    else:
        break
game_end()









