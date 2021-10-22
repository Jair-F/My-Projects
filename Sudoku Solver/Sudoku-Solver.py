import os
import sys
os.system("clear")

"""
    Our Sudoku Board looks like this!
       0  1  2   3  4  5   6  7  8
    A [1  2  3 | 4  5  6 | 7  8  9],
    B [1  2  3 | 4  5  6 | 7  8  9],
    C [1  2  3 | 4  5  6 | 7  8  9],
      ---------|---------|---------
    D [1  2  3 | 4  5  6 | 7  8  9],
    E [1  2  3 | 4  5  6 | 7  8  9],
    F [1  2  3 | 4  5  6 | 7  8  9],
      ---------|---------|---------
    G [1  2  3 | 4  5  6 | 7  8  9],
    H [1  2  3 | 4  5  6 | 7  8  9],
    I [1  2  3 | 4  5  6 | 7  8  9]

    Grids:
        colums -->    
rows   0  1  2   3  4  5   6  7  8
 |  0 [0       |         |        ],
 |  1 [   0    |    1    |    2   ],
    2 [        |         |        ],
      ---------|---------|----------
    3 [        |         |        ],
    4 [   3    |    4    |    5   ],
    5 [        |         |        ],
      ---------|---------|----------
    6 [        |         |        ],
    7 [   6    |    7    |    8   ],
    8 [        |         |        ]
"""

sudoku_board = [
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None]
]

def get_numbers_in_row(row:int) -> list:
    """
        return the numbers in the row(for example A)
    """
    ret = list()
    for colum in sudoku_board[row]:
        if colum != None:
            ret.append(colum)
    return ret

def get_numbers_in_colum(colum:int) -> list:
    """
    """
    ret = list()
    for row in sudoku_board:
        grid = row[colum]
        if grid != None:
            ret.append(grid)
    return ret

def get_numbers_in_grid(begin_row:int, begin_colum:int) -> list:
    """
        specify one point in the sudoku_board and the function will return the numbers set in this grid
    """    
    while begin_row % 3 != 0:  # if the row is divideable by 3 we are at the first number of this grid
        begin_row -= 1
    
    while begin_colum % 3 != 0:  # if the colum is divideable by 3 we are at the first number of this grid
        begin_colum -= 1
    
    ret = list()
    for row in range(3):
        for colum in range(3):
            num = sudoku_board[begin_row + row][begin_colum + colum]
            if num != None:
                ret.append(num)
    return ret

def check_sudoku_board() -> bool:
    """
        
    """
    for i in range(9):  # Check the the horizontal and vertical lines
        row_nums   = get_numbers_in_row(i)
        colum_nums = get_numbers_in_colum(i)
        row_nums.sort()
        colum_nums.sort()
        
        if len(row_nums) != 9 or len(colum_nums) != 9:
            print("Board is not entirely full!", file=sys.stderr)
            return False

        for a in range(9):
            if row_nums[i] != i+1 or colum_nums[i] != i+1:
                return False
        #print(grid_nums)
        #print(row_nums)
        #print(colum_nums)
        #print()

    for rows in range(0, 6 + 1, 3):   #checking the grids
        for colums in range(0, 6 + 1, 3):
            grid_nums  = get_numbers_in_grid(rows, colums)
            grid_nums.sort()

            for a in range(9):
                if grid_nums[i] != i+1:
                    return False
    return True

def check_fully_filled(sudoku_board:list[list]) -> bool:
    """
        checks if every field in the sudoku_board is up - if the board is entirely filled
    """
    for row in sudoku_board:
        for colum in row:
            if colum == None:
                return False
    return True

def solve_sudoku(sudoku_board:list[list]) -> bool:
    """
        Returns if there is a solution for this board - if it could solve it
    """

    if check_fully_filled(sudoku_board) == True:
        return check_sudoku_board() # if the board is right, it will return true else false

    board_backup = list()
    for row in sudoku_board:    # make a deep copy of the board
        board_backup.append(row.copy())

    """
        this list stores at every position of the field the posibillities, which could be filled in
        this list looks like:
        posibillites_to_fill_in = [
        
        This is one position, were the posibillities are stored in, we can which could be at this position
                                                   |
        [[posibilliteis we can fill in],[1,2,3,4].[ ]],
        [[],[],[]],
         .
         .
         .
        ]
    """
    all_posibillities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    posibillities_to_fill_in = list()
    lowest_num_of_possibilities = 1
    

    for row in range(len(sudoku_board)):    # parsing for numbers, we can fill in
        posibillities_to_fill_in.append(list()) # append an new row
        for colum in range(len(sudoku_board[row])):
            posibillities_to_fill_in[row].append(list()) # append an new colum(as liste - there will the posibillies be stored in)
            
            if sudoku_board[row][colum] != None:    # if at this position there is already a number - continue - we dont can put in there a number
                continue

            used_numbers = get_numbers_in_colum(colum) + get_numbers_in_row(row) + get_numbers_in_grid(row, colum)
            used_numbers = list(set(used_numbers)) # remove duplicates
            posibillities_to_fill_in[row][colum] = [item for item in all_posibillities if item not in used_numbers] # add the numbers, which are not in used_numbers, but in all_posibillities
            
            num_of_possibillities = len(posibillities_to_fill_in[row][colum])
            lowest_num_of_possibilities = num_of_possibillities if num_of_possibillities < lowest_num_of_possibilities else lowest_num_of_possibilities
            #print(row, ':', colum, ' ->', used_numbers, '-> possibillities: ', posibillities_to_fill_in[row][colum])

    #for row in posibillites_to_fill_in:
    #    print(row)
    
    for row in range(len(sudoku_board)):    # filling in one number
        for colum in range(len(sudoku_board[row])):
            if sudoku_board[row][colum] != None:   # if the field is already filled up
                continue
            num_of_possibillities = len(posibillities_to_fill_in[row][colum])
            if num_of_possibillities == lowest_num_of_possibilities:
                for possibillity in posibillities_to_fill_in[row][colum]:
                    sudoku_board[row][colum] = possibillity
                    if solve_sudoku(sudoku_board) == True:
                        return True

                #if num_of_possibillities == 1:
                #    sudoku_board[row][colum] = posibillities_to_fill_in[row][colum][0]
                #elif num_of_possibillities == lowest_num_of_possibilities:
                #    for possibillity in posibillities_to_fill_in[row][colum]:
                #        pass    # call us self
            
            # !!!!!!!!! make here a board backup
    return False


def print_board():
    for row in sudoku_board:
        for colum in row:
            print(colum if colum != None else ' ', ',', end='')
        print()

if __name__ == "__main__":
    #for row in range(len(sudoku_board)):
    #    for colum in range(len(sudoku_board[row])):
    #        sudoku_board[row][colum] = 10
    #print_board()
    #print(check_fully_filled(sudoku_board))

    with open("sudoku_board.txt", "r") as file:
        row = 0
        for line in file:
            line = line.strip()
            line = line.replace(' ', '')
            nums = line.split(',')
            for i in range(len(nums)):
                sudoku_board[row][i] = int(nums[i]) if nums[i] != '' else None
            row += 1
    

    if solve_sudoku(sudoku_board) == True:
        print("solved board!!")
    else:
        print("doesnt solved board!!")
    
    print_board()