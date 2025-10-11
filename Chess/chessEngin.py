"""
chessEngin.py
Den här filen hanterar logiken för schackbrädet och spelets tillstånd.
"""

class GameState:
    def __init__(self):
        """
        Skapar starttillståndet för spelet.
        Brädet representeras som en 2D-lista (8x8)
        med koder för varje pjäs:
         - '--' betyder tom ruta
         - 'w' = vit, 'b' = svart
         - bokstaven efter färgen anger pjäsens typ:
            R = Rook (torn), N = Knight (springare), B = Bishop (löpare),
            Q = Queen (drottning), K = King (kung), p = pawn (bonde)
        """
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.whiteToMove = True
        self.moveLog = []
