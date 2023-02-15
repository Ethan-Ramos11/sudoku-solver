N = 9
def printBoard(board:list[list]):
    '''
    Description:
    Iterates through the board and prints out each element of the sudoku board
    '''
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print("\n")
    print() 
def validBoard(board:list[list], row: int, col: int , num: int) -> bool:
    '''
    Description:
    validBoard(board: list[list], row: int, col: int, num: int) -> bool
    Param: list[list] representing an unsolved sudoku board
           Two int representing current row and column we are trying to check 
           Int representing the number we are trying to insert
    Output: True if the number is valid based on the rules of sudoku
            False if the number is invalid based on the rules of sudoku
    '''
    #checks if the number we want to input is in a corresponding row
    for c in range(9):
        if board[row][c] == num:
            return False
    #checks if the number we want to input is in a corresponding column
    for r in range(9):
        if board[r][col] == num:
            return False
    #checks if the number we want to input is within the particular 3 x 3 matrix
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudoku(board: list[list], row: int, col: int) -> bool:
    '''
    Description:
    solveSudoku(board: list[list], row: int, col: int) -> bool
    param: list[list] representing an unsolved sudoku board
           Two int representing current row and column we are trying to check 
    output: returns whether the sudoku board is solved
    '''
    # Checks if we reached the last cell of the board
    if row == N - 1 and col == N:
        return True
    # Checks if we reached the last column
    # If so set the column to 0 and iterate to the next row
    if col == N:
        col = 0
        row = row + 1
    # checks to see if a cell is solved then moves to the next column
    if board[row][col] > 0:
        return solveSudoku(board, row, col + 1)
    
    for num in range(1,10):
        if validBoard(board, row, col, num):
            board[row][col] = num

            if solveSudoku(board, row, col + 1):
                return True
        board[row][col] = num
    return False
#Driver code 
board = [[0,0,0,0,5,0,9,4,0],
         [1,0,0,0,3,2,0,0,0],
         [0,0,0,8,0,0,0,0,0],
         [4,0,7,0,0,5,0,0,0],
         [2,0,0,0,0,1,8,0,0],
         [0,0,0,7,0,0,0,0,6],
         [9,0,0,0,8,0,0,1,3],
         [0,4,0,0,7,0,0,2,0],
         [0,0,5,0,0,0,0,0,0]
]
if solveSudoku(board, 0, 0):
    printBoard(board)
else:
    print("invalid board")