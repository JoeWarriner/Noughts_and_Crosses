
import pandas as pd
import time

# Set initial gamestate. Programme runs two gamestates in parallel
gamestate_back = pd.DataFrame([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) #For calculating win conditions, noughts are 1s, crosses are 10s.
gamestate_array_front = pd.DataFrame([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]) #To display to user
turn = 1
game_over = False

# Define the sets of coordinates that form the "winning lines"
winning_sets = {
    "leftcol" : [[0, 0], [0, 1], [0, 2]],
    "midcol": [[1, 0], [1, 1], [1, 2]],
    "rightcol": [[2, 0], [2, 1], [2, 2]],
    "toprow": [[0, 0], [1, 0], [2, 0]],
    "midrow": [[0, 1], [1, 1], [2, 1]],
    "bottomrow": [[0, 2], [1, 2], [2, 2]],
    "backdiag": [[0, 0], [1, 1], [2, 2]],
    "frontdiag": [[2, 0], [1, 1], [0, 2]]
}

# Function to iterate across the winning sets, checking if any sum of a set matches the int specified.
# e.g. if a winning set = 30, crosses wins.
# Returns list with True/False for a match, and the matching set.
def check_sets(x):
    for set, coordlist in winning_sets.items():
        values = []
        ismatch = False
        for coords in coordlist:
            values.append(gamestate_back[coords[0]][coords[1]])
        if sum(values) == x:
            ismatch = True
            break
    return[ismatch, set]

##UNUSED Checks if someone has won. Returns 0 if nobody has won.
# def check_win():
#     if check_sets(30)[0] == True:
#         return([True, "Player"])
#     elif check_sets(3)[0] == True:
#         return([True, "Computer"])
#     else:
#         return([False, ""])


print(gamestate_array_front)

while turn <= 8:


    ##Player Turn - Request input
    print("Your turn! Where you would you like to go?")
    print('Input coordinates in the form x,y')
    user_move_sl = input().split(",")

    ##Convert user move into coordinates and make the move.
    user_move = []
    user_move.append(int(user_move_sl[0]))
    user_move.append(int(user_move_sl[1]))
    gamestate_back[user_move[0]][user_move[1]] = 10
    gamestate_array_front[user_move[0]][user_move[1]] = "X"
    print(gamestate_array_front)

    ## Check if player has won:
    if check_sets(30)[0] == True:
        game_over = True
        break

    turn += 1

    ## Computer turn - preabmle
    print("Now the computer's turn!")
    print("Computer is thinking...")
    time.sleep(2)
    print("The computer's move is:")
    computer_move = []

    ## 1st Priority - Check if it can win, if so, find the space it needs to do so:
    if check_sets(2)[0] == True:
        for coords in winning_sets[check_sets(2)[1]]:
            if gamestate_back[coords[0]][coords[1]] == 0:
                computer_move = [coords[0], coords[1]]

    ## 2nd Priority - check if player can win, if so, find the space it needs to block:
    elif check_sets(20)[0] == True:
        for coords in winning_sets[check_sets(20)[1]]:
            if gamestate_back[coords[0]][coords[1]] == 0:
                computer_move = [coords[0], coords[1]]

    ## 3rd Priority - play the middle space.
    elif gamestate_back[1][1] == 0:
        computer_move = [1,1]

    ## 4th Priority - one of the corners
    # TODO - Make corner choice either strategic or at least random.
    elif gamestate_back[0][0] == 0:
        computer_move = [0, 0]
    elif gamestate_back[2][2] == 0:
        computer_move = [2, 2]
    elif gamestate_back[0][2] == 0:
        computer_move = [0,2]
    elif gamestate_back[2][0] == 0:
        computer_move = [2,0]

    ## 5th Priority - one of the side squares.
    # TODO - make side choice either strategic or at least random.
    elif gamestate_back[1][0] == 0:
        computer_move = [1, 0]
    elif gamestate_back[0][1] == 0:
        computer_move = [0,1]
    elif gamestate_back[2][0] == 0:
        computer_move = [2,0]
    elif gamestate_back[0][2] == 0:
        computer_move = [0,2]

    ## Computer should have chosen, now they actually make their move.
    gamestate_back[computer_move[0]][computer_move[1]] = 1
    gamestate_array_front[computer_move[0]][computer_move[1]] = "0"
    print(gamestate_array_front)

    ## Check if computer has won:
    if check_sets(3)[0] == True:
        print("Computer wins!")
        game_over = True
        break

    turn += 1

if game_over == False:
    ##Player Turn - Request input
    print("Final turn! Where you would you like to go?")
    print('Input coordinates in the form x,y')
    user_move_sl = input().split(",")

    ##Convert user move into coordinates and make the move.
    user_move = []
    user_move.append(int(user_move_sl[0]))
    user_move.append(int(user_move_sl[1]))
    gamestate_back[user_move[0]][user_move[1]] = 10
    gamestate_array_front[user_move[0]][user_move[1]] = "X"
    print(gamestate_array_front)


## Final check if player has won:

if check_sets(30)[0] == True:
    print("You win!")
    game_over = True

if game_over == False:
    print("It's a draw!")

print("Game over!")





