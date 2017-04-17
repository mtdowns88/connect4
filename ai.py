import random
from util import check_line_for_pattern
import board

def get_horiz_diag_blockwincol(line, pattern, incrementer):
    result = check_line_for_pattern(line, pattern)
    if result >= 0:
        return result+incrementer
    else:
        return -1

def get_best_column(board, test=False): #computer will always play a winning move or a move that prevents 4 in a row for Player 1 if there is only 1 place to have to block
    blockcol = -1
    wincol = -1
    for index, line in enumerate(board.get_vertical_lines()): #check vertical lines - 3 in a row with an empty slot at the top will cause computer to play there
        if check_line_for_pattern(line, [2,2,2,0]) >= 0:
            wincol = index
        elif check_line_for_pattern(line, [1,1,1,0]) >= 0:
            blockcol = index

    horiz_diag_lines = []
    horiz_diag_lines.extend(board.get_horizontal_lines())
    horiz_diag_lines.extend(board.get_diagonal_lines_all())
    for line in horiz_diag_lines:  #check horizontal and diagonal lines - false positives currently if there is not a disc in the slot below the block/win empty slot. get row index and check the vertical column at that index? check prev line

        if blockcol == -1
            blockcol = get_horiz_diag_blockwincol(line, [0,1,1,1], 0)
        if blockcol == -1:
            blockcol = get_horiz_diag_blockwincol(line, [1,0,1,1], 1)
        if blockcol == -1:
            blockcol = get_horiz_diag_blockwincol(line, [1,1,0,1], 2)
        if blockcol == -1:
            blockcol = get_horiz_diag_blockwincol(line, [1,1,1,0], 3)

        if wincol == -1:
            wincol = get_horiz_diag_blockwincol(line, [0,2,2,2], 0)
        if wincol == -1:
            wincol = get_horiz_diag_blockwincol(line, [2,0,2,2], 1)
        if wincol == -1:
            wincol = get_horiz_diag_blockwincol(line, [2,2,0,2], 2)
        if wincol == -1:
            wincol = get_horiz_diag_blockwincol(line, [2,2,2,0], 3)
            
        if wincol >= 0: #computer should always prioritize a winning move
            return wincol
        elif blockcol >= 0: #next should block player from winning
            return blockcol

    if test == False: 
        return random.randint(0,6) #otherwise, play randomly
    else:
        return -1 #if using for test cases, don't want to return a random number and get a false positive

def ai_turn(board,player): #computer gets the next best move and plays there - if the column is already full, plays again
    col = None
    rc = 1
    while col is None or rc == 1:
        col = get_best_column(board)
        if col is not None:
            print('Computer has made a move.')
            rc = board.insert_disc(col,player)

    board.print_board()
    return board.check_win()
