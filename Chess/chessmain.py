"""
This is the main driver file for the chess game.
It handles:
 - initializing the game window,
 - loading images,
 - drawing the game board and pieces,
 - and processing basic user input.
"""

import pygame as p               # importerar pygame-biblioteket för grafik
from Chess import chessEngin     # importerar vårt egna script med GameState-klassen

# --- KONSTANTER (inställningar för spelet) ---
WIDTH = HEIGHT = 512             # storlek på fönstret (kvadrat 512x512 pixlar)
DIMENSION = 8                    # schackbrädet är 8x8 rutor
SQ_SIZE = HEIGHT // DIMENSION    # storlek på varje ruta i pixlar
MAX_FPS = 15                     # frames per second (hur snabbt spelet ritas om)
IMAGES = {}                      # global dictionary där vi lagrar alla pjäsernas bilder


# --- FUNKTION: Ladda in bilderna för alla pjäser ---
def loadImages():
    """
    Laddar in bilderna för varje pjäs en gång och sparar dem i IMAGES-dictionaryn.
    Detta görs bara en gång i början för att undvika lagg.
    """
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK',   # vita pjäser
              'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']   # svarta pjäser
    
    for piece in pieces:
        # laddar bilden för t.ex. "wp.png" (vit bonde)
        # skalar ner bilden till rätt storlek (SQ_SIZE)
        IMAGES[piece] = p.transform.scale(
            p.image.load("../images/" + piece + ".png"),
            (SQ_SIZE, SQ_SIZE)
        )
    # Nu kan vi senare rita ut en pjäs med IMAGES['wp'] t.ex.


# --- FUNKTION: Huvudloop för spelet ---
def main():
    """
    Huvudloopen för schackspelet.
    - Initierar fönstret
    - Skapar GameState (som innehåller brädets status)
    - Laddar in bilder
    - Kör loopen som lyssnar på händelser och ritar om skärmen
    """
    p.init()                                      # startar pygame
    screen = p.display.set_mode((WIDTH, HEIGHT))  # skapar ett fönster
    clock = p.time.Clock()                        # håller koll på tiden (FPS)
    screen.fill(p.Color("white"))                 # fyller bakgrunden med vitt

    gs = chessEngin.GameState()                   # skapar ett GameState-objekt (vår speldata)
    loadImages()                                  # laddar bilderna EN gång innan loopen

    running = True
    while running:
        # --- Event-hantering ---
        for e in p.event.get():
            if e.type == p.QUIT:                  # om spelaren stänger fönstret
                running = False                   # avsluta loopen

        # --- Rita ut all grafik för spelet ---
        drawGameState(screen, gs)                 # ritar brädet + pjäser
        clock.tick(MAX_FPS)                       # håller konstant FPS
        p.display.flip()                          # uppdaterar hela skärmen


# --- FUNKTION: Ritar hela spelets tillstånd ---
def drawGameState(screen, gs):
    """
    Hanterar alla grafiska delar i nuvarande spelomgång.
    Den anropar två hjälpfunktioner:
     1. drawBoard() – ritar brädets rutor
     2. drawPieces() – ritar pjäser ovanpå rutorna
    """
    drawBoard(screen)
    drawPieces(screen, gs.board)


# --- FUNKTION: Rita rutorna på brädet ---
def drawBoard(screen):
    """
    Ritar själva rutmönstret (8x8).
    Färgerna växlar mellan vit och grå med hjälp av (r + c) % 2.
    """
    colors = [p.Color("white"), p.Color("gray")]      # två färger för rutorna
    for r in range(DIMENSION):                        # loopar genom varje rad
        for c in range(DIMENSION):                    # loopar genom varje kolumn
            color = colors[(r + c) % 2]               # växlar färg mellan 0 och 1
            p.draw.rect(                              # ritar ut rektangel
                screen, color,
                p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE)
            )


# --- FUNKTION: Rita ut pjäserna på brädet ---
def drawPieces(screen, board):
    """
    Ritar ut pjäserna utifrån nuvarande brädstatus (gs.board).
    """
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]           # hämtar pjäsen i raden r, kolumn c
            if piece != "--":             # "--" betyder tom ruta
                # ritar bilden på rätt plats
                screen.blit(IMAGES[piece], 
                            p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


# --- Starta spelet ---
if __name__ == "__main__":
    main()
