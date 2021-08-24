import prob


def dfs_search(initial_state):

    frontier = []
    frontier.append(initial_state)

    explored = {}
    num_of_explored_states = 0

    goals_and_paths = []

    while True:
        if len(frontier) == 0:
            return frontier, explored, num_of_explored_states, goals_and_paths

        state = frontier.pop()
        num_of_explored_states += 1
        explored[state.state] = True

        if prob.gen_goal_test(state):
            goal_state = state
            path = []
            while state.parent is not None:
                path.append(state)
                state = state.parent
            path.reverse()
            goals_and_paths.append((goal_state, path))
            state = goal_state
        else:
            for neighbour in prob.neighbours(state):
                if explored.get(neighbour.state) == None and prob.does_not_contain(frontier, neighbour):
                    frontier.append(neighbour)


def solver(initial_tuple):
    initial_state = prob.Node(state=initial_tuple, parent=None)

    frontier, explored, num_of_explored_states, goals_and_paths = dfs_search(
        initial_state)

    for goal, path in goals_and_paths:
        print("\nGoal State: ", goal.state)
        print("Path:")
        for node in path:
            print(node.state)

    print("\nNumber of explored states: ", num_of_explored_states)

    print("Explored States: ")
    for node in explored.keys():
        print(node)


def main():
    # Sample test case:
    # Initial state: (8, 0, 0)
    print("-----DEPTH FIRST SEARCH-----")
    print("Maximum Jar capacity: ", prob.jar_capacity)
    initial_state = (8, 0, 0)  # input()
    print("Initial state: ", initial_state)
    solver(initial_state)


if __name__ == "__main__":
    main()
