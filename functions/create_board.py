#Function to create the board matrix.

def create_board():

#Board Layout
#  - | - | -
#  - | - | -
#  - | - | -

    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    for row in board:
        final_board = (' | '.join(row))
    return final_board

