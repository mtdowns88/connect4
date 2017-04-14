import random

winCol = None #global var for move that ai needs to make to block Player 1 from winning the game

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

def ai_turn(grid,player):
    global winCol
    col = None
    rc = 1
    while col is None or rc == 1:
        if winCol is not None:
            col = winCol #block Player 1
            winCol = None
        else:
            col = random.randint(0,6)
        print('Computer has made a move.')
        if col is not None:
            rc = insert_disc(grid,col,player)

    print_board(grid)
    return check_win(grid)

def print_board(grid):
    for row in grid:
        print(row)

#################################
def get_horizontal_lines(grid):
    return grid

def get_vertical_lines(grid):
    vertical_list = []
    for col in range(0,7): #check verticals
        line = []
        for row in reversed(grid):
            line.append(row[col])
        vertical_list.append(line)
    return vertical_list

def get_diagonal_lines(grid):
    diagonal_list = []
    for col in range(-2,4): #check diagonals
        n1 = 0
        line = []
        for row in reversed(grid): #going up left to right
            if col+n1 >= 0 and col+n1 <= 6:
                line.append(row[col+n1])
            n1 += 1
        diagonal_list.append(line)
        
        n2 = 0
        line2 = []
        for row in grid: #going down left to right
            if col+n2 >= 0 and col+n2 <= 6:
                line2.append(row[col+n2])
            n2 += 1
        diagonal_list.append(line2)
    return diagonal_list

def get_all_lines(grid):
    all_lines = []
    all_lines.extend(get_horizontal_lines(grid))
    all_lines.extend(get_vertical_lines(grid))
    all_lines.extend(get_diagonal_lines(grid))
    return all_lines

def check_line_for_pattern(line, pattern):
    pattern_length = len(pattern)
    line_length = len(line)
    for i in range(0,line_length-pattern_length+1):
        if line[i:i+pattern_length] == pattern:
            return i
    return -1

def check_win(grid):
    list_of_lines = get_all_lines(grid)
    for line in list_of_lines:
        if check_line_for_pattern(line, [1,1,1,1]) >= 0:
            print('Player 1 Wins!')
            return True
        if check_line_for_pattern(line, [2,2,2,2]) > 0:
            print('Player 2 Wins!')
            return True
    return check_tie(grid)

def check_tie(grid):
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
            #game_over = player_turn(grid,2)
            game_over = ai_turn(grid,2)


