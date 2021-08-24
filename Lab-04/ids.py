import prob

# Global variables
explored = {}
goals_and_paths = []


def dls_search(cur_state, cur_depth, depth_limit):
    explored[cur_state.state] = True

    # print(cur_depth)

    if depth_limit < cur_depth:
        # print(f"Depth Limit Exceeded: {cur_depth} > {depth_limit}")
        return False

    if prob.gen_goal_test(cur_state):
        goal_state = cur_state
        path = []
        while cur_state.parent is not None:
            path.append(cur_state)
            cur_state = cur_state.parent
        path.reverse()
        goals_and_paths.append((goal_state, path))
        cur_state = goal_state
        return True
    else:
        for neighbour in prob.neighbours(cur_state):
            # print(cur_depth, depth_limit, cur_state.state, neighbour.state, explored.get(neighbour.state))
            if explored.get(neighbour.state) == None:
                if dls_search(neighbour, cur_depth + 1, depth_limit):
                    return True


def solver(initial_tuple):
    initial_state = prob.Node(state=initial_tuple, parent=None)

    limit = 1
    total = 0

    while(1):
        if dls_search(initial_state, 0, limit):
            print(f"\nSolution found: Depth = [{limit}]")
            total += len(explored)
            break
        else:
            print(
                f"No solution for depth [{limit}] => Explored {len(explored)} states")

        total += len(explored)
        explored.clear()
        limit += 1
        # print(limit)

    for goal, path in goals_and_paths:
        print("\nGoal State: ", goal.state)
        print("Path:")
        for node in path:
            print(node.state)

    print(f"\nNumber of explored statesat depth [{limit}]: {len(explored)} ")

    print(f"Explored States at depth [{limit}]: ")
    for node in explored.keys():
        print(node)

    print(f"Total number of explored states = {total}")


def main():
    # Sample test case:
    # Initial state: (8, 0, 0)
    print("-----ITERATIVE DEEPENING SEARCH-----")
    print("Maximum Jar capacity: ", prob.jar_capacity)
    initial_state = (8, 0, 0)  # input()
    print("Initial state: ", initial_state)
    solver(initial_state)


if __name__ == "__main__":
    main()
