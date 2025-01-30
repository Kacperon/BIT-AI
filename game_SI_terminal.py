import class444 as c
from minmax import MinimaxPlayer
from minmax_alfa_beta import MinimaxabPlayer
from monte_carlo import MonteCarloPlayer
from monte_carlo_time import MonteCarloPlayer as MonteCarlotPlayer
from app import start_game


if __name__ == "__main__":
    game = c.Game_class(4)
    game.import_game(start_game(5),1)

    player1 = MinimaxabPlayer(depth=0)
    player2 = MonteCarlotPlayer(2)
    #player2 = MinimaxPlayer(depth=3)
    for t in range(200):
        if game.get_position()[0]==[]:
            print("winer: ",2)
            print("with points: ",game.get_points(2))
            break
        move1 = player1.find_best_move(game, 1)
        print("Player 1 move: ", move1)
        game.play(move1)
        game.print_map()
        print()
        if game.get_position()[1]==[]:
            print("winer: ",1)
            print("with points: ",game.get_points(1))
            break
        move2 = player2.find_best_move(game, 2)
        print("Player 2 move: ", move2)
        game.play(move2)
        game.print_map()
        print()
    print("numer Tury: ",t)

