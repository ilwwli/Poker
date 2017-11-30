import player
import card
import board

class Game():
    def __init__(self):
        self.board = board.GameBoard()
        self.players = []
        self.init_game()
        #self.reset_game()       

    def set_player_numbers(self, player_numbers, player_names):
        self.players = [player.Player(name) for index, name in zip(player_numbers, player_names)]

    def init_game(self):
        player_numbers = int(input("How many players?\n"))
        player_names = []
        for i in range(player_numbers):
            player_names.append(input("\nType player%d's name:\t" % i))
        self.set_player_numbers(player_numbers, player_names)
        decks = int(input("How many decks do you want to play?\n"))


    


        

