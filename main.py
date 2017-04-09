def insert_disc(grid, column, player):
    for row in reversed(grid):
        if row[column] == 0:
            row[column] = player
            return 0
    print('Incorrect Input. This column is already full.')
    return 1

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

def player_turn(grid,player):
    col = None
    rc = 1
    while col is None or rc == 1:
        col = read_input(player)
        if col is not None:
            rc = insert_disc(grid,col,player)

    print_board(grid)
    return check_win(grid)

def print_board(grid):
    for row in grid:
        print(row)
        
def check_win(grid):
    for row in grid: #check horizontal
        p1count = 0
        p2count = 0
        previous = 0
        for column in row:
            if column == previous:
                if column == 1:
                    p1count += 1
                elif column == 2:
                    p2count += 1
            previous = column
            if p1count >= 3:
                print('Player 1 Wins!')
                return True
            elif p2count >= 3:
                print('Player 2 Wins!')
                return True
    for row in grid: #check for a tie
        for column in row:
            if column == 0:
                return False
    print('The game is a tie!')
    return True

if __name__ == '__main__':
    row1 = [0,0,0,0,0,0,0]
    row2 = [0,0,0,0,0,0,0]
    row3 = [0,0,0,0,0,0,0]
    row4 = [0,0,0,0,0,0,0]
    row5 = [0,0,0,0,0,0,0]
    row6 = [0,0,0,0,0,0,0]
    grid = []
    grid.append(row1)
    grid.append(row2)
    grid.append(row3)
    grid.append(row4)
    grid.append(row5)
    grid.append(row6)
    print_board(grid)
    game_over = False
    while not game_over:
        game_over = player_turn(grid,1)
        if not game_over:
            game_over = player_turn(grid,2)


