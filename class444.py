from print import print_color
import copy

class Rec_Map:

    def __init__(self, n=5, start1=1, start2=3):
        self.map = [[[] for _ in range(n)] for _ in range(n)]
        self.card_list = [[],[]]
        self.map_size=n

    def import_map(self,map):
        self.map = [[[] for _ in range(self.map_size)] for _ in range(self.map_size)]
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j]:
                    self.add_card(i,j,map[i][j][0],map[i][j][1])

    def update_card(self, x, y, player):
        """Add a card to a specific grid position."""
        if self.in_map(x,y):
            if self.map[x][y]:
                # Update the card if it already exists
                self.map[x][y].update(self, x, y, player)
            else:
                raise "Invalid position."
                
        else:
            raise "Invalid position."
        
    def in_map(self,x,y):
        return 0 <= x < self.map_size and 0 <= y < self.map_size
    
    def add_card(self,x,y,player,val=1):
        if self.in_map(x,y):
            if not self.map[x][y]:
                self.map[x][y] = Card(player,val)
                self.card_list[player-1].append((x, y))
            elif self.map[x][y].player != player:
                self.card_list[self.map[x][y].player-1].remove((x, y))
                self.card_list[player-1].append((x, y))
                self.map[x][y].player = player
                self.map[x][y].update(self, x, y, player)
            else:
                self.map[x][y].update(self, x, y, player)

    def get_points(self,player):
        points=0
        for x,y in self.card_list[player-1]:
            points+=self.map[x][y].val
        return points
    
    def get_cards_quantity(self,player):
        return len(self.card_list[player-1])

    def print_map(self):
        """Print the grid with card values."""
        print(end="  ")
        for i in range(self.map_size):
            print(i,end=" ")
        print()
        for i, row in enumerate(self.map):
            print(i,end="|")
            for cell in row:
                if cell:
                    if cell.player==1:
                        print_color(str(cell.val),"red")
                    else: print_color(str(cell.val),"blue")
                else:
                    print("*",end=" ")
            print()

    def return_map(self):
        map = [[None for _ in range(self.map_size)] for _ in range(self.map_size)]
        for i in range(self.map_size):
            for j in range(self.map_size):
                if self.map[i][j]:
                    map[i][j] = (self.map[i][j].player,self.map[i][j].val)
        return map

class Card:
    visualisation=False
    visualisation_maps=[]
    def __init__(self,player,val=1):
        self.val = val  # Initial value of the card
        self.player=player

    def update(self, rec_map, x, y, player):
        if player == self.player:
            if self.val < 3:
                self.val += 1
            else:
                self.val += 1
                if self.visualisation:
                    self.visualisation_maps.append(rec_map.return_map()) 
                rec_map.map[x][y] = None
                rec_map.card_list[player-1].remove((x, y))
                self.break_apart(rec_map, x, y, player)
        else:
            raise "Wrong Player"

    def break_apart(self, rec_map, x, y, player):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            rec_map.add_card(new_x,new_y,player)
                 
class Game_class:

    def __init__(self,n):
        self.rec_map = Rec_Map(n,0,n-1)
        #self.rec_map.print_map()
        self.current_player = 1  # Player 1 starts the game

    def switch_player(self):
        self.current_player = 3 - self.current_player  # Switches 1 -> 2 and 2 -> 1

    def play(self, move):
        x, y = move
        self.rec_map.update_card(x, y, self.current_player)
        self.switch_player()

    def get_position(self):
        return self.rec_map.card_list
    
    def get_points(self,player):
        return self.rec_map.get_points(player)
    
    def get_cards_quantity(self,player):
        return self.rec_map.get_cards_quantity(player)
    
    def import_game(self,map,player):
        self.rec_map = Rec_Map(len(map))
        self.rec_map.import_map(map)
        self.current_player=player
    
    def copy(self):
        new_game = Game_class(0)  # Initialize a dummy game
        new_game.rec_map = copy.deepcopy(self.rec_map)
        new_game.current_player = self.current_player
        return new_game
    
    def print_map(self):
        self.rec_map.print_map()
    
    def return_map(self):
        return self.rec_map.return_map()
    
    def get_winner(self):
        if self.get_cards_quantity(1)==0:
            return 2
        if self.get_cards_quantity(2)==0:
            return 1
        return 0
    
    def play_visual(self, move):
        x, y = move
        Card.visualisation = True
        self.rec_map.update_card(x, y, self.current_player)
        Card.visualisation = False
        self.switch_player()
        maps = copy.deepcopy(Card.visualisation_maps)
        Card.visualisation_maps = []
        maps.append(self.return_map())
        return maps
