#Function to define if someone won the game.

def did_someone_won(board):
    # Check if someone won in the rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True

    # Check if someone won in the columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return True

    # Check if someone won in the diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False