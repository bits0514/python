def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(row, board, n):
    if row == n:
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(row + 1, board, n)
            board[row][col] = 0  # backtrack

def print_board(board):
    for row in board:
        line = ""
        for c in row:
            if c == 1:
                line += "Q "
            else:
                line += "_ "
        print(line)
    print()

def main():
    n = int(input("Enter number of queens (n): "))
    board = [[0]*n for _ in range(n)]
    solve_n_queens(0, board, n)

if __name__ == "__main__":
    main()
