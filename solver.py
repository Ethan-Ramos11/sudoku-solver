
N = 9
def printBoard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print("\n")
    print() 
def validBoard(board, row, col, num):
    for c in range(9):
        if board[row][c] == num:
            return False
    for r in range(9):
        if board[r][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True
def solveSudoku(board, row, col):
    if row == N - 1 and col == N:
        return True
    if col == N:
        col = 0
        row = row + 1
    if board[row][col] > 0:
        return solveSudoku(board, row, col + 1)
    for num in range(1,10):
        if validBoard(board, row, col, num):
            board[row][col] = num

            if solveSudoku(board, row, col + 1):
                return True
        board[row][col] = 0
    return False
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
