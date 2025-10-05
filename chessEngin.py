""" this class is responsible for starting all the införmation aboout the current state of a chess game or responsible for determining the vaild moves current state. it will also keep a move log"""

class GameState():
    def __init__(self):
        # create 2D list. it will be list of list

        # the bord is an 8x8 2D list, eaach element of the list had 2 charachters.
        # the second charachter represent the color of the piece, black or white
        # the second charachter represent the type of the piece "K", "W", "R", "B", "N" or "P".
        # the "--" represent an empty space with no piece on the chess bord

        self.bord = [
            
            # the black side on the chess bord
            ["bR", "bN", "bB", "bQ", "bB", "bN", "bN"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp"],

            # how to we define empty space in the chess bord.
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],

            # the white side on the chess bord
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wB", "wN", "wN"]



        ]


        # white are the one who alaways start the game
        self.whiteToMove = True


        # här kan man senare lägga till logging av drag. t.ex för att kunna ångra drag.
        self.moveLog = []


