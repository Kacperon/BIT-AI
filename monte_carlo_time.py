import class444 as c
import random
import time

def cmp(game):
    return (game.get_cards_quantity(1)-game.get_cards_quantity(2))/(game.get_cards_quantity(1)+game.get_cards_quantity(2))


class MonteCarloPlayer:
    def __init__(self, total_time):
        self.total_time = total_time

    def simulate_game(self, game):
        while game.get_position()[0] and game.get_position()[1]:
            available_moves = game.get_position()[game.current_player - 1]
            random_move = random.choice(available_moves)
            game.play(random_move)
        return cmp(game)

    def find_best_move(self, game, player):
        move_scores = {}
        moves = game.get_position()[player - 1]
        time_per_move = self.total_time / len(moves)

        for move in moves:
            score = 0
            start_time = time.time()
            iterations = 0

            while time.time() - start_time < time_per_move:
                game_copy = game.copy()
                game_copy.play(move)
                score += self.simulate_game(game_copy)
                iterations += 1

            move_scores[move] = score / iterations if iterations > 0 else 0
        if player == 1:
            best_move = max(move_scores, key=move_scores.get)
        else:
            best_move = min(move_scores, key=move_scores.get)
        
        return best_move
