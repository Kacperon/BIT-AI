import class444 as c
from minmax import MinimaxPlayer
from app import start_game
if __name__ == "__main__":
    game = c.Game_class(0)
    game.import_game(start_game(4), 1)
    player1 = MinimaxPlayer(depth=2)
    while True:
        if game.get_position()[0] == []:
            print("Winner: ", 2)
            print("With points: ", game.get_points(2))
            break
        move1 = player1.find_best_move(game, 1)
        print("Player 1 move: ", move1)
        game.play(move1)
        game.print_map()
        print()
        

        if game.get_position()[1] == []:
            print("Winner: ", 1)
            print("With points: ", game.get_points(1))
            break

        print("Player 2, enter your move (format: row column): ")
        while True:
            try:
                move_input = input("Your move: ").strip()
                move2 = tuple(map(int, move_input.split()))
                if move2 in game.get_position()[1]:
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input format. Use two numbers separated by a space.")
        
        print("Player 2 move: ", move2)
        game.play(move2)
        game.print_map()
        print()
