# sudoku-checker 
# loads up a sudoku and checks if its valid 
# create the sudoku structure then validate 
# mainly with using set method
# 
#
# see the wood from the trees

# create the sudoku structure

#sudoku_candidate = [['x' for rows in range(9)] for columns in range(9)]
#print(sudoku_candidate)

sudoku = [[5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1], 
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
       [2,8,7,4,1,9,6,3,5],
       [3,4,5,2,8,6,1,7,8]]

print(sudoku)


# for column in range(9): #create the initial list
#     for row in range(9) : # each of the above elements is a list as well
#         sudoku[column][row] = "*"


    
def validate_row(row_num):
    unique_row = set(sudoku[row_num])
    print(unique_row)
    if (len(unique_row)) == 9:
        return True
    else:
        return False


def validate_column(col_num):
    col = [item[col_num] for item in sudoku] # 
    print(col , "hello")
    return len(set(col)) == 9 


def validate_cell(cel_row, cel_col): #validate a 3x3 grid
    #create a empty list call vals so it can hold a grid then validate if the grid is unique with set
    vals=[]
    #vals must have the first 3 cells for the top of the grid 
    vals = sudoku[cel_row][cel_col:cel_col+3]
    vals.append(sudoku[cel_row+1][cel_col:cel_col+3])
    vals.append(sudoku[cel_row+2][cel_col:cel_col+3])
    unique_block = set(vals)
    print(unique_block)
    if len(unique_block) == 9:
        return True

def validate_sudoku():
    #validate each row
    for row in range (0,9):
        if not validate_row(row):
            return False
    for col in range(0,9):
        if not validate_column(col):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if not validate_cell(i,j):
                return False
    return True



print(sudoku[0])

if validate_sudoku():
    print("Sudoku is valid")
else:
    print("Sudoku is not valid")