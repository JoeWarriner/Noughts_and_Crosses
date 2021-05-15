import pandas as pd

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

    def check_winning_rows(self, check_value):
        '''
        Generic method to checks if any of the "winning rows" sum to the value passed.
        Returns a list with T/F at position 0, and the first set it enounters at position 1.
        '''
        for set, coordlist in WINNING_SETS.items():
            values = []
            ismatch = False
            for coords in coordlist:
                values.append(self.positions[coords[0]][coords[1]])
            if sum(values) == check_value:
                ismatch = True
                break
        return [ismatch, set]


    def check_winner(self):
        if self.check_winning_rows(30)[0]:
            return 'crosses'
        elif self.check_winning_rows(3)[0]:
            return 'noughts'
        else:
            return 'none'

    def check_near_win(self, player):
        check_sum = 2 if player == 'noughts' else 20
        return self.check_winning_rows(check_sum)[0]

    def near_win_coords(self, player):
        check_sum = 2 if player == 'noughts' else 20
        winning_coords_list = WINNING_SETS[self.check_winning_rows(check_sum)[1]]
        for coords in winning_coords_list:
            if self.positions[coords[0]][coords[1]] == 0:
                return [coords[0], coords[1]]

    def check_move_possible(self, coords):
        if self.positions[coords[0]][coords[1]] == 0:
            return True
        else:
            return False

    def make_move(self, player, coords):
        new_value = 1 if player == 'noughts' else 10
        new_piece = '0' if player == 'noughts' else 'X'
        self.positions[coords[0]][coords[1]] = new_value
        self.board[coords[0]][coords[1]] = new_piece




##Tests:
# game = GameState()
#
# print("Overall checks:")
# print(game.positions)
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
