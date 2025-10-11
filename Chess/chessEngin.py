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

    def makeMove(self, move):
        """
        Utför ett drag på brädet.
        Uppdaterar brädet, byter spelare och loggar draget.
        """
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)  # loggar draget för ev. undo
        self.whiteToMove = not self.whiteToMove  # byt spelare


class Move:
    """
    Representerar ett drag i spelet.
    Lagrar start- och slutposition, pjäsen som flyttas och eventuell pjäs som tas.
    """

    # Dictionaries för att konvertera mellan schacknotation och index
    ranksToRows = {"1": 7, "2": 6, "3":5, "4":4, "5":3, "6":2, "7": 1, "8":0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a": 0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        """
        startSq: tuple (rad, kol) för startposition
        endSq: tuple (rad, kol) för slutposition
        board: den aktuella brädbilden (2D-lista)
        """
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]  # pjäsen som flyttas
        self.pieceCaptured = board[self.endRow][self.endCol]    # eventuell pjäs som tas

    def getChessNotation(self):
        """
        Returnerar draget i vanlig schacknotation, t.ex. 'e2e4'.
        """
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        """
        Konverterar rad/kol till schacknotation.
        Exempel: (6,4) -> 'e2'
        """
        return self.colsToFiles[c] + self.rowsToRanks[r]
