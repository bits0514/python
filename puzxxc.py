from collections import deque

def get_input():
    print("Enter the 8-puzzle configuration as a single line of numbers from 0 to 8 (e.g., '1 2 3 4 5 6 7 8 0'):")
    while True:
        try:
            data = input().strip().split()
            if len(data) != 9:
                raise ValueError("Input must contain exactly 9 numbers.")
            puzzle = [int(num) for num in data]
            if sorted(puzzle) != list(range(9)):
                raise ValueError("Input must be a permutation of numbers 0 to 8.")
            return puzzle
        except ValueError as e:
            print(f"Invalid input: {e} Please try again.\n")

def is_solvable(puzzle):
    inversion_count = sum(
        1
        for i in range(len(puzzle))
        for j in range(i + 1, len(puzzle))
        if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]
    )
    return inversion_count % 2 == 0

def bfs(start):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    queue = deque([(start, [start])])  # Start included in path
    visited = set([start])
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        zero_index = current.index(0)
        row, col = divmod(zero_index, 3)
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_puzzle = list(current)
                new_puzzle[zero_index], new_puzzle[new_index] = new_puzzle[new_index], new_puzzle[zero_index]
                new_state = tuple(new_puzzle)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))
    return None

def print_puzzle(puzzle):
    for i in range(0, 9, 3):
        print(puzzle[i:i+3])
    print()

def main():
    puzzle = get_input()
    if not is_solvable(puzzle):
        print("The provided puzzle configuration is not solvable.")
        return

    solution = bfs(tuple(puzzle))
    if solution is None:
        print("No solution found.")
    else:
        print(f"Solution found in {len(solution) - 1} moves:\n")
        for i, step in enumerate(solution):
            print(f"Step {i}:")
            print_puzzle(step)

if __name__ == "__main__":
    main()
