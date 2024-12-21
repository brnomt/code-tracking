#Define the game turns
from functions import play_game as pg
import main as m

def turns():
    player1 = 'X'
    player2 = 'O'

    while True:
        if m.nowplaying == 1:
            #This is player1 turn
            pg.play_game()
        else:
        #This is player2 turn
            pg.play_game()
