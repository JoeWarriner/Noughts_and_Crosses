from gamestate import GameState
import time

POTENTIAL_MOVES = [
    [1, 1],  # Middle
    [0, 0],  # Corners
    [2, 2],
    [0, 2],
    [2, 0],
    [1, 0],  # Sides
    [0, 1],
    [2, 0],
    [0, 2]
]




game = GameState()

print(game.board)

##Turns 1-8:

while game.turn <= 8:

    ##Player Turn - Request input
    print("Your turn! Where you would you like to go?")
    print('Input coordinates in the form x,y')
    user_move_sl = input().split(",")

    ##Convert user move into coordinates and make the move.
    user_move = []
    user_move.append(int(user_move_sl[0]))
    user_move.append(int(user_move_sl[1]))
    game.make_move('crosses', user_move)
    print(game.board)

    ## Check if player has won:
    if game.check_win('crosses') == True:
        game.game_over = True
        break

    ## Update turn counter
    game.turn += 1

    ## COMPUTER TURN - preamble
    print("Now the computer's turn!")
    print("Computer is thinking...")
    time.sleep(2)
    print("The computer's move is:")
    computer_move = []


    ## 1st Priority - Check if it can win, if so, find the space it needs to do so:
    if game.check_near_win('noughts') == True:
        computer_move = game.near_win_coords('noughts')

    ## 2nd Priority - check if player can win, if so, find the space it needs to block:
    elif game.check_near_win('crosses') == True:
        computer_move = game.near_win_coords('crosses')

    ## 3rd Priority - cycle through moves in order of priority. First middle, then corners, then side squares.
    else:
        for i in POTENTIAL_MOVES:
            if game.check_move_possible(i) == True:
                computer_move = i
                break



    ## Computer should have chosen, now they actually make their move.
    game.make_move('noughts',computer_move)
    print(game.board)

    ## Check if computer has won:
    if game.check_win('noughts') == True:
        print("Computer wins!")
        game.game_over = True
        break

    game.turn += 1

if game.game_over == False:
    ##Player Turn - Request input
    print("Final turn! Where you would you like to go?")
    print('Input coordinates in the form x,y')
    user_move_sl = input().split(",")

    ##Convert user move into coordinates and make the move.
    user_move = []
    user_move.append(int(user_move_sl[0]))
    user_move.append(int(user_move_sl[1]))
    game.make_move('crosses', user_move)
    print(game.board)

## Final check if player has won:

if game.check_win('crosses') == True:
    print("You win!")
    game.game_over = True

if game.game_over == False:
    print("It's a draw!")

print("Game over!")





