import player
import card
import board
import random
import math
# from player import Player


class Game():
    def __init__(self):
        self.board = board.GameBoard()
        self.players = []
        self.init_game()
        #self.reset_game()

    def cardDistributor(self, poker):
        random.shuffle(poker)
        cardsPerPlayer = int(len(poker) / len(self.players))
        print(cardsPerPlayer)
        for index in range(len(self.players)):
            self.players[index].cards = poker[0 + index * cardsPerPlayer: (index + 1) * cardsPerPlayer]

    def set_player_numbers(self, player_numbers, player_names):
        self.players = [player.Player(name) for index, name in zip(range(player_numbers), player_names)]
        print (len(self.players))
        print (self.players[0].display_cards())

    def init_game(self):
        player_numbers = int(input("How many players?\n"))
        player_names = []
        for i in range(player_numbers):
            player_names.append(input("\nType player%d's name:\t" % i))
        self.set_player_numbers(player_numbers, player_names)
        # decks = int(input("How many decks do you want to play?\n"))
        self.cardDistributor(card.FullDeck().cards)
        self.players[0].display_cards()

    def nextRound(self, currentPlayer):
        lastPlayerClime = {}
        while (True):
            playerInfo = currentPlayer.turn(lastPlayerClime)
            if (playerInfo['ifWin']):
                exit()
            if (playerInfo['ifDoubt']):
                if (len(board.Gameboard.DisplayArea) == lastPlayerClime['claim_length']) \
                        and (board.GameBoard.DisplayArea == lastPlayerClime['claim_rank']):
                    currentPlayer.insert_cards(board.GameBoard.DisplayArea)
                    board.GameBoard.delDiscard(board.GameBoard.DisplayArea)
                    board.GameBoard.ClearDisplay()
                    return self.players[(self.players.index(currentPlayer) + 1) % len(self.players)]
                else:
                    lastPlayer = self.players[(self.players.index(currentPlayer) - 1)] if self.players.index(currentPlayer) \
                         else self.players[-1]
                    lastPlayer.insert_cards(board.GameBoard.DisplayArea)
                    board.GameBoard.delDiscard(board.GameBoard.DisplayArea)
                    board.GameBoard.ClearDisplay()
                    return currentPlayer
            if (playerInfo['Pass']):
                return self.players[(self.players.index(currentPlayer) + 1) % len(self.players)]
            else:
                currentPlayer.play_cards(playerInfo['Claim_rank'])
                board.GameBoard.Display(playerInfo['Claim_rank'])
                board.GameBoard.Discard(playerInfo['Claim_rank'])
                return self.players[(self.players.index(currentPlayer) + 1) % len(self.players)]


    def runGame(self):
        currentPlayer = random.choice(self.players)
        while(True):
            nextPlayer = self.nextRound(self, currentPlayer)





if __name__ == "__main__":
    Game()







    


        

