import class444 as c
import random

def cmp(game):
    return (game.get_cards_quantity(1)-game.get_cards_quantity(2))/(game.get_cards_quantity(1)+game.get_cards_quantity(2))

def cmp(game):
    return game.get_points(1) - game.get_points(2)

class MonteCarloPlayer:
    def __init__(self, iterations):
        self.iterations = iterations

    def simulate_game(self, game):
        while game.get_position()[0] and game.get_position()[1]:
            available_moves = game.get_position()[game.current_player - 1]
            random_move = random.choice(available_moves)
            game.play(random_move)
        return cmp(game)

    def find_best_move(self, game, player):
        move_scores = {}

        for move in game.get_position()[player - 1]:
            score = 0

            for _ in range(self.iterations):
                game_copy = game.copy()
                game_copy.play(move)
                score += self.simulate_game(game_copy)

            move_scores[move] = score
        if player == 1:
            best_move = max(move_scores, key=move_scores.get)
        else:
            best_move = min(move_scores, key=move_scores.get)
        
        return best_move