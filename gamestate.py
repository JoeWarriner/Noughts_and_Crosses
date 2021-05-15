import pandas as pd
import random

WINNING_SETS = {
    "leftcol" : [[0, 0], [0, 1], [0, 2]],
    "midcol": [[1, 0], [1, 1], [1, 2]],
    "rightcol": [[2, 0], [2, 1], [2, 2]],
    "toprow": [[0, 0], [1, 0], [2, 0]],
    "midrow": [[0, 1], [1, 1], [2, 1]],
    "bottomrow": [[0, 2], [1, 2], [2, 2]],
    "backdiag": [[0, 0], [1, 1], [2, 2]],
    "frontdiag": [[2, 0], [1, 1], [0, 2]]
}



class GameState:
    def __init__(self):
        self.positions = pd.DataFrame([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.board = pd.DataFrame([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])
        self.turn = 1
        self.game_over = False

    def check_sets(self, check_value, sets_dictionary):
        '''
        Generic method to checks if any of the rows in the dictonary passed sum to the value passed.
        Returns a list with T/F at position 0, and the first set it enounters at position 1.
        '''
        for set, coordlist in sets_dictionary.items():
            values = []
            ismatch = False
            for coords in coordlist:
                values.append(self.positions[coords[0]][coords[1]])
            if sum(values) == check_value:
                ismatch = True
                break
        return [ismatch, set]


    def check_winner(self):
        if self.check_sets(30, WINNING_SETS)[0]:
            return 'crosses'
        elif self.check_sets(3, WINNING_SETS)[0]:
            return 'noughts'
        else:
            return 'none'

    def check_near_win(self, player):
        check_sum = 2 if player == 'noughts' else 20
        return self.check_sets(check_sum, WINNING_SETS)[0]

    def near_win_coords(self, player):
        check_sum = 2 if player == 'noughts' else 20
        winning_coords_list = WINNING_SETS[self.check_sets(check_sum, WINNING_SETS)[1]]
        for coords in winning_coords_list:
            if self.positions[coords[0]][coords[1]] == 0:
                return [coords[0], coords[1]]

    def check_move_possible(self, coords):
        if not ((0 <= coords[0] <= 2) and (0 <= coords[1] <= 2)):
            return False
        elif self.positions[coords[0]][coords[1]] == 0:
            return True
        else:
            return False

    def check_mrmc(self, player):
        '''
        Slightly weird one. This is to check if either the middle row or middle column have only one total piece in
        them belonging to the current player. Used for computer decision making.
        '''
        mrmc = {s: WINNING_SETS[s] for s in ('midrow','midcol')}
        check_sum = 1 if player == 'noughts' else 10
        return self.check_sets(check_sum, mrmc)[0]

    def mrmc_coords(self, player):
        mrmc = {s: WINNING_SETS[s] for s in ('midrow', 'midcol')}
        print(mrmc)
        check_sum = 1 if player == 'noughts' else 10
        print(check_sum)
        mrmc_set = mrmc[self.check_sets(check_sum, mrmc)[1]]
        print(mrmc_set)
        random.shuffle(mrmc_set)
        print(mrmc_set)
        for coords in mrmc_set:
            if self.positions[coords[0]][coords[1]] == 0:
                return coords


    def make_move(self, player, coords):
        new_value = 1 if player == 'noughts' else 10
        new_piece = '0' if player == 'noughts' else 'X'
        self.positions[coords[0]][coords[1]] = new_value
        self.board[coords[0]][coords[1]] = new_piece





# ##Tests:
# game = GameState()
# # print(game.positions)
# # print(game.mrmc_coords('noughts'))
#
# # # print(game.check_move_possible([0,0]))
# # print(game.check_move_possible([4,0]))
# # print(game.check_move_possible(["T",0]))
# # print(game.check_move_possible([0,4]))
# print('Overall assessment: ', str(game.check_move_possible([0,2])))


# print("Overall checks:")

# print(game.board)
# game.make_move('noughts', [0,1])
# game.make_move('crosses', [1,1])
# print(game.positions)
# print(game.board)
#
# # # print("Noughts win: " + str(game.check_win('noughts')))
# # # print("Crosses win: " + str(game.check_win('crosses')))
# # # print("Noughts near win: " + str(game.check_near_win('noughts')))
# # # print("Crosses near win:" + str(game.check_near_win('crosses')))
# # # print("Winning coords noughts: " + str(game.near_win_coords('noughts')[0]) + " " + str(game.near_win_coords('noughts')[1]))
# # # print("Winning coords crosses: " + str(game.near_win_coords('crosses')[0]) + " " + str(game.near_win_coords('crosses')[1]))
# # print("Possible move at 0,0: " + str(game.check_move_possible([0, 0])))
