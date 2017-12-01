#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import player
import card
import board
# import math
# from player import Player


class Game():
    def __init__(self):
        '''
        Attributes are defined here
        Game Initialization is delegated to init_game()
        Attributes:
            self.board : Pubilc Decks
            self.players : List of Player Infomations
            self.pack_num  : Numbers of Pack of Cards
        '''
        self.board = board.GameBoard()
        self.players = []
        self.pack_num = 0
        card.FullDeck() # initial card.FullDeck
        self.init_game()
        self.run_game()

    # def cardDistributor(self, poker):
    #     random.shuffle(poker)
    #     cardsPerPlayer = int(len(poker) / len(self.players))
    #     print(cardsPerPlayer)
    #     for index in range(len(self.players)):
    #         self.players[index].cards = poker[0 + index * cardsPerPlayer: (index + 1) * cardsPerPlayer]

    def set_player_numbers(self, player_numbers, player_names):
        self.players = [player.Player(name) for index, name in zip(range(player_numbers), player_names)]
        print (len(self.players))
        print (self.players[0].display_cards())

    def init_game(self):
        '''
        Parameters that will not change till the program ends
            will be initialized in this function.
        Paremeters that are initialized here include:
            player_numbers
            player_name for each player
            pack_numbers
        '''
        player_numbers = int(input("How many players?\n"))
        player_names = []
        for i in range(player_numbers):
            player_names.append(input("\nType player%d's name:\t" % i))
        self.set_player_numbers(player_numbers, player_names)
        self.pack_num = int(input("How many decks do you want to play?\n"))

    def next_round(self, currentPlayer):
        PassCount = 0
        lastPlayerClaim = {}  #dict(claim_length:int, claim_rank:card_rank)
        IsNewTurn = True  # or TurnCount
        while (True):
            playerInfo = currentPlayer.turn(IsNewTurn)
            IsNewTurn = False
            if (playerInfo['Win']):
                return None
            elif playerInfo['Choice'] == 'Claim':
                lastPlayerClaim = playerInfo['Claim']
                currentPlayer.play_cards(playerInfo['Cards'])
                board.GameBoard.Display(playerInfo['Cards'])
            elif playerInfo['Choice'] == 'Qustion':
                LastPlayerCards = board.GameBoard.GetDisplayArea[len(board.GameBoard.GetDisplayArea()) \
                            - len(playerInfo['Cards']): len(board.GameBoard.GetDisplayArea())]
                temp = []
                for i in LastPlayerCards:
                    temp.append(i)
                if set(temp) == set(lastPlayerClaim['Claim_rank']):
                    # Doubt Failed
                    currentPlayer.insert_cards(board.GameBoard.GetDisplayArea)
                    board.GameBoard.ClearDisplay()
                    return self.players[(self.players.index(currentPlayer) + 1) % len(self.players)]
                else:
                    # Doubt Succeeded
                    lastPlayer = self.players[self.players.index(currentPlayer) - PassCount]
                    lastPlayer.insert_cards(board.GameBoard.DisplayArea)
                    board.GameBoard.ClearDisplay()
                    return currentPlayer
            elif playerInfo['Choice'] == 'Pass':
                PassCount += 1
                if PassCount == len(self.Players) - 1:
                    return currentPlayer

            elif (playerInfo['Choice'] == 'Follow'):
                # or claim
                # Actual Played Card are different from what he claimed*******
                currentPlayer.play_cards(playerInfo['Cards'])
                board.GameBoard.Display(playerInfo['Cards'])
                lastPlayerClaim = playerInfo['Claim']
                PassCount = 0

    def run_game(self):
        self.reset_game()
        currentPlayer = random.choice(self.players)
        while(currentPlayer):
            nextPlayer = self.next_round(currentPlayer)
            currentPlayer = nextPlayer

    def reset_game(self):
        '''
        Reset the game to its initial state
        Steps of reset progress are as follows:
            1.Reset pubilc card Piles
            2.Deal cards to players
        '''
        # step 1
        self.board.ResetBoard()
        # step 2
        cardsPerPlayer = int(54 * self.pack_num / len(self.players))
        index = 0
        for hand in self.board.Deal(cardsPerPlayer, len(self.players)):
            self.players[index].initial_cards(hand)
            index += 1
        return 

if __name__ == "__main__":
    Game()















