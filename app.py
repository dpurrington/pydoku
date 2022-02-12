#! /usr/bin/env python
import numpy

board = numpy.matrix([
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
        ])

regions = [
        [[0,2],[0,2]],
        [[3,5],[0,2]],
        [[6,8],[0,2]],
        [[0,2],[3,5]],
        [[3,5],[3,5]],
        [[6,8],[3,5]],
        [[0,2],[6,8]],
        [[3,5],[6,8]],
        [[6,8],[6,8]]
        ]

def get_region_ranges(x,y) :
    for region in regions:
        if x >= region[0][0] and \
            x <= region[0][1] and \
            y >= region[1][0] and \
            y <= region[1][1] :

                x_range = range(region[0][0], region[0][1] + 1)
                y_range = range(region[1][0], region[1][1] + 1)
                return x_range, y_range

def is_valid(x, y, v) :
    #check the row
    if v in board[:,x] : return False
    #check the column
    if v in board[y,:] : return False

    (x_range, y_range) = get_region_ranges(x,y)

    # look for the value in the region
    for x in x_range:
        for y in y_range:
            if v == board[y,x] :
                return False

    return True

def solve() :
    global board
    for y in range(9) :
        for x in range (9) :
            if (board[y,x] == 0) :
                # empty cell, let's try things
                for v in range(1,10) :
                    if is_valid(x, y, v) :
                        board[y,x] = v
                        solve()
                        # backtrack
                        board[y,x] = 0
                return
    print(board)
    input("More?")


if __name__ == '__main__' :
    solve()
