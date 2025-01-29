import class444 as c
from random import choice
import sys


def cmp(game):
    return (game.get_cards_quantity(1)-game.get_cards_quantity(2))+3*(game.get_points(1) - game.get_points(2))

class MinimaxPlayer:
    def __init__(self, depth):
        self.depth = depth
        self.cmp=cmp

    def minimax(self, game, depth, is_maximizing):
        if depth == 0:
            return cmp(game)
        
        if game.get_position()[0] == []:
            return -10**10
        
        if game.get_position()[1] == []:
            return 10**10
        
        if is_maximizing:
            max_eval = -sys.maxsize
            for move in game.get_position()[0]:
                game_copy = game.copy()
                game_copy.play(move)
                eval = self.minimax(game_copy, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = sys.maxsize
            for move in game.get_position()[1]:
                game_copy = game.copy()
                game_copy.play(move)
                eval = self.minimax(game_copy, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self, game, player):
        best_move = None
        best_value = -sys.maxsize if player == 1 else sys.maxsize

        for move in game.get_position()[player - 1]:
            game_copy = game.copy()
            game_copy.play(move)
            value = self.minimax(game_copy, self.depth, player == 2)
            if (player == 1 and value > best_value) or (player == 2 and value < best_value):
                best_value = value
                best_move = move   


        return best_move
