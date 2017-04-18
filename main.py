from board import Board
from ai import ai_turn


def convert_to_int(input_str):
    input_int = 0
    try:
        input_int = int(input_str)
        return input_int
    except ValueError:
        raise ValueError

def check_range(input_int):
    if input_int >= 0 and input_int <= 6:
        return input_int
    else:
        raise ValueError

def read_input(player):
    try:
        return check_range(convert_to_int(input('Player '+str(player)+' indicate column:'))-1)
    except ValueError:
        print('Incorrect Input. Please enter a number between 1 and 7')
        return None

def player_turn(board,player):
    col = None
    rc = 1
    while col is None or rc == 1:
        col = read_input(player)
        if col is not None:
            rc = board.insert_disc(col,player)

    board.print_board()
    return board.check_win()


if __name__ == '__main__':
    board = Board()
    game_over = False
    while not game_over:
        game_over = player_turn(board,1) #add in proper error handling?
        if not game_over:
            #game_over = player_turn(grid,2)
            game_over = ai_turn(board,2)


