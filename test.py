from board import Board
from ai import get_best_column

def test1():
    row1 = [0,0,0,0,0,0,0]
    row2 = [0,0,0,0,0,0,0]
    row3 = [0,0,0,0,0,0,0]
    row4 = [0,0,0,0,0,0,0]
    row5 = [0,0,0,0,0,0,0]
    row6 = [1,1,2,0,2,2,0]
    grid = []
    grid.append(row1)
    grid.append(row2)
    grid.append(row3)
    grid.append(row4)
    grid.append(row5)
    grid.append(row6)
    board = Board(grid)
    return get_best_column(board,True) == 3

def test2():
    row1 = [0,0,0,0,0,0,0]
    row2 = [0,0,0,0,0,0,0]
    row3 = [0,0,2,0,0,0,0]
    row4 = [0,2,1,1,0,0,0]
    row5 = [2,1,1,1,2,0,0]
    row6 = [1,1,1,2,2,0,0]
    grid = []
    grid.append(row1)
    grid.append(row2)
    grid.append(row3)
    grid.append(row4)
    grid.append(row5)
    grid.append(row6)
    board = Board(grid)
    return get_best_column(board,True) == 3

def test3():
    row1 = [0,0,0,0,0,0,0]
    row2 = [0,0,0,0,0,0,0]
    row3 = [0,0,2,1,0,0,0]
    row4 = [0,2,1,1,0,0,0]
    row5 = [2,1,1,1,2,0,0]
    row6 = [1,1,1,2,2,0,0]
    grid = []
    grid.append(row1)
    grid.append(row2)
    grid.append(row3)
    grid.append(row4)
    grid.append(row5)
    grid.append(row6)
    board = Board(grid)
    return board.check_win()

def test4():
    row1 = [0,0,0,0,0,0,0]
    row2 = [0,2,0,0,0,0,0]
    row3 = [0,1,2,0,0,0,0]
    row4 = [0,2,1,2,0,0,0]
    row5 = [2,1,1,1,2,0,0]
    row6 = [1,1,1,2,2,0,0]
    grid = []
    grid.append(row1)
    grid.append(row2)
    grid.append(row3)
    grid.append(row4)
    grid.append(row5)
    grid.append(row6)
    board = Board(grid)
    return board.check_win()

if __name__ == '__main__':
    print(test1())
    print(test2())
    print(test3())
    print(test4())
