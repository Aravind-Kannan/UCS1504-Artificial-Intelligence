import prob

# Global variables
explored = {}
goals_and_paths = []


def dls_search(cur_state, cur_depth, depth_limit):
    explored[cur_state.state] = True

    if depth_limit < cur_depth:
        print("Depth Limit Exceeded: ", cur_depth)
        return

    if prob.gen_goal_test(cur_state):
        goal_state = cur_state
        path = []
        while cur_state.parent is not None:
            path.append(cur_state)
            cur_state = cur_state.parent
        path.reverse()
        goals_and_paths.append((goal_state, path))
        cur_state = goal_state
        return
    else:
        for neighbour in prob.neighbours(cur_state):
            if explored.get(neighbour.state) == None:
                dls_search(neighbour, cur_depth + 1, depth_limit)


def solver(initial_tuple):
    initial_state = prob.Node(state=initial_tuple, parent=None)

    limit = 8  # Hard coded

    # limit = 6 -> (1,4,3)
    # limit = 9 -> (4,1,3)

    dls_search(initial_state, 0, limit)

    for goal, path in goals_and_paths:
        print("\nGoal State: ", goal.state)
        print("Path:")
        for node in path:
            print(node.state)

    print("\nNumber of explored states: ", len(explored))

    print("Explored States: ")
    for node in explored.keys():
        print(node)


def main():
    # Sample test case:
    # Initial state: (8, 0, 0)
    print("-----DEPTH LIMITED SEARCH-----")
    print("Maximum Jar capacity: ", prob.jar_capacity)
    initial_state = (8, 0, 0)  # input()
    print("Initial state: ", initial_state)
    solver(initial_state)


if __name__ == "__main__":
    main()
