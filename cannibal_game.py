def is_valid(state):
    # Check if the number of cannibals does not outnumber the number of missionaries on both sides
    return (state[0] >= state[1] or state[0] == 0) and \
           ((3 - state[0]) >= (3 - state[1]) or (3 - state[0]) == 0)

def goal_test(state):
    # Check if all missionaries and cannibals have crossed the river
    return state == (0, 0, 0)

def get_successors(state):
    actions = [(1, 0, 1), (2, 0, 1), (0, 1, 1), (0, 2, 1), (1, 1, 1)]
    successors = []

    for action in actions:
        new_state = (state[0] - action[0], state[1] - action[1], 1 - state[2])
        if is_valid(new_state):
            successors.append((new_state, action))  # Modified to also return the action

    return successors

def solve_missionaries_and_cannibals():
    initial_state = (3, 3, 1)
    frontier = [(initial_state, None)]  # Modified to store the action along with the state
    explored = set()
    parent = {}

    while frontier:
        state, action = frontier.pop(0)
        print("Exploring state:", state, "with action:", action)  # Debugging statement
        if goal_test(state):
            path = []
            current_state = state
            while current_state != initial_state:
                path.insert(0, (current_state, parent[current_state][1]))
                current_state = parent[current_state][0]
            path.insert(0, (initial_state, None))
            return path
        explored.add(state)
        for successor, action in get_successors(state):
            if successor not in explored and (successor, action) not in frontier:
                parent[successor] = (state, action)
                frontier.append((successor, action))

    return None

def print_solution_path(path):
    if path:
        print("Solution Path:")
        for i, (state, action) in enumerate(path):
            if action:
                print(f"Step {i + 1}: {action} - {state}")  # Print the action and state
            else:
                print(f"Step {i + 1}: Start - {state}")  # Indicate the start state
    else:
        print("No solution found.")


if __name__ == "__main__":
    solution_path = solve_missionaries_and_cannibals()
    print_solution_path(solution_path)
