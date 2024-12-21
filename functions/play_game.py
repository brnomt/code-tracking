from turns import turns as t

nowplaying = t.turns()
def place(nowplaying):
    if nowplaying == 1:
        return 'X'
    else:
        return 'O'

def play_game(board):
    while True:
        opc = int(input('Choose a position to play (1-9): '))
        if opc.isdigit() and 1 <= int(opc) <= 9 and board[int(opc) - 1] == ' ':
            board[opc-1]= place()
            break
        else:
            print('Invalid position. Choose a position between 1 and 9.')
