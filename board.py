from util import check_line_for_pattern
from util import diagonal_iterator

class Board():
    grid = []
    
    def __init__(self, grid=None): #create a new empty board unless a board is passed in for testing
        if grid is not None:
            self.grid = grid
        else:
            row1 = [0,0,0,0,0,0,0]
            row2 = [0,0,0,0,0,0,0]
            row3 = [0,0,0,0,0,0,0]
            row4 = [0,0,0,0,0,0,0]
            row5 = [0,0,0,0,0,0,0]
            row6 = [0,0,0,0,0,0,0]
            self.grid.append(row1)
            self.grid.append(row2)
            self.grid.append(row3)
            self.grid.append(row4)
            self.grid.append(row5)
            self.grid.append(row6)
            self.print_board()

    def get_horizontal_lines(self): #returns a list of lists containing all horizontal lines going left to right
        return self.grid

    def get_vertical_lines(self): #returns a list of lists containing all vertical lines going bottom to top (ascending order)
        vertical_list = []
        for col in range(0,7):
            line = []
            for row in reversed(self.grid):
                line.append(row[col])
            vertical_list.append(line)
        return vertical_list

    def get_diagonal_lines_up(self): #returns a list of lists containing all diagonal lines of at least 4 spots long going up left to right
        return diagonal_iterator(list(reversed(self.grid)))

    def get_diagonal_lines_down(self): #returns a list of lists containing all diagonal lines of at least 4 spots long going down left to right
        return diagonal_iterator(self.grid)

    def get_diagonal_lines_all(self): #returns a list of lists containing all diagonal lines of at least 4 spots long - going up and going down
        diagonal_lines = []
        diagonal_lines.extend(self.get_diagonal_lines_up())
        diagonal_lines.extend(self.get_diagonal_lines_down())
        return diagonal_lines

    def get_all_lines(self): #returns a list of lists containing all lines on the board
        all_lines = []
        all_lines.extend(self.get_horizontal_lines())
        all_lines.extend(self.get_vertical_lines())
        all_lines.extend(self.get_diagonal_lines_all())
        return all_lines

    def check_win(self): #checks for Player 1 win, Player 2 win, or tie
        list_of_lines = self.get_all_lines()
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

    def insert_disc(self,column,player): #inserts a disc belonging to the indicated player into the first available spot in the column indicated
        for row in reversed(self.grid):
            if row[column] == 0:
                row[column] = player
                return 0
        print('Incorrect Input. This column is already full.')
        return 1

    def print_board(self): #prints the board contained in this object
        for row in self.grid:
            rowstring = '|'
            for disc in row:
                rowstring = rowstring + str(disc)
                rowstring = rowstring + '|'
            print(rowstring)
