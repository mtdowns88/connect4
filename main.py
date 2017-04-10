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
        
def check_win(grid): #TODO: create test that inputs all winning scenarios?
    global winCol
    for row in grid: #check horizontals
        p1count = 0
        p2count = 0
        previous = 0
        for index, column in enumerate(row):
            if column == previous:
                if column == 1:
                    p1count += 1
                elif column == 2:
                    p2count += 1
            else: #reset counters back to zero
                p1count = 0
                p2count = 0
            previous = column
            if p1count >= 3:
                print('Player 1 Wins!')
                return True
            elif p2count >= 3:
                print('Player 2 Wins!')
                return True
            elif p1count >= 2 and column == previous and column == 1 and row[index+1] == 0: #if player 1 has 3 in a row horizontally and the next spot is blank, set winCol to the next column to the right
                winCol = index+1 #TODO: this only works if the column to block is on the right, implement for left side
    for col in range(0,7): #check verticals
        p1count = 0
        p2count = 0
        previous = 0
        for index, row in enumerate(reversed(grid)):
            if row[col] == previous:
                if row[col] == 1:
                    p1count += 1
                elif row[col] == 2:
                    p2count += 1
            else: #reset counters back to zero
                p1count = 0
                p2count = 0
            previous = row[col]
            if p1count >= 3:
                print('Player 1 Wins!')
                return True
            elif p2count >= 3:
                print('Player 2 Wins!')
                return True
            elif p1count >= 2 and row[col] == previous and row[col] == 1 and grid[6-index-2][col] == 0: #if player 1 has 3 in a row vertically and the next spot is blank, set winCol to the current column
                print(6-index-2)
                print(col)
                winCol = col
    for col in range(-2,4): #check diagonals
        p1count1 = 0
        p2count1 = 0
        previous1 = 0
        n1 = 0
        for row in reversed(grid): #going up left to right
            if col+n1 <= 6 and col+n1 >= 0:
                if row[col+n1] == previous1:
                    if row[col+n1] == 1:
                        p1count1 += 1
                    elif row[col+n1] == 2:
                        p2count1 += 1
                previous1 = row[col+n1]
                if p1count1 >= 3:
                    print('Player 1 Wins!')
                    return True
                elif p2count1 >= 3:
                    print('Player 2 Wins!')
                    return True
            n1 += 1
        
        p1count2 = 0
        p2count2 = 0
        previous2 = 0
        n2 = 0
        for row in grid: #going down left to right
            if col+n2 <= 6 and col+n2 >= 0:
                if row[col+n2] == previous2:
                    if row[col+n2] == 1:
                        p1count2 += 1
                    elif row[col+n2] == 2:
                        p2count2 += 1
                previous2 = row[col+n2]
                if p1count2 >= 3:
                    print('Player 1 Wins!')
                    return True
                elif p2count2 >= 3:
                    print('Player 2 Wins!')
                    return True
            n2 += 1
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


