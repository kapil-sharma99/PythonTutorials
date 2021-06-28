# <!-----Global Variables-----!>
# Game board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-", ]
# If game is still goind
game_still_going = True
# Who won or title
winner = None
# Whos turn it is
current_player = 'X'


def display_board():
    print(board[0] + " | ", board[1], " | " + board[2])
    print(board[3] + " | ", board[4], " | " + board[5])
    print(board[6] + " | ", board[7], " | " + board[8])


def handle_turn(player):
    print(player + " 's turn.")
    position = input("Choose a position from 1-9: ")
    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid position. Choose a position from 1-9")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("Position already filled!! Choose another one...")
    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_rows():
    # Setting up the game_still_going in global mode
    global game_still_going
    # Check if any of the row have all the same value(and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner(X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # Setting up the game_still_going in global mode
    global game_still_going
    # Check if any of the column have all the same value(and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner(X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # Setting up the game_still_going in global mode
    global game_still_going
    # Check if any of the diagonals have all the same value(and is not empty)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    # If any diagonals does have a match, flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    # return the winner(X or O)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


def check_for_winner():
    # Setting up the winner variable in global mode
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        # There was a win
        winner = row_winner
    elif column_winner:
        # There was a win
        winner = column_winner
    elif diagonal_winner:
        # There was a win
        winner = diagonal_winner
    else:
        # There was no win
        winner = None
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # Global variable we need
    global current_player
    # If current player is X then change it to O and vice versa
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


def play_game():
    # display initial board
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + " Won...!!")
    elif winner == None:
        print("It's a Tie...!")


play_game()
