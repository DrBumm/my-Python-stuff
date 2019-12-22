# Als erstes erstellen wir uns ein spiel wo wir die KI implementieren wollen
# Bei mir wird es Tik Tak Toe

# Wir brauchen ein Board, 1 spieler, check algorithmus und eine KI

import os
import sys


class TikTakToe:
    def __init__(self):
        self.b = []
        for i in range(9):
            self.b.append("")

        print("Wer beginnt? [player 1 (p1) | player 2 (p2)]?\n")
        while True:
            self.starting_player = input()
            if self.starting_player == "p1":
                print("Ist player " + self.starting_player[1] + " richtig? [y|n]\n")
                self.player_right = input()
            elif self.starting_player == "p2":
                print("Ist player " + self.starting_player[1] + " richtig? [y|n]\n")
                self.player_right = input()
            else:
                print("Du musst für player 1 p1 eingeben oder für player 2 p2\n")

            if self.player_right == "y":
                break
            elif self.player_right == "n":
                print("Bitte jetzt neu wählen\n")

    def print_board(self):
        b = self.b
        print(b[0], "|", b[1], "|", b[2], "\n",
              b[3], "|", b[4], "|", b[5], "\n",
              b[6], "|", b[7], "|", b[8])

    def player_1(self):
        b = self.b
        while True:
            try:
                p1_turn = int(input("Wo willst du deinh zeichen (X) machen? [1-9]\n"))
            except ValueError:
                print("Du musst eine Zahl von 1 bis 9 wählen\n")

            if p1_turn in [1, 2, 3, 4, 5, 6, 6, 8, 9]:
                if b[p1_turn-1] == "O" or b[p1_turn-1] == "X":
                    print("Feld Wird schon benutzt\n")
                else:
                    b[p1_turn-1] = "X"
                    self.b = b

    def player_2(self):
        b = self.b
        while True:
            try:
                p2_turn = int(input("Wo willst du deinh zeichen (O) machen? [1-9]\n"))
            except ValueError:
                print("Du musst eine Zahl von 1 bis 9 wählen\n")

            if p2_turn in [1, 2, 3, 4, 5, 6, 6, 8, 9]:
                if b[p2_turn-1] == "O" or b[p2_turn-1] == "X":
                    print("Feld Wird schon benutzt\n")
                else:
                    b[p2_turn-1] = "X"
                    self.b = b

    def check_win(self):
        return


game = TikTakToe()
while True:
    # This code is by Tornax07 thanks to him
    # For Windows
    if sys.platform == "win32":
        os.system('cls')
    # For Linux
    else:
        os.system('clear')

    # Mac wird nicht supported da ich und Tornax07 nicht wissen wie man die Konsole cleared in Mac

    game.print_board()

    if game.starting_player == "p1":
        game.player_1()
    else:
        game.player_2()

    if game.starting_player == "p2":
        game.player_2()
    else:
        game.player_1()

    game.check_win()
