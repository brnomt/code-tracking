#Tic-Tac-Toe
import random
import functions.did_someone_won as dsw
import functions.create_board as cb
from functions.turns import turns as t

nowplaying = random.randint(1, 2)


board=cb.create_board()

t.turns()

