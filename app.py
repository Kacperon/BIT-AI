from fastapi import FastAPI
from class444 import Game_class
from minmax_alfa_beta import MinimaxabPlayer
from minmax import MinimaxPlayer
from monte_carlo_time import MonteCarloPlayer

app = FastAPI()

@app.post("/start_game")
def start_game(n: int):
    "return the map of the game as a list of lists of triples"
    "where first element is a player number and the second contains card value"
    game = [[None for _ in range(n)] for _ in range(n)]
    if n <= 4:
        game[0][0] = (1, 1)
        game[n-1][n-1] = (2, 1)
    else:
        game[1][1] = (1, 1)
        game[n-2][n-2] = (2, 1)
    return {"game": game}

@app.post("/get_valid_moves")
def get_valid_moves(tab: list, player: int):
    "return a list of valid moves for the current player"
    Game = Game_class(0)
    Game.import_game(tab, player)
    return {"valid_moves": Game.get_position()[Game.current_player-1]}

@app.post("/make_move")
def make_move(tab: list, move: tuple, player: int):
    "make a move for the current player and return the new map and the winner or 0 if the game is not finished"
    Game = Game_class(0)
    Game.import_game(tab, player)
    tab = Game.play_visual(move)
    winner = Game.get_winner()
    return {"new_game_state": tab, "winner": winner}

@app.post("/generate_move_minmax")
def generate_move_minmax(game: list, depth: int, if_alphabeta: bool):
    "return the best move for the current player using Minmax algorithm"
    Game = Game_class(0)
    Game.import_game(game, 1)
    if if_alphabeta:
        best_move = MinimaxabPlayer(depth).find_best_move(Game, Game.current_player)
    else:
        best_move = MinimaxPlayer(depth).find_best_move(Game, Game.current_player)
    return {"best_move": best_move}

@app.post("/generate_move_monte_carlo")
def generate_move_monte_carlo(game: list, time: int):
    "return the best move for the current player using Monte Carlo algorithm"
    Game = Game_class(0)
    Game.import_game(game, 1)
    best_move = MonteCarloPlayer(time).find_best_move(Game, Game.current_player)
    return {"best_move": best_move}
