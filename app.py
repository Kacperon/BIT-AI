from class444 import Game_class
from minmax_alfa_beta import MinimaxabPlayer
from minmax import MinimaxPlayer
from monte_carlo_time import MonteCarloPlayer


def start_game(n: int) -> list:
    "return the map of the game as a list of lists of triples"
    "where first element is a player number and the second contains card value"
    game = [[None for _ in range(n)] for _ in range(n)]
    if n<3:
        game[0][0] = (1, 1)
        game[n-1][n-1] = (2, 1)
    else:
        game[1][1] = (1, 1)
        game[n-2][n-2] = (2, 1)
    return game

def get_valid_moves(tab: list) -> list:
    "return a list of valid moves for the current player"
    Game=Game_class(0)
    Game.import_game(tab,1)
    return Game.get_position()[Game.current_player-1]

def make_move(tab: list, move: tuple, player) -> tuple[list, int]:
    "make a move for the current player and return the new map and the winner or 0 if the game is not finished"
    Game=Game_class(0)
    Game.import_game(tab,player)
    tab=Game.play_visual(move)
    winer=Game.get_winner()
    return tab,winer

def generate_move_minmax(game:list,deph: int,if_alphabeta: bool) -> tuple:
    "return the best move for the current player using Minmax algorithm"
    Game=Game_class(0)
    Game.import_game(game,1)
    if if_alphabeta:
        return MinimaxabPlayer(deph).find_best_move(Game,Game.current_player)
    else:
        return MinimaxPlayer(deph).find_best_move(Game,Game.current_player)
    
def generate_move_monte_carlo(game: list,time: int) -> tuple:
    "return the best move for the current player using Monte Carlo algorithm"
    Game=Game_class(0)
    Game.import_game(game,1)
    return MonteCarloPlayer(time).find_best_move(Game,Game.current_player)

