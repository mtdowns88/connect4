
def check_line_for_pattern(line, pattern): #check to see if the pattern list passed in is a subset of the line list. if it is, returns the start position of the pattern list.
    pattern_length = len(pattern)
    line_length = len(line)
    for i in range(0,line_length-pattern_length+1):
        if line[i:i+pattern_length] == pattern:
            return i
    return -1

def diagonal_iterator(grid):
    diagonal_list = []
    for col in range(-2,4): #check diagonals - have to "pad" diagonal lines that start below the bottom row or above the top row to ensure correct column positioning
        n = 0
        if col < 1:
            line = []
        elif col == 1:
            line = [-1]
        elif col == 2:
            line = [-1,-1]
        elif col == 3:
            line = [-1,-1,-1]
        for row in grid:
            if col+n >= 0 and col+n <= 6:
                line.append(row[col+n])
            n += 1
        diagonal_list.append(line)
        
    return diagonal_list
