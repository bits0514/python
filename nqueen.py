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

def count_solutions(board, row, n):
    if row == n:
        return 1
    count = 0
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            count += count_solutions(board, row + 1, n)
            board[row][col] = 0
    return count

def find_one_solution(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if find_one_solution(board, row + 1, n):
                return True
            board[row][col] = 0
    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()

def main():
    n = int(input("Enter the number of queens (N): "))
    board = [[0]*n for _ in range(n)]

    # Count all solutions
    total = count_solutions(board, 0, n)

    # Find and display one solution
    found = find_one_solution(board, 0, n)

    if found:
        print("\nOne valid solution:")
        print_board(board)
        print(f"Total number of solutions: {total}")
    else:
        print("No solution exists for N =", n)

if __name__ =="__main__":
    main()

   
    
