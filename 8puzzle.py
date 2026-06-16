from collections import deque

def get_input():
    print("Enter the 8-puzzle configuration as a single line of numbers from 0 to 8 (e.g., '1 2 3 4 5 6 7 8 0'):")
    while True:
        try:
            data = input().strip().split()
            if len(data) != 9:
                raise ValueError("Invalid input length.")
            puzzle = [int(num) for num in data]
            if sorted(puzzle) != list(range(9)):
                raise ValueError("Input must be a permutation of numbers 0 to 8.")
            return puzzle
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def is_solvable(puzzle):
    inversion_count = sum(
        1
        for i in range(len(puzzle))
        for j in range(i + 1, len(puzzle))
        if puzzle[i] and puzzle[j] and puzzle[i] > puzzle[j]
    )
    return inversion_count % 2 == 0

def bfs(start):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    queue = deque([(start, [])])
    visited = set([start])
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        zero_index = current.index(0)
        zero_row, zero_col = divmod(zero_index, 3)
        for move_row, move_col in moves:
            new_row, new_col = zero_row + move_row, zero_col + move_col
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_puzzle = list(current)
                new_puzzle[zero_index], new_puzzle[new_index] = new_puzzle[new_index], new_puzzle[zero_index]
                new_puzzle_tuple = tuple(new_puzzle)
                if new_puzzle_tuple not in visited:
                    visited.add(new_puzzle_tuple)
                    queue.append((new_puzzle_tuple, path + [new_puzzle_tuple]))
    return None

def main():
    puzzle = get_input()
    if not is_solvable(puzzle):
        print("The provided puzzle configuration is not solvable.")
        return
    solution = bfs(tuple(puzzle))
    if solution is None:
        print("No solution found.")
    else:
        print("Solution steps:")
        for step in solution:
            print_puzzle(step)

def print_puzzle(puzzle):
    for i in range(0, 9, 3):
        print(puzzle[i:i+3])
    print()

if __name__ == "__main__":
    main()
