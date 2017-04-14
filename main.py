import random

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
    col = None
    rc = 1
    while col is None or rc == 1:
        col = get_best_column(grid)
        if col is not None:
            print('Computer has made a move.')
            rc = insert_disc(grid,col,player)

    print_board(grid)
    return check_win(grid)

def print_board(grid):
    for row in grid:
        print(row)

def get_horizontal_lines(grid):
    return grid

def get_vertical_lines(grid):
    vertical_list = []
    for col in range(0,7): #check verticals
        line = []
        for row in reversed(grid): #list is generated in ascending order
            line.append(row[col])
        vertical_list.append(line)
    return vertical_list

def get_diagonal_lines(grid): #make this 1 function that takes in either grid or reversed(grid) as as argument and call it twice
    diagonal_list = []
    for col in range(-2,4): #check diagonals
        n1 = 0
        if col < 1:
            line = []
        elif col == 1:
            line = [-1]
        elif col == 2:
            line = [-1,-1]
        elif col == 3:
            line = [-1,-1,-1]
        for row in reversed(grid): #going up left to right
            if col+n1 >= 0 and col+n1 <= 6:
                line.append(row[col+n1])
            n1 += 1
        diagonal_list.append(line)
        
        n2 = 0
        if col < 1:
            line2 = []
        elif col == 1:
            line2 = [-1]
        elif col == 2:
            line2 = [-1,-1]
        elif col == 3:
            line2 = [-1,-1,-1]
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
    tie = True
    for line in list_of_lines:
        if check_line_for_pattern(line, [1,1,1,1]) >= 0:
            print('Player 1 Wins!')
            return True
        elif check_line_for_pattern(line, [2,2,2,2]) >= 0:
            print('Player 2 Wins!')
            return True
        elif check_line_for_pattern(line, [0]) >= 0:
            tie = False
    if tie:
        print('The game is a tie!')
        return True
    else:
        return False

def get_best_column(grid):
    blockcol = -1
    wincol = -1
    for index, line in enumerate(get_vertical_lines(grid)): #check vertical lines
        if check_line_for_pattern(line, [1,1,1,0]) >= 0:
            blockcol = index
        elif check_line_for_pattern(line, [2,2,2,0]) >= 0:
            wincol = index

    horiz_diag_lines = []
    horiz_diag_lines.extend(get_horizontal_lines(grid))
    horiz_diag_lines.extend(get_diagonal_lines(grid))
    for line in horiz_diag_lines: #check horizontal and diagonal lines - false positives currently if there is not a disc in the slot below the block/win empty slot. get row index and check the vertical column at that index?
        pattern1a = check_line_for_pattern(line, [0,1,1,1])
        if pattern1a >= 0:
            blockcol = pattern1a
        pattern1b = check_line_for_pattern(line, [1,0,1,1])
        if pattern1b >= 0:
            blockcol = pattern1b+1
        pattern1c = check_line_for_pattern(line, [1,1,0,1])
        if pattern1c >= 0:
            blockcol = pattern1c+2
        pattern1d = check_line_for_pattern(line, [1,1,1,0])
        if pattern1d >= 0:
            blockcol = pattern1d+3
        pattern2a = check_line_for_pattern(line, [0,2,2,2])
        if pattern2a >= 0:
            wincol = pattern2a
        pattern2b = check_line_for_pattern(line, [2,0,2,2])
        if pattern2b >= 0:
            wincol = pattern2b+1
        pattern2c = check_line_for_pattern(line, [2,2,0,2])
        if pattern2c >= 0:
            wincol = pattern2c+2
        pattern2d = check_line_for_pattern(line, [2,2,2,0])
        if pattern2d >= 0:
            wincol = pattern2d+3
            
    if wincol >= 0: #computer should always prioritize a winning move
        return wincol
    elif blockcol >= 0: #next should block player from winning
        return blockcol
    else: #otherwise, play randomly for now
        return random.randint(0,6)

if __name__ == '__main__': #add in test cases?
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
        game_over = player_turn(grid,1) #add in proper error handling
        if not game_over:
            #game_over = player_turn(grid,2)
            game_over = ai_turn(grid,2)


