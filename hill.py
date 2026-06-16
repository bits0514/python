def objective_function(x):
    # Example function: f(x) = -x^2 + 4x
    return -x**2 + 4*x

def hill_climbing(initial_x, step_size, max_iterations):
    current_x = initial_x
    current_value = objective_function(current_x)

    for _ in range(max_iterations):
        # Generate new candidate solutions
        next_x_up = current_x + step_size
        next_x_down = current_x - step_size

        # Evaluate the new candidates
        next_value_up = objective_function(next_x_up)
        next_value_down = objective_function(next_x_down)

        # Select the candidate with the highest value
        if next_value_up > current_value:
            current_x = next_x_up
            current_value = next_value_up
        elif next_value_down > current_value:
            current_x = next_x_down
            current_value = next_value_down
        else:
            # No improvement, terminate the search
            break

    return current_x, current_value

if __name__ == "__main__":
    # User inputs
    initial_x = float(input("Enter initial guess for x: "))
    step_size = float(input("Enter step size: "))
    max_iterations = int(input("Enter maximum number of iterations: "))

    # Perform hill climbing
    best_x, best_value = hill_climbing(initial_x, step_size, max_iterations)

    print(f"Best solution: x = {best_x}, f(x) = {best_value}")
